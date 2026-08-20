# Fiat Lux

Post-collapse fiction. A university outlives the end of state power, becomes a regional capital, and keeps penicillin-level medicine and a working pharmacopeia running. Register is **nobledark**: tragic choice rather than villainy, recorded vote counts, small technical heroism.

Published on AO3 as [work 89851861](https://archiveofourown.org/works/89851861).

## Layout

| Path | Holds | Rule |
|---|---|---|
| `manuscript/` | The chapters, as markdown | **Prose only.** Nothing generated ever lands here |
| `canon/` | Names, kinship, geography, settled decisions | `canon/pedigree.md` is authoritative for names and relations, `canon/setting-map.md` for places and what flows between them; both have a Graphviz companion |
| `notes/` | Directions still being weighed | **Not canon.** `chapter-plan.md` is the sequence; `spitball.md` is the discursive record with reasoning; `stripped-canon.md` inventories what commit `7330333` removed. Settled things graduate to `canon/` |
| `research/` | Briefs written to support the fiction | Primary documents under `research/sources/` |
| `tools/` | Build and check scripts | |
| `build/` | Generated HTML | Gitignored. Derived from `manuscript/`, never hand-edited |

## Shipping a chapter

```bash
make
```

Builds every chapter whose markdown changed. Then, to get one onto the clipboard:

```bash
make copy CH=01-continuity-test
```

Paste into the AO3 chapter editor **with the HTML tab selected**, not Rich Text.

**AO3 chapter numbers are not plan chapter numbers, and the gap is deliberate.** *Boil Water* is plan chapter 8 and AO3 chapter 7, because an unposted draft holds AO3 slot 6 for *Notifiable*. The mechanism, learned the hard way on 2026-08-20:

- **A draft chapter holds a position and shifts everything after it.** That is how you publish out of plan order — put a placeholder draft in each slot you are skipping, then post into the slot beyond them.
- **AO3 clamps a new chapter to the next real position.** Typing 8 when 7 is the highest existing slot silently gives you 7. The gap has to exist before you can post past it.
- **A draft at position 1 renumbers the whole work.** One sat there briefly and the published work read as starting at Chapter 2, with no Chapter 1. Check `/works/89851861/navigate` after any reposition.
- **Filenames are local.** The Archive never sees them, so renaming a chapter file — even a posted one — costs nothing upstream. Bare `make copy` lists the available slugs. `make clean` removes `build/`.

**Do not run pandoc by hand.** Two flags in the `Makefile` are load-bearing rather than cosmetic: one stops apostrophes being silently rewritten, the other stops the macOS pasteboard corrupting accented characters when the HTML is pasted into the browser. Both are explained in place at the top of the `Makefile`, because both have bitten once already.

Every build runs `tools/verify-fidelity.py`, which fails the build if the rendered text stops matching the source word-for-word, if a tag appears that AO3 will strip, or if any non-ASCII survives. It deliberately understands only the markdown constructs the manuscript actually uses, so a new one fails loudly instead of being normalised away in silence. It carries a `--self-test`.

## Conventions

- **Chapter files are `NN-slug.md`, where the slug is that chapter's AO3 title**, lowercased and hyphenated. No in-file heading — the filename carries the title.
- **Each chapter is titled in its POV character's own register.** Ch1 *ante finem mundi* is Collie's, a classics adjunct, so Latin. Ch2 *Continuity Test* is Lewis's, an electronics kid who never got the university, so engineering English. The rule keeps ch1's Latin hers rather than the book's.
- Paragraph references inside `canon/` carry a chapter — `ch2 ¶71`. A bare `¶N` means chapter one.
- Commit subjects are imperative and written in the chapter's own voice.

If a chapter file is renamed while an editor has it open, re-save from the editor before committing — otherwise the editor writes the old path back and the rename captures stale text.

## Known gaps

- **The working bible is not in the working tree, but it is in the history.** `canon/the-academy-brainstorm.md` — 310 lines, third edition, subtitled *"descent removed, project installed"* — was stripped in `7330333` along with 2,062 lines of research and the origin chat. Deliberate, not lost. Inventory and recovery paths in [`notes/stripped-canon.md`](notes/stripped-canon.md), which also flags a live contradiction between that bible's removal of descent and the current direction. **The 809th Vavilov Lecture** remains outside the repo entirely.
- **The AO3 work-level tags were rewritten on 2026-08-13** — 34 canonical tags, no longer chapter one's set. Still no relationship tag and no Diana, and `POV Multiple` survived a rewrite it now fits worse than ever, Ch3 being three in-world documents. The Fandoms field also carries `Climate Change - Fandom`, apparently an unintended disambiguation suffix.
