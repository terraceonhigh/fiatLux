# What the strip removed

**Commit `7330333`, "Strip branch to the two-file second canon", deleted 2,062 lines across 17 files** — deliberately. Its body reads: *"Keep manuscript/00-ante-finem-mundi.md and manuscript/01-the-repair-shop.md, drop everything else, preserve dir structure with .gitkeep."* This branch is `terrace/second-canon`; the strip was a reset to the prose, not an accident.

Nothing here is being restored. This file exists because **work done after the strip has begun duplicating and in one case possibly contradicting what was removed**, and because three files still carry dangling references to it.

Everything is recoverable: `git show 7330333^:<path>`.

---

## The inventory

| Path | Lines | What it was |
|---|---|---|
| `canon/the-academy-brainstorm.md` | 310 | **Working bible, third edition — "descent removed, project installed."** Sections: Register / Settled / Still open / The premise, corrected / Titles / Faculties into ministries / Chronology / The province / Reach and scale / Strategy: the first twenty-five years / Knowing things / Memory / Is it sustainable — and the project / Still to decide |
| `canon/pedigree.md` | 99 | Earlier pedigree, since rewritten from scratch |
| `research/four-beats.md` | 276 | **A four-beat spine**: the seed bank, the circuit, the instruments, the voyage. Contained its own `SUPERSEDED` markers on spine and chronology |
| `research/university-to-city-state.md` | 269 | — |
| `research/penicillin-city-state.md` | 248 | — |
| `research/the-two-lights.md` | 153 | **Register and thesis.** "There is no second descent" as *the correction that reorganizes everything*; graceful degradation as the register; *Fiat Lux* and the two lights; "The Vestals are prior art only" |
| `research/pragmatics.md` | 137 | Ceiling, dissolution, absorption |
| `research/absorbing-the-houses.md` | 133 | **The university takes the police station and the fraternities.** The rules all three arrived at / the failure mode predicted three times out of three / the renewal trap / the earliest indicator, and it is always a clerical convenience / where they split — the shape of the vote / the hole in the plan / what it costs, permanently |
| `research/sources/origin-chat-2026-08-03.md` | 124 | The claude.ai origin conversation |
| `manuscript/ao3-posting-kit.md` | 93 | Prior AO3 workflow |
| `TODO.md` | 91 | — |
| `manuscript/00-ante-finem-mundi.ao3.html` | 75 | Prior build output |
| `manuscript/to-ao3.py` | 54 | **Prior AO3 build script** |

---

## Three collisions with work done tonight

**1. `absorbing-the-houses.md` already covered chapter five's subject.** Its stated scope is *"the university takes the police station and the fraternities."* Tonight's `research/absorbing-armed-bands.md` was written from scratch without knowledge of it, and independently reached at least one of the same conclusions — the stripped file's *"the earliest indicator, and it is always a clerical convenience"* is the same finding as the new brief's Section VIII, that consolidation always arrives argued on grounds of convenience. Convergence is reassuring about correctness and means the new brief is partly redundant. **Worth diffing before ch5 is drafted.** The stripped file also has *"where they split — the shape of the vote,"* which the new brief does not cover and which matters for the minutes chapter.

**2. `the-two-lights.md` had already worked out the light motif.** It contains *"Fiat Lux — the two lights,"* *"The joke was not a joke,"* *"A light cannot be hidden,"* and *"The Vestals are prior art only — these people live and love and have children and die."* The celestial naming pattern presented as a find on 2026-08-10 — Coelia as sky and kept fire, Maia a Pleiad, Diana the moon, Medea granddaughter of Helios — is very likely rediscovery of documented ground, and the Vestal reading in `canon/pedigree.md`'s naming section was explicitly bounded there as *prior art only*.

**3. `four-beats.md` had a spine, and two of its beats are chapters we planned tonight.** Its four beats are the seed bank, **the circuit**, **the instruments**, and the voyage. "The instruments" is the Maia chapter; "the circuit" is what Lewis gets sent out on. Neither was written tonight with any knowledge of the prior treatment.

---

## Settled: the second canon governs

Raised as a possible contradiction and **resolved by the author on 2026-08-10.** The stripped bible's third edition is subtitled *"descent removed, project installed"* and `the-two-lights.md` opens with *"there is no second descent"* as the correction that reorganizes everything — while the current direction leans the other way, treating descent as load-bearing through Roman clientela, Collie as Patronus, the marriage plot, and contraception as fertility policy.

There is no conflict to manage. **`main` got riddled with overwrought worldbuild; this branch is intentionally breezy and agile.** The strip was the point, the second canon governs, and nothing above is a constraint on it.

Read the inventory as a source of *optional* prior art — `absorbing-the-houses.md`'s shape-of-the-vote material is worth a look before the minutes chapter — not as a standard to reconcile against.

## The merge, planned for 2026-08-11

Tag `main`'s current commit as reference first, then merge `terrace/second-canon` into `main`. The tag is what makes the stripped material findable by name rather than by remembering a commit hash — after which everything in the inventory above is reachable from the tag instead of from `7330333^`.

---

## Residue to clean

Three files referenced the stripped documents as though they were present. Corrected on 2026-08-10 to say they were stripped and name the recovery path:

- `canon/pedigree.md` line 3 — pointed at `the-academy-brainstorm.md` as the setting reference
- `research/prepper-beekeeping.md` line 5 — named `research/pragmatics.md` as its companion in register
- `README.md` known gaps — described the canon documents as having *"originated in a claude.ai chat and are not in this repo,"* which was materially incomplete: the bible was in the repo, at `canon/the-academy-brainstorm.md`, and the origin chat was too, at `research/sources/origin-chat-2026-08-03.md`
