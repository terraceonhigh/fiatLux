# External model critique, 2026-08-31

Six frontier models read the ten written chapters (16,048 words) cold and ranked
the author's biggest areas for improvement. Claude-written digest. Terrace has
made no calls on any of this yet — everything below is model opinion plus
verification, not canon and not a decision.

## Method

- Payload: the ten non-empty `manuscript/*.md` in reading order, FILE headers only.
  No `canon/`, no `notes/`. Models saw prose, not lore.
- Run via `opencode run --pure --dir <scratchpad> -m <model> -f <payload>`.
  `--pure` matters: the first run picked up the `humanizer` skill and its output
  ranked "conspicuous indirect phrasing" #1, mirroring that skill's checklist.
  Re-run without it demoted the same finding to #3 and reframed it as POV control.
  **Any future run must use `--pure` or the review is contaminated.**
- Models: `gpt-5.6-terra` (2 runs), `gemini-3.1-pro-preview`, `claude-sonnet-5`,
  `deepseek-v4-flash-0731`, `kimi-k3`, `minimax-m3`, `grok-4.6`.
- Every quoted citation was grepped against the manuscript. All verified except
  two noted under Discard.

Two tooling facts, recorded 2026-08-31, that apply to both rounds and will bite
any future run:

- **`opencode run -f` truncates the attachment at 50KB.** The model gets the head
  of the payload and must tool-call to read the rest. In the comprehension round
  Sonnet 5 named the cut exactly ("truncated at 50KB ... through line 1187") and
  Grok reported it; Kimi and DeepSeek read past it without comment. No evidence it
  changes answers, but every run spends extra tool calls, and the payload (90KB)
  is well over the limit in both rounds.
- **Local models behind llama-swap must be called directly** on the
  OpenAI-compatible endpoint, not through `opencode run`. The agentic loop plus
  the truncated attachment stalls them. `qwen3.6:35b` returned nothing through
  opencode and answered on a direct call: 119s for 22,698 prompt tokens. Its
  output file carries no opencode header, which is how to tell a direct call from
  a routed one in the scratchpad.

## Frame

Two calibrations that should govern how much weight each finding gets.

**1. Every complaint is about allocation, not capability.** The six asked for
subtraction: ration the inventory, settle the register, delete the captions, cut
the tics, fix five POV hops. None said a character fails to build, nothing is at
stake, or the prose cannot do the work. The recurring charge is that the voice is
*too* present. That is a surplus problem.

**2. The models reviewed an unassembled draft.** Six chapter files are empty and
`chapter-plan.md` runs to Pulp. The "no spine / no momentum" finding (Tier 2,
below) is partly a true diagnosis and partly a description of a book roughly a
third written. Do not accept it as a verdict on structure until the slots fill.

## Tier 1 — replicated 5-6 of 6

### Inventory is doing the work of scenes  [6/6, unanimous]
The packing list is a default unit. Objects accumulate and nothing happens to them.
- `01-continuity-test.md:9` — the backpack manifest (toolkit, gloves, hardhat,
  tourniquet, three vials)
- `01-continuity-test.md:147` — thirty kegs / five sides / twenty crates / seven bags
- `00-ante-finem-mundi.md:5` — the bin installed two years ago and the paper-spoon
  procurement debate, mid-scene
- `11-mulberry.md:3-27` — the washer #17 teardown (panels, wire colours, vinegar,
  alcohol, extension cords)
- `09-ground.md:39` — tools, t-shirts, trowel, string in one paragraph
Grok: "The reader is not in a novel. They are walking a warehouse with you."
Note the distinction Grok drew and Sonnet 5 seconded: a loaf, a stump, a cuff
reading 170/60 land. A convoy manifest does not. The test is whether the object
is doing something to a person.

### One authorial wit across all mouths  [5/6]
Registers taped together inside single characters, and one arch voice across
characters of different class and age.
- `09-ground.md:131` — "By Jove, Alex! ... just Collie is fine" (Collie, Regency-inflected)
- `03-formulary.md:31` — "I accept the compliment. So, how may I be of service?" (Rosa)
- `06-isolation.md:131` vs `10-wild-oats.md:43` — Bréal runs "Till Valhalla!" and
  "Oorah!" and then "Wallahi bro, this ain't the navy. Spit." Grok: three registers,
  not a person.
- `10-wild-oats.md:65,181` — "jizzing grass all over town" / "frolic pure-of-heart style"
Sonnet 5: the book contains "at least three different centuries of English at once,
and not in a way that seems to be commenting on anything."
Counter-evidence worth keeping: Kimi held that the *dialogue* register is controlled
and distinct (Rosa's formality, Diana's "'sgot peppermint in it", Bréal's bluster)
and that the unsettled voice is the **narration between** speeches. That is a
narrower and more actionable version of the same finding.

## Tier 2 — replicated 3-4 of 6

### You caption your own book  [4/6]
Meaning arrives as gloss rather than consequence. Terra and Grok independently
converged on the same passage without seeing each other.
- `07-boil-water.md:141` — the Medea speech. Both: the scene has already done the
  adoption; the myth restamps it. Grok adds `:153` "you are mine now" and the name
  as a third stamp on the same beat.
- `00-ante-finem-mundi.md:63-71` — the clinic shakedown. Grok: "Collie does not
  exercise power. She announces she has it."
- `04-off-label-part-i.md` — "she trained for this" / "if you panic everybody panics"
  told alongside vitals that already show it.
- `10-wild-oats.md:353` — "Nadia lied." Kimi: the reader already knew; the tag
  converts a taut beat into a wink.
Kimi's line is the one to keep: **"Your silences are the best thing you have."**

### Tics repeated past visibility  [4/6] — counts verified exact
- `Thunk.` — 4x in `10-wild-oats.md`
- "just Collie is fine" — 4x, `00-ante-finem-mundi.md:1` and `09-ground.md:131` et al
- "We make do" — 3x across `03-formulary.md`, `06-isolation.md`, `09-ground.md`
- clocks and skies that "said" the time — 5x, incl. `01-continuity-test.md:59,101`,
  `06-isolation.md`
- Grok's structural tic, and the only finding at whole-book scale: **four chapters
  end on a short declarative button** — `00:71` "And then it was a handshake",
  `01:75` "She let him in", `09:223` "It was not just one", `10:373` "She had the watch".
  "You do not trust an ending unless you stamp it."

### Scenes do not hand off / no forward momentum  [4/6 — but see Frame #2]
DeepSeek ranked this #1, Grok #3.
- DeepSeek: the `---` break is doing all the transition work, each scene resets to
  zero. "No spine, just a rack of beautiful birds."
- Grok: "the book reads like a chronicle of a better novel. We get the minutes.
  We do not get the hour." Cites `00-ante-finem-mundi.md:17` (a paragraph of
  summarized childhood: "That is not a child's afternoon. It is a dossier").
- `10-wild-oats.md:377` — "The trip ended up taking four and a half days."
  **Three models independently (Terra, DeepSeek, Grok) called this the chapter
  refusing its own aftermath.** This is the line restored from AO3 on 2026-08-31.
Discount per Frame #2, but the four-and-a-half-days line does not get the
incomplete-draft excuse. That one is local.

### Reader kept outside the characters  [3/6]
Interiority displaced onto physical business until the business becomes the screen.
- `07-boil-water.md:157` "did not look at her thirdborn child", `:171` the yolk
  "like a thin moat" — Terra: choreography instead of either woman's shock
- `09-ground.md:81` "letting the skin slide off his fingertips" — Sonnet 5: a
  consequential decision (leaving Lewis, moving to the observatory) buried under
  gesture after gesture
Sonnet 5's split is the useful form: ch7 ironing **earns** it because dialogue
carries the emotion and the ironing is counterpoint. ch9 does not. Same device,
opposite results.

### Grammar and tense read as accident, not voice  [3/6]
- `11-mulberry.md:3` — "The load in the other machines were pure white"
- `00-ante-finem-mundi.md:3` — "if the school had so much as bothered to inspect"
- `00-ante-finem-mundi.md:23` — Kimi: subject mutates mid-sentence, "which" attaches
  to a noun that cannot sob. The most tangled sentence in the draft.
- `01-continuity-test.md` — "her beau, who rode the truck behind him and Egghead":
  "him" has no clean antecedent, the beau is already the subject of "rode".

**Three items the models filed here that do NOT survive checking (2026-08-31):**
- `09-ground.md:91` — "But, won't it better, if, he is young, and, if we don't,
  Collie would—" is *dialogue*, Maia halting and getting cut off in a scene about
  giving up her son. The line before it (`:85` "*But—*") is cut off the same way.
  Deliberate rendering of distress. Terra filed it as a grammar slip. Misread.
- `00-ante-finem-mundi.md:17-19` — the present tense holds across the entire
  section without a single lapse, and the section is set off by `---`. That is a
  device, not a slip (a child has no past tense for their own childhood). Gemini's
  real complaint was that it is *unmarked*, which is a legibility question.
- `01-continuity-test.md:17` — "The trucks will be going elsewhere next month"
  follows "Which the manager said now cost two vials of poppy." Free indirect
  discourse, the manager's tense leaking into narration, and the "Which..."
  fragment before it is the same device. Defensible technique.

The pattern across all three: the models cannot separate a deliberate effect from
an error, and default to calling it an error. Kimi named this honestly — the
strangeness "makes intentional strangeness difficult to distinguish from accidental
awkwardness." That is a legibility note, not a correctness note, and it is the
version worth keeping.

## Tier 3 — single source, verified, worth acting on anyway

### POV head-hops inside otherwise locked close-third  [Kimi only]
Kimi gave five. Checked against the text on 2026-08-31: three hold, one is a
judgement call, one is Kimi misreading correct POV discipline as vagueness.

**Hold:**
- `03-formulary.md:51` — "Rosa turned to face the wall while she did so. Diana
  rolled her eyes." Chapter is Rosa-locked (`:3` "Egghead flipped the note",
  `:5` "her office", `:9` "Rusina had her kneel"). Rosa is facing the wall and
  cannot see the eye-roll.
- ~~`10-wild-oats.md:221`~~ — WITHDRAWN 2026-08-31. Mechanically a hop, but it
  is the chapter's only time-of-day marker, the halo pays off at `:303` ("You
  really are an angel", same speaker), and the narration enters that woman twice
  (`:221`, `:307`) both times to register her read of Maddy, both feeding her
  letter at `:325`. A pattern, not a lapse. See `notes/revision-worklist.md`.
- `11-mulberry.md:73` — "Collie could be seen sinking most of herself into the
  river." Passive positing an observer the ensemble camera does not have. Also a
  comma splice: "...massaging the liquid into Nona's hair, Collie could be seen...".
  Worse than Kimi said. A period and an active verb fixes both at once.

**Judgement call:**
- `10-wild-oats.md:307` — "And so humble too, the woman thought." Technically
  outside the sibling unit, but the irony is doing work — the reader knows Maddy
  is performing modesty and the host is buying it. Defensible as a deliberate
  one-line dip. Keep or cut on whether the joke is worth the hop.

**Kimi is wrong:**
- `09-ground.md:181` — "Alex did something with his right hand". The section from
  `:119` is Collie-POV (`:121` "Collie's room ... would remind her of her duties",
  `:177` "Alex looked at Collie's face"). So this is Collie watching a gesture she
  does not parse. That is correct limited perception, not authorial vagueness.

Kimi also noted `04-off-label-part-i.md` is airtight on POV, which is why the real
lapses read as error rather than omniscience.

### Italics-no-quotes dialogue fails at three or more speakers  [Gemini + Sonnet 5]
Both hit it independently and neither was in the first round.
The convention works for two people. With three you have left yourself no other
tool for attribution.
- `10-wild-oats.md:43-181` — the diner/cab scenes
- `11-mulberry.md:37-71` — three women at the river. Sonnet 5 named "Collie flanked"
  and "Nona had picked a side" as doing the job clearer staging should do.
Gemini adds that the muted, dreamlike distance of unquoted italics actively fights
the trauma scene in `04-off-label-part-i.md`.

### Worldbuilding as a wink at the reader  [DeepSeek]
- `00-ante-finem-mundi.md:1` — the $25 poke bowl, the Mohsin Hamid joke, the
  one-dollar coffee, the gas price beginning with a two. DeepSeek: "a joke told
  *at* the reader ... It's not Attis's head, it's the author's voice in a hat."
- `00-ante-finem-mundi.md:17` — Nadia's child-voice section as a character
  directory: "the reader experiences being lectured by a mascot." Adult
  worldbuilding in kid syntax ("where all the red buses live just outside").

## What to protect — near-unanimous

**Five of six named the same passage: Attis Cassidy's death, `04-off-label-part-i.md`.**
Not the same quality — the same passage.

The praised mechanism is the procedural-ritual mode: competent hands doing work
while the emotion happens off to the side. `04`'s memory test collapsing from
"Bundle, Book, Banana" to "what's a banana?" to `:125` "sword, tree, pillar" to
"umm, sword, apple, ...paper?", then `:173` the flat "pronounced Mr Attis Cassidy
dead at 1148 hours".

Also named: Diana's stump exam and cooling soup (`03`), the water-failure radio
traffic (`06`), Collie rinsing already-clean hands (`07`), Lewis and his father
and the controller (`00:23`), the river laundry (`11`).

**The reconciliation, and the single most useful note in the six reviews
(Sonnet 5):** the flat clinical register works in `04` *because flat affect is the
content* — a mind refusing to feel anything yet. Spent on laundry and soup, it has
no charge left when it is needed. The note is therefore not *less procedure*. It is
procedure only where the flatness means something.

Terra and Gemini read the register itself as the defect. Sonnet 5, Kimi and Grok
read it as the best asset misallocated. Prefer the second: the first has to call
`04` an accident.

Minimax dissented on what to protect and named **the social architecture** instead
— relationships conveyed entirely through enacted behaviour, who defers to whom
and in what register, Bréal's authority visible in what he signs. It reads
"please, just Collie is fine" as a motif doing real work, where Grok and DeepSeek
read the same line as a tic run into the ground. Unresolved.

## Disputed

`07-boil-water.md:59,91` — the call-and-response grief beats ("Neither could I",
"It is unfair. / Yes, it is."). Grok alone: agreement is not conflict, so the
exchange states the theme instead of dramatizing it, and the ironing was already
carrying it. Terra and Sonnet 5 both named this scene among the draft's best.
One model against models that liked what it disliked is the profile of a taste
call, not a defect.

## Discard

- **Sonnet 5 asserts Maddy is Collie's biological daughter.** False, and against a
  hard constraint in `canon/pedigree.md` — Collie never has biological children.
  Maddy is her niece, Alice Swartz's daughter. The finding underneath (the
  parentage reveal rests on a thin thread four chapters back, `00:17` and
  "Nona visited, quite often") survives; the reasoning does not. Worth knowing a
  careful reader with the whole text in one sitting drew exactly the wrong conclusion.
- **Grok's "a wok that was labeled a wok"** is a paraphrase. The line is
  `09-ground.md:117` "The pot was labeled a wok". Point stands, quote is loose.
- **Minimax says the watch does not recur.** Its actual claim was narrower — the
  brand and the engraved motto do not recur (`04-off-label-part-i.md:173`). The
  watch itself does, `10-wild-oats.md:373`.

## Open

Whether the chapters accumulate into a novel rather than a collection. The prose
demonstrably reaches literary-fiction register in `04`; six independent readers
found it. What is unproven is the spine, and that question cannot be settled
until the empty chapter files fill. Nothing in these reviews indicates it will
go badly.

Raw reviews: session scratchpad, `review-*.txt` (not in repo).

# Reading-comprehension round, 2026-08-31

Same payload as the prose round (`fiatlux-prose.md`, ten chapters, 16,048 words),
same `opencode run --pure`, different task: three questions about buried meaning,
with the prompt stating "this is a reading-comprehension test, not a critique"
and instructing plainly, "If the text does not settle something, say so plainly
rather than guessing confidently" (`prompt-comprehension.txt:3`). That instruction
matters to the scoring below — a decline is compliance, a confident wrong answer
is not. Claude-written digest. Terrace has made no calls on any of this.

## Roster

Eight models attempted, eight answered. `gpt-5.6-terra`, `claude-sonnet-5`,
`kimi-k3`, `grok-4.6`, `deepseek-v4-flash-0731`, `minimax-m3` answered in the
first batch. `gemini-3.1-pro-preview` produced nothing in that batch and answered
on the scripted retry at about 19:00, clean, no timeout marker. Three later
gemini attempts produced zero-byte files, including a 5-token ping with no
payload at all, so the flakiness is provider-side and not a function of the
questions. The batch output cannot be re-checked: the retry overwrote the file.
`qwen3.6:35b` is the local model, called direct per the Method note above.

## The three questions

1. `11-mulberry.md` — why does Nona radio for liver or blood sausage?
2. `04-off-label-part-i.md` — why "what's a banana?"
3. `10-wild-oats.md:325-345` — what is in the second letter, the one for Maddy's
   mother and father, and what is the woman proposing?

## Q1 — the liver  [2 hit / 1 partial / 5 miss of 8]

The chain the text supports: at the river Nona finds the underwear with *MADDY*
sewn on the tailbone, bags it, and notes to soak it overnight on its own
(`11-mulberry.md:69`). Hours later she radios Lewis for liver or blood sausage
(`:119`), the two most iron-dense things a butcher sells. Reading: iron for a girl
who has started menstruating, phrased as a grocery order because it travels over
an open channel with Vavasseur and everyone else listening. **This reading is
nowhere stated in the text.** Record it as the strongest available inference, not
as fact. The two scenes are juxtaposed and no character connects them.

- **Kimi — hit**, the whole chain including the open-radio reason, and it flagged
  its own inference ("the chapter only juxtaposes the two scenes and lets you
  connect them").
- **Gemini — hit**, same chain, same open-radio reason, stated flat as fact with
  no caveat, against the prompt's instruction.
- **DeepSeek — partial.** Iron and B12, iron-deficiency anemia, Nona-as-fortifier
  (cites the chalk loaf in `02`). Never reaches Maddy or the underwear.
- **Terra — miss, confabulated.** Attributes it to "Collie's evident weight loss."
  Grepped 2026-08-31: **no weight loss, thinness or gauntness appears anywhere in
  `manuscript/`.** Invented whole.
- **Minimax — miss, confabulated.** Builds a detailed case that Nona is pregnant
  or postpartum. Its three anchors are all real — the dye and the dresses "we'll
  want for Nadia and Maddy pretty soon" (`11-mulberry.md:85,87`) and "I know I
  won't remember it" (`:101`) — and it reads the last as pregnancy brain. Wrong,
  but assembled from the page. An available misreading, not a stupid one.
- **Sonnet 5 — miss, declined.** Reads it as a mundane dietitian's grocery order
  and a comedy of channel mismatch, the water emergency of `06` versus a shopping
  list. Names the iron inference and explicitly refuses it as unsupported.
- **Grok — miss, declined.** "Whether someone at home is anemic, pregnant, or she
  is only restocking is not settled."
- **Qwen — miss, declined.** Generic nutrient density and offal efficiency.

Two things worth keeping. First, both hits supplied a detail the page does not
contain: Kimi calls the underwear "stained," Gemini "soiled." `:69` says only that
it went in her bag with a note to soak it separately overnight. The real signal is
the separate treatment, and both readers upgraded it to a stain to make the chain
say itself. Second, the misses split by kind — three declined and two guessed. The
declines are the prompt being obeyed. The confabulations are the failure.

## Q2 — the banana  [7 of 8]

Unanimous among the seven frontier models: bananas need a supply chain that no
longer exists, a fifteen-year-old farm boy has no referent, so the old-world
recall triad fails and Rosa substitutes locally real words at
`04-off-label-part-i.md:125` ("sword, tree, pillar"), which the reader then watches
fail at `:153` ("umm, sword, apple, ...paper?").

Two models added craft readings nobody asked for and neither had seen the other:

- **Kimi** — because the reader watched the substitute list get chosen, the later
  recall lands as a clean measurable failure. "It's a small joke that turns out to
  be the hinge of the diagnosis."
- **Grok** — "shows her protocol failing in a small way before it fails in the
  large one."

**Qwen — miss, and the only one.** Reads the confusion as a clinical symptom of
Attis's head trauma rather than as the world showing through, and reads the pivot
as bedside composure. It gets the scene and loses the setting.

## Q3 — the second letter  [8 of 8 on shape]

Every model got the broad shape: a proposal, and a family alliance. The addressees
are textual and needed no inference — Maddy names them on the page (`:331`, "my
mother's name is Collie, and father is, uhh, Alex").

The split is on flavour, and it is roughly even:

- **Betrothal first:** Terra ("a marriage proposal or preliminary request for
  Maddy's hand"), Kimi ("a marriage or betrothal offer"), Gemini ("a courtship or
  arranged marriage between her son and Maddy"), Qwen.
- **Sponsorship or wardship first, match as undertone:** DeepSeek ("family-alliance
  proposal with a betrothal/match undertone"), Minimax ("ward or protégé ... also
  leaves open that this doubles as a long-game match-making overture"), Grok
  ("sponsor him ... i.e. patronage, and likely a match with Maddy").
- **Refused to pick:** Sonnet 5 names both and says the text stops short, "it could
  alternatively be a more modest ask (formal guardianship/mentorship, not
  marriage)."

Minimax alone guesses the intended girl is Nadia rather than Maddy. Qwen's answer
is garbled in a way the tally hides: it says "the woman is proposing a serious
romantic partnership or marriage" without ever naming the parties, and half reads
as the woman proposing on her own behalf.

Three models reached the content through the family's **reaction** rather than
through the letter, which is never shown. Kimi and Grok used the reaction as the
primary inference path, Terra as confirmation. The evidence they used is the same
three beats: Nadia lying to keep everyone in one room (`10-wild-oats.md:353`),
Lewis loading the family shotgun and sleeping against the door (`:361`), Nadia
taking the watch (`:373`).

**Open.** The text does not settle whether the proposal is marriage or
fostering/patronage. Both readings are defensible from the page, and eight readers
splitting down the middle is itself the evidence that the page does not decide it.

## What the round shows

**Buried meaning survived in proportion to whether a character reacts to it on the
page.** The three questions happen to form a clean gradient:

- **Reacted to on the page, cued locally** — the envelope. The whole household
  reacts within twenty lines of the letter being sealed. **8 of 8**, weakest model
  included.
- **Needs a premise carried across chapters, then reacted to** — the banana. Rosa
  visibly recalibrates in the same breath. **7 of 8**; only the small local model
  failed.
- **Needs the premise and outside domain knowledge, halves in different scenes, no
  character connecting them** — the liver. **2 of 8.**

## Cross-reference to the prose round

This localises the "you withhold basic scene information" complaint, which appears
above in Tier 2 as the momentum and scene-handoff item and in the first Terra run.
The comprehension round is the only hard evidence in either round for that charge,
and it narrows it hard: the problem is not general withholding. Two of the three
buried things came through at 7 of 8 or better. It is specifically the liver, where
the two halves sit in different scenes and nobody on the page joins them.

The failure mode is also not what the prose round assumed. Readers who miss it do
not report confusion. Two of eight reconstructed a confident wrong answer instead —
Terra's invented weight loss, Minimax's pregnancy — and Minimax's is built entirely
from real details. A gap that produces plausible wrong readings is a different
problem from a gap that produces a puzzled reader, and it is the one that is
actually here.

Raw answers: session scratchpad, `comp-*.txt` and `prompt-comprehension.txt` (not
in repo).
