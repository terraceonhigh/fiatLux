#!/usr/bin/env python3
"""Push a built chapter into an already-posted AO3 chapter.

AO3 has no API. Editing a chapter is a plain Rails form, so this does what the
browser does: GET the edit page, read every control in the chapter form, swap
only chapter[content] for the built HTML, and POST the whole form back with
the login cookie. Every other field (title, summary, notes, pseuds, the
checkbox twins Rails plants) is carried through untouched, so nothing blanks.

Default is a DRY RUN. Nothing is sent unless --post is given.

Usage:  ao3-publish.py --slug 01-continuity-test --html build/01-continuity-test.html
        ao3-publish.py --chid 239850826 --html build/01-continuity-test.html --post
        ao3-publish.py --self-test

Cookie: the full Cookie header string from a logged-in browser session, via
$AO3_COOKIE or --cookie-file. Never stored, never printed.
"""

import argparse
import http.client
import http.cookiejar
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser

WORK = 89851861
BASE = "https://archiveofourown.org"
HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_MAP = os.path.join(HERE, "ao3-chapters.tsv")
CONTENT_FIELD = "chapter[content]"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/17.4 Safari/605.1.15"
)
TRANSIENT = {429, 502, 503, 525}
BACKOFF = (5, 15, 45)


# ---------------------------------------------------------------- form parse

class FormParser(HTMLParser):
    """Collect (name, value) pairs from every form on the page, keyed by action.

    Pairs, not a dict: Rails repeats names (pseud ids as `...[ids][]`, and a
    hidden `x=0` twin before every checkbox). Deduping would drop authors.
    Submit buttons are kept separately so the caller can choose exactly one.
    """

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.forms = []          # [{action, method, fields, submits}]
        self._form = None
        self._select = None      # (name, multiple, [selected values], [all values])
        self._textarea = None    # (name, [chunks])

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "form":
            self._form = {"action": a.get("action", ""), "method": a.get("method", "get"),
                          "fields": [], "submits": []}
            self.forms.append(self._form)
            return
        if self._form is None or "disabled" in a:
            return
        name = a.get("name")
        if tag == "input" and name:
            t = (a.get("type") or "text").lower()
            if t in ("file", "image", "reset", "button"):
                return
            if t == "submit":
                self._form["submits"].append((name, a.get("value", "")))
            elif t in ("checkbox", "radio"):
                if "checked" in a:
                    self._form["fields"].append((name, a.get("value", "on")))
            else:
                self._form["fields"].append((name, a.get("value", "")))
        elif tag == "button" and name and (a.get("type") or "submit").lower() == "submit":
            self._form["submits"].append((name, a.get("value", "")))
        elif tag == "textarea" and name:
            self._textarea = (name, [])
        elif tag == "select" and name:
            self._select = (name, "multiple" in a, [], [])
        elif tag == "option" and self._select is not None:
            v = a.get("value", "")
            self._select[3].append(v)
            if "selected" in a:
                self._select[2].append(v)

    def handle_data(self, data):
        if self._textarea is not None:
            self._textarea[1].append(data)

    def handle_endtag(self, tag):
        if tag == "form":
            self._form = None
        elif tag == "textarea" and self._textarea is not None:
            name, chunks = self._textarea
            self._form["fields"].append((name, "".join(chunks)))
            self._textarea = None
        elif tag == "select" and self._select is not None:
            name, multiple, sel, all_ = self._select
            if sel:
                for v in (sel if multiple else sel[:1]):
                    self._form["fields"].append((name, v))
            elif all_ and not multiple:
                self._form["fields"].append((name, all_[0]))
            self._select = None


def chapter_form(page, chid):
    """The one form on the edit page that posts to /chapters/<chid>."""
    p = FormParser()
    p.feed(page)
    hits = [f for f in p.forms if re.search(rf"/chapters/{chid}(?:$|[/?])", f["action"])]
    if not hits:
        return None
    return hits[0]


def pick_submit(submits):
    """Exactly one submit pair. The chapter form offers Preview, Update,
    Cancel; sending all is the same as clicking all."""
    want = [s for s in submits if re.search(r"update|post without preview", s[1], re.I)]
    if len(want) != 1:
        raise SystemExit(f"cannot pick a submit button from {submits!r} "
                         f"(need exactly one matching 'update')")
    return want[0]


def rebuild(form, new_content):
    """Same form, chapter[content] swapped, one submit button. Returns
    (pairs, old_content)."""
    old = None
    pairs = []
    for name, value in form["fields"]:
        if name == CONTENT_FIELD:
            old = value
            value = new_content
        pairs.append((name, value))
    if old is None:
        raise SystemExit(f"form has no {CONTENT_FIELD} field")
    pairs.append(pick_submit(form["submits"]))
    return pairs, old


# ------------------------------------------------------------------ network

def cookie_jar(header):
    jar = http.cookiejar.CookieJar()
    for part in header.split(";"):
        if "=" not in part:
            continue
        k, v = part.strip().split("=", 1)
        jar.set_cookie(http.cookiejar.Cookie(
            0, k, v, None, False, "archiveofourown.org", True, False, "/", True,
            True, None, False, None, None, {}))
    return jar


def fetch(opener, url, data=None, referer=None):
    """One request with gentle retries on the transient signals only."""
    for attempt, delay in enumerate(BACKOFF + (None,)):
        req = urllib.request.Request(url, data=data, headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml",
            "Accept-Language": "en-US,en;q=0.9",
            **({"Referer": referer} if referer else {}),
            **({"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"} if data else {}),
        })
        try:
            with opener.open(req, timeout=60) as r:
                body = r.read().decode("utf-8", "replace")
                status, final, retry_after = r.status, r.geturl(), r.headers.get("Retry-After")
        except urllib.error.HTTPError as e:
            try:
                body = e.read().decode("utf-8", "replace")
            except (http.client.HTTPException, OSError):
                body = ""   # error page truncated too; the status code is enough
            status, final, retry_after = e.code, e.geturl(), e.headers.get("Retry-After")
            if status not in TRANSIENT:
                return status, final, body
        except (urllib.error.URLError, http.client.HTTPException, OSError) as e:
            # dropped connection, truncated chunked body, DNS blip: network-level, retry
            status, final, body, retry_after = 0, url, "", None
            print(f"  network error: {e}", file=sys.stderr)
        transient = status == 0 or status in TRANSIENT or "Retry later" in body
        if not transient:
            return status, final, body
        if delay is None:
            raise SystemExit(f"gave up after {attempt} retries: HTTP {status} from {url}")
        wait = int(retry_after) if retry_after and retry_after.isdigit() else delay
        print(f"  transient HTTP {status}, retrying in {wait}s", file=sys.stderr)
        time.sleep(wait)


def flash(body):
    m = re.search(r'<div[^>]+class="[^"]*\bflash\b[^"]*"[^>]*>(.*?)</div>', body, re.S)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(1))).strip() if m else ""


def succeeded(body, chid):
    """Did the POST land? The final URL cannot tell: Rails redirects a good
    update to /chapters/<chid>, and re-renders a failed one at that same URL.
    The edit form coming back (validation error, or Preview) is the tell."""
    if "successfully updated" in body.lower():
        return True
    if chapter_form(body, chid) is not None:
        return False
    if re.search(r'class="[^"]*\bflash\b[^"]*\berror\b', body) or re.search(r'class="[^"]*\berror\b[^"]*\bflash\b', body):
        return False
    return True


# --------------------------------------------------------------------- main

def resolve_chid(slug, chid, map_path):
    if chid:
        return chid
    if not slug:
        raise SystemExit("need --slug or --chid")
    with open(map_path, encoding="utf-8") as f:
        for line in f:
            cols = line.split()
            if len(cols) == 2 and cols[0] == slug:
                return cols[1]
    raise SystemExit(f"{slug} is not in {map_path}; add it or pass CHID=<id>")


def load_cookie(args):
    if args.cookie_file:
        return open(args.cookie_file, encoding="utf-8").read().strip()
    c = os.environ.get("AO3_COOKIE", "").strip()
    if not c:
        raise SystemExit("no cookie: set $AO3_COOKIE or pass --cookie-file")
    return c


def publish(args):
    chid = resolve_chid(args.slug, args.chid, args.map)
    new = open(args.html, encoding="utf-8").read()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar(load_cookie(args))))
    edit_url = f"{BASE}/works/{WORK}/chapters/{chid}/edit"
    post_url = f"{BASE}/works/{WORK}/chapters/{chid}"

    print(f"GET {edit_url}", flush=True)
    status, final, body = fetch(opener, edit_url)
    if "/users/login" in final or status in (401, 403):
        raise SystemExit("cookie not accepted: the edit page redirected to login")
    if status != 200:
        raise SystemExit(f"edit page returned HTTP {status} ({final})")
    form = chapter_form(body, chid)
    if form is None:
        raise SystemExit("no chapter form on the page: cookie accepted but not the owner? "
                         "or AO3 changed the form action")

    pairs, old = rebuild(form, new)
    names = sorted({n for n, _ in pairs})
    print(f"form -> {post_url}")
    print(f"fields ({len(pairs)}): {', '.join(names)}")
    print(f"{CONTENT_FIELD}: {len(old)} -> {len(new)} chars ({len(new) - len(old):+d})")

    if not args.post:
        print("DRY RUN: nothing sent. Add --post (make ... POST=1) to submit.")
        return

    print(f"POST {post_url}", flush=True)
    data = urllib.parse.urlencode(pairs).encode("utf-8")
    status, final, body = fetch(opener, post_url, data=data, referer=edit_url)
    ok = status == 200 and succeeded(body, chid)
    msg = flash(body)
    if ok:
        print(f"PASS chapter {chid} updated ({final}){' : ' + msg if msg else ''}")
    else:
        print(f"FAIL HTTP {status} at {final}{' : ' + msg if msg else ''}", file=sys.stderr)
        sys.exit(1)


# ---------------------------------------------------------------- self-test

FIXTURE = """
<html><body>
<form action="/works/search" method="get"><input name="work_search[query]" value="x">
<input type="submit" name="commit" value="Search"></form>
<form action="/works/89851861/chapters/239850826" method="post" id="edit_chapter">
  <input type="hidden" name="_method" value="patch">
  <input type="hidden" name="authenticity_token" value="TOK123">
  <input type="text" name="chapter[title]" value="Continuity &amp; Test">
  <select name="chapter[author_attributes][ids][]" multiple>
    <option value="1">a</option><option value="2" selected>terraceonhigh</option>
    <option value="3" selected>coauthor</option>
  </select>
  <input name="chapter[published_at]" value="2026-08-21" disabled>
  <input type="hidden" name="chapter[wip]" value="0">
  <input type="checkbox" name="chapter[wip]" value="1" checked>
  <textarea name="chapter[summary]">old summary</textarea>
  <textarea name="chapter[content]">&lt;p&gt;old &amp; stale&lt;/p&gt;</textarea>
  <input type="submit" name="preview_button" value="Preview">
  <input type="submit" name="post_button" value="Update">
  <input type="submit" name="cancel_button" value="Cancel">
</form>
<form action="/users/logout" method="post"><input type="hidden" name="_method" value="delete">
<input type="submit" name="commit" value="Log out"></form>
</body></html>
"""


def self_test():
    form = chapter_form(FIXTURE, "239850826")
    assert form is not None, "must find the chapter form by action"
    assert chapter_form(FIXTURE, "999") is None, "wrong chid must not match"
    pairs, old = rebuild(form, "<p>new</p>")
    d = {}
    for k, v in pairs:
        d.setdefault(k, []).append(v)
    assert old == "<p>old & stale</p>", f"textarea must unescape: {old!r}"
    assert d[CONTENT_FIELD] == ["<p>new</p>"], "content must be swapped"
    assert d["authenticity_token"] == ["TOK123"], "token must survive"
    assert d["_method"] == ["patch"], "method override must survive"
    assert d["chapter[title]"] == ["Continuity & Test"], "title must survive, unescaped"
    assert d["chapter[summary]"] == ["old summary"], "summary must survive"
    assert d["chapter[author_attributes][ids][]"] == ["2", "3"], "both pseuds must survive"
    assert d["chapter[wip]"] == ["0", "1"], "hidden twin then checked box, in order"
    assert "chapter[published_at]" not in d, "disabled controls must not be sent"
    assert "work_search[query]" not in d and d.get("commit") is None, "other forms must not leak"
    assert "post_button" in d and "preview_button" not in d and "cancel_button" not in d, \
        "exactly the Update button"
    body = urllib.parse.urlencode(pairs)
    assert "chapter%5Bcontent%5D=%3Cp%3Enew%3C%2Fp%3E" in body, "body must carry new content"
    jar = cookie_jar("_otwarchive_session=abc; remember_user_token=def; junk")
    req = urllib.request.Request(f"{BASE}/works/{WORK}/chapters/1/edit")
    jar.add_cookie_header(req)
    assert "remember_user_token=def" in req.get_header("Cookie", ""), "jar must attach the cookie to AO3 requests"
    notice = '<div class="flash notice">Chapter was <b>successfully updated</b>.</div>'
    assert not flash("<p>x</p>") and flash(notice) == "Chapter was successfully updated."
    assert succeeded(notice, "239850826"), "notice flash is a PASS"
    assert not succeeded(FIXTURE, "239850826"), "edit form coming back is a FAIL"
    assert not succeeded('<div class="flash error">Nope</div><p>view</p>', "239850826"), "error flash is a FAIL"
    assert succeeded("<p>chapter view, no flash</p>", "239850826"), "plain chapter view is a PASS"
    print("ao3-publish self-test: ok")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--slug", help="manuscript slug, looked up in the tsv map")
    ap.add_argument("--chid", help="AO3 chapter id; overrides --slug")
    ap.add_argument("--html", help="built HTML file to send")
    ap.add_argument("--map", default=DEFAULT_MAP)
    ap.add_argument("--cookie-file", help="file holding the Cookie header (else $AO3_COOKIE)")
    ap.add_argument("--post", action="store_true", help="actually submit (default is dry run)")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if not args.html:
        ap.error("--html is required")
    publish(args)


if __name__ == "__main__":
    main()
