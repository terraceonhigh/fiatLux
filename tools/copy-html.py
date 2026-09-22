#!/usr/bin/env python3
"""Copy an HTML file with the platform clipboard command."""

from pathlib import Path
import shutil
import subprocess
import sys


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: copy-html.py <file.html>")

    path = Path(sys.argv[1])
    if not path.is_file():
        raise SystemExit(f"no such file: {path}")

    commands = (
        ("pbcopy", ["pbcopy"]),
        ("wl-copy", ["wl-copy", "--type", "text/html"]),
        ("xclip", ["xclip", "-selection", "clipboard", "-t", "text/html"]),
    )
    for executable, command in commands:
        if shutil.which(executable):
            with path.open("rb") as source:
                subprocess.run(command, stdin=source, check=True)
            print(f"clipboard <- {path} ({path.stat().st_size} bytes)")
            return

    raise SystemExit("no clipboard command found: install pbcopy, wl-copy, or xclip")


if __name__ == "__main__":
    main()
