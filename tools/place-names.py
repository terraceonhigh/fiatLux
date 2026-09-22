#!/usr/bin/env python3
"""Blend real British Columbia and Washington settlement names.

The output is planning material. A generated name is not canon. Examine real
place names, language origins, and trademarks before Terrace selects a name.
"""

import argparse
import csv
import random
import re
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CORPUS = ROOT / "world" / "place-name-corpus.tsv"


def load_names(path, jurisdiction=None):
    with path.open(encoding="utf-8", newline="") as source:
        rows = list(csv.DictReader(source, delimiter="\t"))
    if jurisdiction:
        rows = [row for row in rows if row["jurisdiction"] == jurisdiction]
    if len(rows) < 2:
        raise SystemExit("the corpus needs at least two source names")
    return rows


def compact(name):
    text = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z]", "", text.lower())


def blend(left, right, left_cut, right_cut):
    first = compact(left)[:left_cut]
    second = compact(right)[right_cut:]
    if first[-1:] == second[:1]:
        second = second[1:]
    return (first + second).title()


def candidates(rows, count, seed):
    rng = random.Random(seed)
    source_names = {compact(row["name"]) for row in rows}
    results = []
    used = set()
    attempts = 0
    while len(results) < count and attempts < count * 1000:
        attempts += 1
        left, right = rng.sample(rows, 2)
        left_text = compact(left["name"])
        right_text = compact(right["name"])
        if len(left_text) < 5 or len(right_text) < 5:
            continue
        left_cut = rng.randrange(2, len(left_text) - 1)
        right_cut = rng.randrange(1, len(right_text) - 2)
        name = blend(left["name"], right["name"], left_cut, right_cut)
        key = name.lower()
        if not 6 <= len(name) <= 14 or key in source_names or key in used:
            continue
        used.add(key)
        results.append((name, left, right, left_cut, right_cut))
    if len(results) < count:
        raise SystemExit(f"made only {len(results)} candidates after {attempts} attempts")
    return results


def self_test():
    rows = load_names(DEFAULT_CORPUS)
    assert len(rows) == 440
    first = candidates(rows, 5, 0)
    second = candidates(rows, 5, 0)
    assert first == second
    source_names = {compact(row["name"]) for row in rows}
    assert all(compact(name) not in source_names for name, *_ in first)
    print("place-names self-test: ok")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--jurisdiction", choices=("BC", "WA"))
    parser.add_argument("--count", type=int, default=20)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--explain", action="store_true", help="show source names")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        return
    if args.count < 1:
        parser.error("--count must be positive")

    rows = load_names(args.corpus, args.jurisdiction)
    for name, left, right, left_cut, right_cut in candidates(rows, args.count, args.seed):
        if args.explain:
            print(
                f"{name}\t{left['jurisdiction']}:{left['name']}[:{left_cut}] + "
                f"{right['jurisdiction']}:{right['name']}[{right_cut}:]"
            )
        else:
            print(name)


if __name__ == "__main__":
    main()
