# Open items

*Written 2026-08-04, at the end of a long working session, on the assumption that whoever reads this next has none of that conversation's context. Everything needed to act should be here.*

---

## 1. ~~Rename Nanaya~~ — DONE, 7 August 2026

**Collie's daughter is now Medea, called Maddy.** All seven occurrences in `00-ante-finem-mundi.md` renamed to *Maddy*, and the `.ao3.html` regenerated.

**Why Medea.** Μήδεια is from *mēdomai*, to plan or devise — *the one who plans* — and that *med-* root is the root of *medicine* (*medeor*, to heal). The planner and the physician are etymologically one word, which is a good name for the daughter of a classicist in a polity whose founding competence is a clinic and whose purpose is minimising pain. She is also a *pharmakis*, a drug-woman, and *pharmakon* means the cure and the poison without distinguishing — which is what the chlor-alkali plant does. And she is the granddaughter of Helios, who escapes at the end of Euripides in the chariot of the Sun, in a book called *Fiat Lux*. Collie is a classicist and would know all of that.

The infanticide is deliberate, not an oversight. Euripides gives Medea the argument and makes you follow the reasoning — a wronged woman who *calculates*. That is the register: the person who did the terrible thing had reasons and could defend them in the minutes.

**Why Maddy.** It reproduces the Collie pattern exactly — *Coelia 'Collie' Swartz*, *Medea 'Maddy' Swartz* — a grand name filed down to something you can shout across a park, which is characterization on its own: Collie did to her daughter what someone did to her. It also fixes the problem that killed *Nanaya*: two syllables, front-stressed, flat vowel, no *-ia* ending, so nothing left to confuse with *Nadia*. Mild residual: *Maddy* and *Maia* are both M-initial two-syllable names sharing scenes, judged acceptable since one is a child and one is a mother.

### Still to do for the rename

- **The full name has never appeared on the page.** Every existing mention is in child POV, so they are all *Maddy* and *Medea* is unspent. Introduce it once, in the established form — `Coelia 'Collie' Swartz (please, just Collie is fine)` is the model — whenever she gets a section of her own.
- **Her surname is unstated.** Nadia has Elbakyan, Lewis presumably has Latimer. *Medea Swartz* is the obvious default if she takes Collie's.
- ~~**AO3 still says Nanaya.**~~ **Done, 7 August 2026, on the author's explicit instruction.** All seven occurrences replaced in the live chapter body and saved. Verified after: 0 `Nanaya`, 7 `Maddy`, and the rating, chapter count and chapter title all still intact. Repo and AO3 are content-identical — SHA-256 match over all 32 paragraphs. See `manuscript/ao3-posting-kit.md` for the comparison method, which is paragraph-level because AO3 rewrites the raw HTML on save.

### Who she is, for reference

**Collie's daughter.** Second generation. She appears as a child in chapter one, playing with Nadia and Lewis in the household that forms around Collie's third-floor flat.

The household, for reference:

| Adult | Child | Notes |
|---|---|---|
| **Coelia 'Collie' Swartz** | **Medea 'Maddy'** | Classicist. Adjunct → Senior Lecturer → insists on *Doctor*. The line runs through her |
| **Maia** | **Lewis** | Astronomer, away at the mountain observatory. Lewis is lonely because of it |
| **Nona** | **Nadia Elbakyan** | Knits, charity work, drives the kids. Nadia has the POV in the child sections |

## 2. Chapter one is posted — the repo is canonical

Posted 4 August 2026, public, at the URL above. Chapter two is repo-only; AO3 shows `1/?`.

**Write in the repo.** AO3 is a publishing target, not a working copy, because **AO3 keeps no version history** — an edit there overwrites permanently and the repo is the only place a previous draft survives. Chapter one was edited on AO3 between 5 and 7 August and pulled back on the 7th; the two are byte-identical as of that sync. If it happens again, see `manuscript/ao3-posting-kit.md` for the direction to sync in and why pasting the rendered page back would flatten every line of dialogue.

To render a chapter for posting: `python3 manuscript/to-ao3.py manuscript/<chapter>.md`

---

## 3. Chapter two — the direction, decided 9 August 2026

**A palace drama in the history department.** The university absorbs the failing municipal police force and the campus fraternities into a single security force. Collie witnesses and participates. It is set in §VI's decade two or three — the accords era, well before Phase 1's Emergency — so **nobody in the room knows they are founding anything**, which is the zone `university-to-city-state.md` calls the best fiction in the setting.

**Who proposes it.** A **Latin Americanist** whose expertise is partly the history of violence in universities. Not from the region — the expertise is scholarly and citable, not ancestral. Seeing what is coming, they make the difficult decision to do the unthinkable thing *responsibly*, as damage control, on the grounds that the police will rent themselves out and the houses will arm themselves regardless, and the only real question is whether it happens under a charter with rules or in the dark. That argument is unanswerable and is how these things are actually built. §0: no villain, someone who can defend it in the minutes.

The sharpest thing about them: their field's founding constitutional principle is **autonomía universitaria** — police may *not* enter campus — out of the Córdoba Reform of 1918, which also won *co-gobierno*. They are proposing the precise inversion of the tradition their scholarship rests on, and can name the year it went wrong in half a dozen countries.

**Why it matters structurally.** This plants **§VI Phase 5** — *first serious coup attempt, from Facilities or the militia; the absorbed garrison does not believe a committee should command it.* Chapter two is that garrison's founding charter, written by people who will all be dead before it is refused.

**Collie's position is load-bearing.** She is a classicist, not a historian, so she needs a reason to be in the room — either her unit was merged into History by austerity (she has personally been through the operation they are about to perform, which makes her the precedent sitting there), or she is the precedent-supplier, since watch and ward and the proctors are in her field. Either way: **as an adjunct she has no vote.** She can speak, be cited, and not be counted. §I says division counts; she is in the room and not in the division. Her arc runs adjunct → Senior Lecturer → Doctor, so **the moment she gains a vote is a datable event in the manuscript.** The founding vote is Phase 2, a decade or more later, so nothing here forecloses §XIII.4.

### Still to decide for chapter two

- **Which charter model wins the vote.** Three coherent, incompatible positions are set out in `research/absorbing-the-houses.md` — charter nothing, charter one house at a time, or charter all twelve for status only. The losing sides are not cowards, which is what §0 requires.
- **Frats versus Athletics.** §VI Phase 2 already says *Athletics becomes the militia*. Frats-as-guards competes with it. Three reconciliations, none chosen: frats replace Athletics (a canon amendment), frats and Athletics as rivals (two factions at ground level, thirty years early), or cops-and-frats as the small pre-founding force that the Winters' mass militia later envelops.
- **Whether the vote to take the police station is the founding vote.** §VI names two candidates already built — the water quality contract and the vote to absorb the charity. This is a stronger candidate than either, because it is the first that transfers a *power* rather than a service. The question is how much weight decade three should carry.
- **What the force is called.** It starts as a committee, so it will carry a committee's name, and whatever it is called in decade three is what it is still called in Phase 5 — which lands the garrison's objection on the sign above its own door.
- **The existing 71 words of chapter two** are Lewis at the repair shop. The vignette form means these can coexist in one chapter or be displaced; it is the only prose that would move.

### Shelved, with the reason

**The salmon-run beat** — a fisheries expert with jurisdiction over run information, and a vote to eat the escapement against a four-year deferred harm. Shelved 9 August 2026 because it is **structurally the seed bank again**: escapement is a corpus, harvest is income, and *don't eat the seed* is a beat this setting has already got. Possibly revivable much later in the story, where the co-sovereignty negotiation (§XIII.3) needs a scene rather than a gap. The research is not written down; the anchors were Hells Gate 1913–14, the Babine barricades 1904–06, *Sparrow*, *Boldt*, and W̱SÁNEĆ reef-net sites as named heritable property.

---

## 4. Still open in canon

From `canon/the-academy-brainstorm.md` §II, §XIII — listed here only as a pointer, not restated:

- The matriculated-to-hinterland ratio (§II.3; 1:10 is the standing recommendation)
- The two-tier credential (§II.7)
- The gate on the first night — number turned away, if any (§XIII.1)
- **Indigenous co-sovereignty (§XIII.3) — the largest structural hole**, a gap across §VI–§IX rather than a missing paragraph
- Whether the restoration project succeeds (§XIII.2; may never need answering)
- Whether the founding vote's dissenter is one of the existing women (§XIII.4)

---

## Orientation, if you are new to this repo

- `canon/` — authoritative. `the-academy-brainstorm.md` is the working bible, third edition; read §0 and §XII first. `pedigree.md` has the chapter one cast, their kin, and the placeholder tokens for every name still unsettled.
- `research/` — six briefs behind it: the register and narrative frame (`the-two-lights.md`), the technology and state-collapse machinery (`pragmatics.md`), the pharmacopeia (`penicillin-city-state.md`), institutional conversion (`university-to-city-state.md`), materiel for four specific scenes (`four-beats.md`, which carries a status header explaining what in it is no longer canon), and the police-and-fraternity absorption behind chapter two (`absorbing-the-houses.md`, produced by a blind three-lens panel — the header explains why that matters).
- `manuscript/` — the prose. Chapter one is done and posted. `to-ao3.py` renders a chapter for the AO3 editor.
- `research/sources/` — a transcript of the conversation the setting started in. **Do not edit it**; it is evidence, it carries an archival header, and most of the names in it are dead. Anything it says is superseded by `canon/`.

The author's role for the assistant here has been **researcher, not writer** — supply facts, constraints, failure modes and historical precedent; catch errors of fact and grammar on request; do not draft narrative prose unless asked.
