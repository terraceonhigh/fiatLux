#!/usr/bin/env python3
"""Render a chapter markdown file to AO3-safe HTML.

    python3 manuscript/to-ao3.py manuscript/00-ante-finem-mundi.md

Writes <name>.ao3.html beside it. Paste that into the AO3 editor with
**HTML mode toggled on** -- AO3 does not parse markdown, so pasting the
.md directly shows literal asterisks.

    *italics*  ->  <em>italics</em>     (the dialogue convention)
    ---        ->  <hr />               (section breaks)
    paragraph  ->  <p>paragraph</p>
    `code`     ->  plain text           (AO3 allows no code element)
"""
import html
import pathlib
import re
import sys


def convert(md: str) -> str:
    out = []
    for block in (b.strip() for b in md.split("\n\n")):
        if not block:
            continue
        if block == "---":
            out.append("<hr />")
            continue
        b = html.escape(block, quote=False)  # escape before adding our own tags
        b = b.replace("`", "")
        b = re.sub(r"\*(.+?)\*", r"<em>\1</em>", b, flags=re.S)
        out.append(f"<p>{b}</p>")
    return "\n\n".join(out) + "\n"


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    src = pathlib.Path(sys.argv[1])
    dst = src.with_suffix(".ao3.html")
    text = convert(src.read_text())
    dst.write_text(text)
    print(f"{dst}  ({text.count('<p>')} paragraphs, "
          f"{text.count('<em>')} italic runs, {text.count('<hr />')} breaks)")


def _selftest() -> None:
    got = convert("One *two* three.\n\n---\n\n`x` & <y>")
    assert got == "<p>One <em>two</em> three.</p>\n\n<hr />\n\n<p>x &amp; &lt;y&gt;</p>\n", got
    print("ok")


if __name__ == "__main__":
    _selftest() if "--selftest" in sys.argv else main()
