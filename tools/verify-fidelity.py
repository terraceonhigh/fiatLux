#!/usr/bin/env python3
"""Check that generated HTML says exactly what the markdown said.

Two failure modes this exists to catch, both of which have actually happened:

  1. pandoc quietly rewriting the prose (smart quotes curling apostrophes,
     an entity dropping a character) — caught by comparing word lists.
  2. a tag AO3 will strip or choke on — caught by the allowlist.

Usage:  verify-fidelity.py <source.md> <built.html>
        verify-fidelity.py --self-test
        verify-fidelity.py --no-storyboard <source.md>
"""

import html
import re
import sys

# What AO3's "plain text with limited HTML" actually keeps: the `elements:`
# array of Sanitize::Config::ARCHIVE, in the otwarchive source at
# config/initializers/gem-plugin_config/sanitizer_config.rb. That file is
# ground truth — anything outside it the Archive strips on save, silently.
# Re-check against that file rather than the user-facing FAQ
# (archiveofourown.org/faq/formatting-content-on-ao3-with-html): the FAQ is
# prose about the sanitiser, the sanitiser is what runs, and the two can
# drift. The point of the set is that a human looks before posting, so err
# toward flagging: a tag wrongly listed here gets blessed and then eaten.
ALLOWED = {
    "p", "br", "hr", "em", "strong", "i", "b", "u", "s", "strike", "del", "ins",
    "sub", "sup", "a", "blockquote", "q", "cite", "code", "pre", "small", "big",
    "center", "h1", "h2", "h3", "h4", "h5", "h6", "ol", "ul", "li", "dl", "dt",
    "dd", "table", "thead", "tbody", "tfoot", "tr", "th", "td", "caption",
    "col", "colgroup", "div", "span", "img", "details", "summary", "ruby",
    "rt", "rp", "figure", "figcaption", "abbr", "acronym", "address", "dfn",
    "kbd", "samp", "tt", "var",
}


def html_words(text):
    """Visible words of an HTML fragment.

    Tags are removed with NO replacement character: `<em>shut up</em>.` must
    tokenise as ["shut", "up."], matching the markdown `*shut up*.`. Substituting
    a space here splits the period into its own token and produces a phantom
    mismatch.
    """
    return html.unescape(re.sub(r"<[^>]*>", "", text)).split()


def md_words(text):
    """Visible words of the markdown, with syntax that becomes markup removed.

    Handles exactly the constructs the manuscript actually uses. That is
    deliberate: if a new one appears — a link, a list — this will mismatch and
    fail the build, which is the point. A blanket "strip all punctuation that
    might be syntax" would silently normalise away a real difference between
    source and output.

    Headings and pipe tables were added when the manuscript acquired a chapter
    that is a document rather than prose (the loaf formula). The table rule row
    must go before the pipes do, or its dashes survive as words.

    Strikeout arrived with a sign that was amended rather than replaced. The
    non-obvious part is on the other side: pandoc's HTML writer emits <del> for
    `~~`, not the <s> you would guess, so ALLOWED above has to carry del. Only
    the doubled marker is stripped — a lone `~` is prose and must survive on
    both sides or it becomes a phantom mismatch of its own.
    """
    text = re.sub(r"^---\s*$", "", text, flags=re.M)     # scene break -> <hr>
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.M)   # heading     -> <hN>
    text = re.sub(r"^\|[\s|:-]+\|\s*$", "", text, flags=re.M)  # rule  -> (nothing)
    text = text.replace("|", " ")                        # cell edge   -> <td>
    text = text.replace("~~", "")                        # strikeout   -> <del>
    text = text.replace("*", "")                         # emphasis    -> <em>
    return text.replace("`", "").split()                 # code span   -> <code>


def bad_tags(text):
    found = {t.lower() for t in re.findall(r"<\s*/?\s*([A-Za-z][A-Za-z0-9]*)", text)}
    return sorted(found - ALLOWED)


def storyboard_lines(text):
    """Return line numbers that contain reserved storyboard markers."""
    return [
        number
        for number, line in enumerate(text.splitlines(), start=1)
        if line.startswith("[STORYBOARD:")
    ]


def check(md_path, html_path):
    md = open(md_path, encoding="utf-8").read()
    ht = open(html_path, encoding="utf-8").read()
    problems = []

    a, b = html_words(ht), md_words(md)
    if a != b:
        detail = f"word count {len(a)} in html vs {len(b)} in markdown"
        for i, (x, y) in enumerate(zip(a, b)):
            if x != y:
                detail = f"first difference at word {i}: html {x!r} vs markdown {y!r}"
                break
        problems.append(f"text differs from source — {detail}")

    if extra := bad_tags(ht):
        problems.append(f"tags outside AO3's allowlist: {', '.join(extra)}")

    if non_ascii := [c for c in ht if ord(c) > 127]:
        problems.append(
            f"{len(non_ascii)} non-ASCII character(s) survived --ascii "
            f"(e.g. {non_ascii[0]!r}) — these will mangle when pasted"
        )

    return problems


def self_test():
    assert html_words("<p><em>shut up</em>.</p>") == ["shut", "up."], "tag strip must not insert space"
    assert html_words("<p>Br&#xE9;al</p>") == ["Bréal"], "entities must decode"
    assert md_words("*shut up*.") == ["shut", "up."], "emphasis markers must drop"
    assert md_words("a\n\n---\n\nb") == ["a", "b"], "scene break must drop"
    assert md_words("`waitlisted`") == ["waitlisted"], "code span must drop"
    assert md_words("*a*") == html_words("<p><em>a</em></p>"), "round trip"
    assert md_words("`a`") == html_words("<p><code>a</code></p>"), "code round trip"
    assert md_words("~~him~~") == ["him"], "strikeout markers must drop"
    assert md_words("~~him~~") == html_words("<p><del>him</del></p>"), "strikeout round trip"
    assert md_words("~5 miles") == html_words("<p>~5 miles</p>"), "lone tilde is prose, not syntax"
    assert bad_tags("<p><del>x</del></p>") == [], "pandoc's strikeout tag must be allowed"
    assert bad_tags("<p>x</p><script>y</script>") == ["script"], "allowlist must flag script"
    assert bad_tags("<p><em>x</em><hr /></p>") == [], "allowed tags must pass"
    assert storyboard_lines("prose\n[STORYBOARD: Add the turn.]\nprose") == [2]
    assert storyboard_lines("[ordinary brackets]") == []
    print("verify-fidelity self-test: ok")


def main():
    if sys.argv[1:] == ["--self-test"]:
        return self_test()
    if len(sys.argv) == 3 and sys.argv[1] == "--no-storyboard":
        md_path = sys.argv[2]
        markers = storyboard_lines(open(md_path, encoding="utf-8").read())
        if markers:
            joined = ", ".join(str(line) for line in markers)
            sys.exit(f"FAIL {md_path}: storyboard marker(s) remain on line(s) {joined}")
        print(f"ok {md_path} (no storyboard markers)")
        return
    if len(sys.argv) != 3:
        sys.exit(__doc__)

    md_path, html_path = sys.argv[1], sys.argv[2]
    if problems := check(md_path, html_path):
        print(f"FAIL {html_path}", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        sys.exit(1)

    words = len(md_words(open(md_path, encoding="utf-8").read()))
    print(f"ok {html_path} ({words} words, verified against {md_path})")


if __name__ == "__main__":
    main()
