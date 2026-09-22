#!/usr/bin/env python3
"""Combine approved components into candidate settlement names.

The output is planning material. A generated name is not canon. Examine real
place names and trademarks before Terrace selects a candidate.
"""

import argparse
import csv
import itertools
import random
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_COMPONENTS = ROOT / "world" / "place-name-components.tsv"


def load_components(path):
    groups = {"root": [], "suffix": []}
    with path.open(encoding="utf-8", newline="") as source:
        for row in csv.DictReader(source, delimiter="\t"):
            kind = row["kind"]
            if kind not in groups:
                raise SystemExit(f"unknown component kind: {kind}")
            groups[kind].append(row)
    if not groups["root"] or not groups["suffix"]:
        raise SystemExit("the component file needs roots and suffixes")
    return groups


def candidates(groups, terrain=None):
    pairs = itertools.product(groups["root"], groups["suffix"])
    results = []
    for root, suffix in pairs:
        tags = set(root["terrain"].split(",")) | set(suffix["terrain"].split(","))
        if terrain and terrain not in tags:
            continue
        results.append((root["component"] + suffix["component"], root, suffix))
    return results


def self_test():
    groups = load_components(DEFAULT_COMPONENTS)
    names = {name for name, _, _ in candidates(groups)}
    assert "aldermere" in names
    assert "weirwick" in names
    assert [name for name, _, _ in candidates(groups, "coastal")] == [
        "alderwick",
        "weirmere",
        "weirwick",
    ]
    print("place-names self-test: ok")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--components", type=Path, default=DEFAULT_COMPONENTS)
    parser.add_argument("--terrain", help="keep names with this terrain tag")
    parser.add_argument("--count", type=int, help="maximum number of names")
    parser.add_argument("--seed", type=int, default=0, help="shuffle seed")
    parser.add_argument("--explain", action="store_true", help="show meanings")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        return

    results = candidates(load_components(args.components), args.terrain)
    random.Random(args.seed).shuffle(results)
    if args.count is not None:
        if args.count < 1:
            parser.error("--count must be positive")
        results = results[:args.count]

    for name, root, suffix in results:
        if args.explain:
            print(
                f"{name.title()}\t{root['component']} ({root['meaning']}) + "
                f"{suffix['component']} ({suffix['meaning']})"
            )
        else:
            print(name.title())


if __name__ == "__main__":
    main()
