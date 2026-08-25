# Pedigree

*Kin across the whole written cast. **Scope corrected 2026-08-21** — the title and this line said "chapters one and two" long after the file had grown sections for chapter four, *Formulary*, *Boil Water* and the *Skywave* apprentice. Authoritative for names and relations. The setting reference was `canon/the-academy-brainstorm.md`, stripped from the branch in `7330333` and recoverable with `git show 7330333^:canon/the-academy-brainstorm.md` — see [`../notes/stripped-canon.md`](../notes/stripped-canon.md).*

**The kin graph itself is still a chapter-one-and-two object**, because no chapter since has added a blood or marriage tie — everything later adds household, not descent. *Ground* is the clearest case: a whole chapter inside the Tsien marriage that changes no edge on the chart.

The graph itself lives in [`pedigree.dot`](pedigree.dot) — open it with a Graphviz preview (e.g. the VS Code Graphviz extensions). Everything below still applies to reading it.

Paragraph references now carry a chapter — **ch1 ¶29**, **ch2 ¶71**. A bare `¶N` anywhere in this file means chapter one.

## How to read it

| Edge | Means |
|---|---|
| **Solid arrow** | Parentage **stated in the prose** |
| **Dotted arrow** | Parentage that must be true, but is **never written on the page** |
| **Solid line, no arrow** | A marriage the prose states |
| **Dotted line, no arrow** | A pairing the prose implies and never states |
| **Bold line, no arrow** | A romance the prose states outright, short of marriage — currently only Lewis and Diana |

The groupings carry the rest: the three women shared a flat, the three children grew up together, and the men are sorted by whether they made it onto the page.

The three women shared a flat before any of the children. That tie is **historical, not current** — by chapter one they are three households, and Maia's moving into Collie's in the last paragraph is a *re*convergence. **How roommate they were is deliberately unpinned** and the chart does not resolve it.

Chapter two adds a **fourth household that was never in the flat** — Diana's, outside the town, with a mother in it. It is the first kin group in the book that does not descend from the three women, and Lewis is the only edge connecting it to the rest.

## The relation the line runs through

**Settled 2026-08-20 by *Boil Water*, and it reverses what this file used to say.** **Collie is not Maddy's biological mother.** Maddy's mother is **Alice Richards**, dead before ch2 — a university teacher who **wrote the water standards** in the time she was not teaching, killed in a bad season by a treatable illness and a bad vial. Collie's account: *"She was the smarter one, if you'll believe me."*

**Which means ch1 ¶17 needed no reconciling and this file mis-inferred it.** *"Maddy's mom is someone who is very smart, and works at the university"* and *"Auntie Collie is a nice woman"* are **two different women in one child's POV** — Nadia naming Maddy's actual mother, and calling Collie an aunt because Collie is not hers. The earlier reading treated the pair as evidence the reader had to assemble into Collie-as-mother. It never was.

**Alice Richards, what the prose gives her:**

- University, and she taught. Alive at ch1, dead before ch2.
- **The water standards are hers.** *Isolation* is a water emergency and *Boil Water* is a public-health advisory, and the woman who wrote the valley's water document is dead before either.
- Died on injectable medicine, syringes steam-sterilised at home by Maddy at about ten, with peppermint oil for her nose. **Cause never identified** — *"we lost a lot of good people that season."*
- **The vial killed her.** *"They couldn't find a better vial for anyone in the city."* Collie privately knows the drug safety agency had been tendered out three summers earlier and does not say so.
- Palliated with poppy. She went to sleep. She smiled through it, and did it most for Maddy.
- **Buried in the city**, next to Maddy's father, who died first — so `[placeholder_03]` is dead and interred, and if Lewis's salvage runs go to the same city his route passes both graves.
- **She co-named Maddy with Collie before the birth**, choosing *Medea* because *"she saw what was coming, and she wanted you to be strong."*
- Her last instructions: stay healthy, bury me next to your dad, take care of Maddy.

**Maddy was renamed, and the reason is institutional.** *"It was the only way to make sure that the university knew you were mine."* An orphan could not be covered unless she was a Swartz on a form — so the erasure of Alice Richards's surname is **affiliation paperwork**, not sentiment, which is why Collie would not look at her while saying it. **Collie offers to write it back and Maddy declines.**

**Which builds the *Skywave* comparison in the right order.** The apprentice there, surname **Lacks**, keeps her own name. Two orphans absorbed by two of these women, and the difference is not the guardian — **Maddy was offered the choice and chose Swartz.**

**Collie has three children and not one of them is hers biologically.** *Boil Water* calls Maddy **her thirdborn child**, so Collie counts Lewis, Nadia and Maddy in order and has for years. That answers the standing question in [`../notes/spitball.md`](../notes/spitball.md) about her case for calling Lewis her son and Nadia her daughter: there is no case, there is a count.

**Settled 2026-08-24 by *Wild Oats*, and it sharpens that count.** **Nadia is about three months older than Maddy.** Lewis calls Maddy *"the annoying baby sister who insisted she tagged along"* and Nadia protests *"we were like three months apart"* (*Wild Oats* ¶109–111, [`../manuscript/10-wild-oats.md`](../manuscript/10-wild-oats.md), unposted).

**Which fixes the birth order as Lewis, Nadia, Maddy** — Lewis *"a bit older"* in ch1 ¶19, then Nadia, then Maddy three months behind her. ***Thirdborn* matches that order exactly**, so the word is doing birth-order work: Collie is not numbering the order they came to her, she is numbering them as though she had borne them.

**Open: the order they actually entered the household is not recoverable and should not be inferred.** Maddy was co-named before her birth but raised by Alice — she was steam-sterilising Alice's syringes at about ten. Lewis got a bunk at twelve. Nona and Nadia have laminated cards delivered over three pots of tea at the collapse. Those are three different clocks and the text never converts between them.

**And it puts the physical impossibility in the children's own mouths.** Two births three months apart cannot come from one woman, so the datum Bréal is reaching for — *"You ever seen them all together? Like, lined up, side to side"* — is on the page, delivered as a squabble about which of them is the baby, with nobody explaining it and no adult present.

**And Collie tells Maddy what Medea means, with the load-bearing half removed** — medicine, poison, *"she found a place with people she could trust, and lived happily ever after."* That is Medea in Athens, which is to say after the infanticide, delivered in a fairy-tale formula. The same withholding Rosa performs three times in one farmyard, done by a classicist to a child about her own name.


## Diana's household

Chapter two introduces **Diana** (ch2 ¶71) and, in three words, a mother. What the page gives her:

- **A given name and nothing after it** — `[placeholder_05]`. She is named once, by Lewis, at a door.
- **A household outside the town.** A lodge behind a thicket, reached by a blind and the littlest path, with a dirt road back into town (ch2 ¶63). Not campus, not the town proper, not the fields.
- **A prosthetic leg** she takes off herself, and a stump that wants massaging (ch2 ¶121). She asks whether the incoming doctor could help with it (ch2 ¶129) — the only thing she is shown wanting from the university.
- **Her own production.** She hunts (ch2 ¶101), cooks (ch2 ¶79), and puts up honey-sweetened huckleberry jam that Lewis carries home in a jar identical to the one he leaves behind (ch2 ¶137). The casing he brings will come back filled with deer.
- **A mother, on the page, unnamed** — `[placeholder_06]`.

**Diana is the speaker of ch2 ¶139, and "Mother" is hers.** The added clause settles it — *"and to mind the trip home"* is advice to whoever is travelling, and that is Lewis — and the commit that added it (`797930c`) says so outright: the clause exists to put the line in Diana's mouth and give her a household, *"rather than leaving it to read as Maia knowing about the lodge."* **There is no Maia–Diana edge.**

The parentage edge is therefore **solid** — Diana calls her Mother on the page, which states the relation — while the name stays open.

**Diana and Lewis are both around high school age.** Decided off-page and recorded here because nothing in the prose pins it: ch1 ¶29 has Lewis at twelve, and ch2 ¶3 only insists he is past being patted on the head.

### What the household implies

**The secrecy runs one way.** Diana's mother knows Lewis well enough to send him off with a word about the road. Bréal knows enough to tease and to let it drop (ch2 ¶141). Madam Swartz knows enough to say nothing, serve the jam, and bake the rest of it into a cake for Bréal (ch2 ¶143). Maia extracts an oath about the mead and gets a true answer to a question she should not have asked (ch2 ¶143). **The person kept in the dark is Lewis's mother, and the people covering for him include Diana's.**

Her leg is also chapter one's clinic scene arriving one generation later. Nona could not be treated because she was unaffiliated (ch1 ¶51–71), and Collie had to spend her own standing to fix that. Diana wants to know whether a doctor posted to the town for three months at a time can look at a stump. **Nobody has spent anything on her behalf yet**, and the woman who knows how to do that spending is the one quietly eating her jam.

## The fathers

**One of the four is on the page and three are not**, and that asymmetry is currently doing work whether or not it was chosen.

**Lewis's father is alive, he is Chinese, and he is Alexander "Alex" Tsien** — alive decided 2026-08-10, Chinese decided 2026-08-11 with the surname, given name settled 2026-08-13 (see `[placeholder_01]` below for the three derivations). Lewis is therefore mixed, and nothing in either posted chapter contradicts it or remarks on it. Chapter two does not yet reflect the *alive* half: ch2 ¶11's habitual *"His father would say"* and his absence from the ¶143 ledger both read as elegiac. **Corrected 2026-08-20 — the observatory posting is Maia's, not his.** Ch0 ¶19 is explicit: *"his mom Maia works at the observatory on the mountain, so he gets lonely sometimes,"* and ¶29's *"mom was home"* only reads right if she's usually not. Alex is the parent written present and staying — he fixes the controller, he watches the house fail, he is the one who does not leave. This file previously borrowed the observatory as a geographic excuse for *his* absence in ch2; that borrowing is wrong on its face once ch0 is read, since the posting was never his to have. *Ground*'s pillow-talk scene now dramatizes the correct version directly: Maia is the one called back up the mountain, and Alex volunteers to go **with** her, as an assistant, for this one move — which still gives ch2 a live geographic-not-mortal reading, but only for the trip in *Ground*, not as his standing situation. Whether ch2 falls inside that window is still open. **In chapter one he is written and present.** ¶25 has him take the controller apart and show Lewis where the wire to the motor had gone loose; ¶29 gives him a house where *"the lights would go out after dinner sometimes"*, and a wife who talks about selling it when they think the boy is asleep. He is the only adult male relative in the chapter, he is the reason Lewis can hold a soldering iron, and he is the one member of the household whose material circumstances are visibly failing. His marriage to Maia is stated outright in ¶75 — *"Maia and her husband"*.

**Settled 2026-08-21 by *Ground*, which is his chapter.** He is the POV throughout, and the file's long-standing complaint that he had one line of dialogue is dead. What the prose now fixes about him:

- **He is an electrician, and the trade has a season.** *"The season has been quiet, so it is good to keep my hands busy."* Collie needles him that *"electricians don't handle concrete if they can help it"* and he answers *"we make do."* He lays brick, mixes concrete, frames a doorway in 2x4s, reads the building's blueprints, and sends Nadia to the archives for them.
- **He speaks English as a second language, and the register is consistent.** Articles drop under load — *"Come down and help me with wall"*, *"is a bit more willing to work on hot wires than I want him."* He offers ***xuanguan*** and then translates it for a son who needed it translated.
- ***The old country* is his standing comparison** for how a thing ought to be done: he has been leaving the doorframe thin on purpose, holding the gap for a proper security grille, *"like how we had back in the old country. They knew their things."*
- **He arrived as a student, and the object that dates it is a wok.** Bought from an Asian grocer *"three months after landing on this side of the planet"*, with something of mango and sago the same day, *"for the train back to campus."* **Inference, not statement:** the campus is the university's, which would put him inside the institution from arrival — the same building Collie and Maia were in — rather than meeting them later.
- **He defers to titles and cannot stop.** He knocks and says *"Doctor Swartz?"*, is told *just Collie is fine*, explains himself with *"can never be too polite"*, and says *ma'am* to her anyway three minutes later. **Collie lets that slide**, which is the second time in two chapters that a Swartz declines to correct someone twice.
- **He calls Maia *four-eyes*.** The book's only spousal nickname, and the only name anyone calls her that is not *Maia*.
- **He was present when the elevator car came out**, which makes him the household's institutional memory for the building itself.

**None of this touches the chart.** *Ground* adds no kin edge; it fills in the one adult the graph had as a node and a surname.

**Maddy's father and Nadia's father are absent without comment.** No pronoun, no reference, no gap acknowledged. The nearest thing to evidence is ¶29 calling Collie **"Mrs Swartz"** in Lewis's POV — a child's politeness convention, but it does imply a marriage happened. For Nona there is nothing at all; Nadia carries Elbakyan and no man is attached to it.

**Diana's father is not even implied.** Chapter two names her mother's existence and stops. No pronoun, no household second adult, no gap acknowledged — the same nil support `[placeholder_04]` has, and `[placeholder_07]` gets the same treatment: dotted to the mother because the pairing is unstated, dotted to Diana because the parentage must be true and is nowhere on the page.

Three ways to take it, all consistent with what is written:

- **Leave them absent.** Three of the four households are run by a woman alone and the book simply never remarks on it, which is a register choice rather than a plot point. It also sets up the covenant descent — *by flesh or by covenant* — as the household's normal rather than its exception.
- **Name them and keep them offstage.** They exist in the register, get one line each when it costs something, and never appear.
- **Give one of them a death or a departure.** Cheap and available, but it converts an absence into a wound, and the chapter's whole method is to decline that.

The chart takes no position: they are placeholder nodes, dotted to the mothers because the pairing is implied and never stated, and dotted to the children because the parentage must be true and is nowhere on the page.

## Placeholders

Numbered so each unknown is tracked separately and greppable. Numbers are append-only — nothing is renumbered when one is settled.

| Token | Slot | Note |
|---|---|---|
| ~~`[placeholder_00]`~~ | Maia's surname | **Settled 2026-08-13 — Tsien**, her husband's: *Fortification* bylines the dandelion noodle recipe to **Maia Tsien**. She is not Chinese; he is |
| ~~`[placeholder_01]`~~ | The husband's **given** name | **Settled 2026-08-13 — Alexander "Alex" Tsien.** Terrace's call, direction (3): a diaspora English given name, so he is the one adult with no grand register at all. **Three derivations, and the third is the in-universe one.** *(a)* **Alexandria** — the library, and Catherine of Alexandria is patron of scholars, teachers and librarians, so the saint thread survives on an ordinary name. *(b)* **Alexander Graham Bell**, which puts him at the root of the book's nervous system: *Isolation* runs entirely on telephony — a landline with no number pad, an operator who must connect you, a red phone nobody answers. *(c)* **Watsonianly, he is named after "Alexander the Pretty Alright"** — presumably his own answer when asked, which lands him in the book's most repeated joke, the deflection of a title: *please, just Collie is fine* / *just Rosa is **alright**, no Doctor*. **He deflects a title he was handed at birth**, and it sits in the degraded-version register beside slush and *whatever passed as stains*. **The Bell reference works by irony, not tribute** — the corrective device inverted. Bell is history's most successful claimant (Gray filed a caveat the same day; Meucci had a prior claim), and this is the one adult in the book who gets no credit for anything: one maxim, a governor screw, a house sold while his son pretends to be asleep, and no chapter. **His son carries *Latimer*, who made the filament practical and was credited for nothing. Father named for the claimant, son for the erased.** *Alexander → Alex closes the nickname slot by itself, exactly as Coelia → Collie does, and dodges a collision with **sparky**, which is already a category noun in Oyá's mouth (Isolation ¶5) rather than a nickname.* **Banked, not taken:** *Liang* (亮, bright) if he ever wants a Chinese given name alongside — it would give Maia something to call him that the shop and Collie never would; and *Isidore*, for Isidore of Seville, who compiled the *Etymologiae* as the classical world collapsed — the closest thematic fit of any candidate, better spent on a place or an institution than on a man who needs to read unremarkable |
| ~~`[placeholder_02]`~~ | Lewis's surname | **Settled 2026-08-11 — Tsien**, through his father. **Not** *Latimer*: that reference supplies his *given* name — Lewis Latimer made the carbon filament practical and is credited for none of it |
| `[placeholder_03]` | **Maddy's father**, entire name | Wholly unwritten. If he is ever named, *Swartz* is the likelier surname to be his than Collie's, given ¶29's *Mrs Swartz* — settling that also settles whether Coelia Swartz is a married name |
| `[placeholder_04]` | **Nadia's father**, entire name | Wholly unwritten, and with less support than `[placeholder_03]` — no marriage is implied for Nona anywhere. *Elbakyan* is Nona's own as far as the page goes |
| `[placeholder_05]` | **Diana's surname** | Wholly unwritten. She is introduced by given name alone (ch2 ¶71) and never gets a second one. Whether she has one the university would recognise is the same question as whether she can be treated. ***Lacks* was proposed here on 2026-08-12 and declined** — see the naming section |
| `[placeholder_06]` | **Diana's mother**, entire name | Her existence *and* the relation are on the page — Diana calls her Mother (ch2 ¶139) — so the edge is solid and only the name is open. Will equal `[placeholder_05]` if the surname passes through her |
| `[placeholder_07]` | **Diana's father**, entire name | Wholly unwritten, nil support, same standing as `[placeholder_04]` |

Rendered bare in `pedigree.dot`'s node labels — Graphviz's own bracket syntax means the literal `[placeholder_NN]` form stays in this table, not the graph.

## Naming, for consistency

The adults carry classical names that read as graduate-school nicknames which hardened — **Coelia** is a Roman *gens* name and the last Vestalis Maxima, **Maia** the eldest Pleiad and Greek for midwife, **Nona** the Parca who spins. The children split: **Medea** stays in that register (from *mēdomai*, to plan; the *med-* root of *medicine*; granddaughter of Helios), while **Nadia Elbakyan** and **Lewis** carry the corrective device — named for people the old world took from and did not credit.

**Settled 2026-08-14: the corrective device governs everyone from outside the flat, and it is a system rather than a set of nods.** **Rosa** is Rosalind Franklin, whose data was used without her knowledge. **Lacks** is Henrietta Lacks, whose cells were taken without her consent. **Ada Fleming** is Ada Lovelace *and* Williamina Fleming — two computers, one credited a century late and one hired as a housemaid before she catalogued ten thousand stellar spectra. **Carmen Warner** is Carmenta, who was credited with inventing the Latin alphabet and was invoked by midwives at childbirth, over Sylvia Ashton-Warner, who taught in remote rural schools for decades and built her method out of the words the children already had.

So there are **two women's registers**: the flat's generation is mythological and light-bearing, and everyone who arrives from outside is named for a real woman the record under-credited. Terrace's rule — *the corrective device exists to credit* — means the naming convention **is** the device, and it is already doing the work.

**Diana** joins the classical register from outside the flat: Roman goddess of the hunt, and she hunts on the page (ch2 ¶101). She is also the moon, and that is where the pattern stops being decoration.

| Name | Light |
|---|---|
| **Coelia** | *caelum*, sky, is audible in it; and the Vestalis Maxima kept a fire that was not allowed to go out |
| **Maia** | eldest of the Pleiades — a star |
| **Diana** | the moon |
| **Medea** | granddaughter of Helios — the sun |

Four of the five are named for things that hold or give light, in a book called ***Fiat Lux***. **Nona** is the exception and the interesting one: she is not a light but the Parca who *spins* — the one who makes the thread the others get measured on — and she is also the one who keeps the bees, and the apiary is the last image in chapter two (ch2 ¶145).

Every one of them goes by something a neighbour could shout across a park. The grand register is entirely on the paperwork.

**Settled 2026-08-11.** **Lewis's surname is Tsien**, through his father, who is Chinese. Maia is not. The reference is **Qian Xuesen** — who published in the West as *H. S. Tsien*, co-founded JPL, held a wartime commission, and was as inside the institution as a person could be. In 1950 his clearance was pulled; after five years of detention and house arrest he was deported, went to China, and built its missile and space programme from nothing.

**That is a different device from Elbakyan's, and it is the one this book runs on.** Elbakyan and Latimer are *taken from and not credited* — outsiders the record declined to name. Tsien is **the register being wrong about someone already on it**, applied competently, by correct procedure, at catastrophic cost to the institution doing the applying. Every failure in this book is a list problem: Nona is not on it, Diana has never been offered a card, the landrace lost a fair count on correct criteria, and the frats need a category nobody has written. Tsien is the name for that.

The surname also lands on the right line. He was an aerodynamicist and ballistician, and **ballistics and celestial navigation are the same mathematics** — so the name sits on the household that computes rate, keeps the almanac, and eventually supplies a navigator. Carrying it as *Tsien* rather than *Qian* keeps the spelling the expelling institution used.

Free rhyme, never to be pointed at: **the observatory child refusing to have this surname written onto a laminated card is refusing the name of a man who was written out of a register.**

### Lacks — declined for Diana, given to the apprentice

**Terrace, 2026-08-12:** *Lacks* was proposed for Diana, whose whole position is being taken from by an institution that will not extend her care. **Terrace declined it, and the reason governs the whole device:** putting **Henrietta Lacks**'s name on a character built to be institutionally abused is digging her up for another round of it. The corrective device exists to *credit*. It does not get to borrow a real woman's name in order to hurt a fictional one.

**The name goes to Maia's apprentice instead**, and the reasoning inverts cleanly:

- **HeLa is the first immortal human cell line** and is still dividing seventy-odd years on. The apprentice is this book's continuity device — the almanac, the rate, and eventually the navigator. Persistence is the correct association.
- **Henrietta Lacks's name was erased while her cells were used** — pseudonymised wrong for decades. The apprentice, at eight or ten, **refuses to have her surname written over on a laminated card.** That is a restoration, not a repetition. She gets to insist on exactly the thing the real woman was never asked about.
- **The almanac is a published document with a name on the title page.** Whose name goes on it is a decision that arrives decades later, when a ship going south needs figures signed by someone strangers can trust. Lacks on that title page is the whole argument, unspoken.

**She is female**, and she is the one still carrying the name decades on, holding Maia's hand at the end. *(Terrace: "if we even depict it" — the deathbed is a possible beat, not a planned one.)*

**Settled 2026-08-11.** **Bréal** is **Michel Bréal** — the philologist who proposed the marathon. He sits in neither the classical-light register nor the corrective device, and that is the answer rather than a gap: he is the only man in the book with a voice, and he is named for a man who **invented a tradition and made it real by getting people to run it.** Bréal also coined *sémantique*.

## Out of scope

Characters who are not kin, listed so the chart's completeness is auditable.

**Chapter one:**

- **The clinic doctor** — ¶51–71, male, unnamed. Shakes Collie's hand at the end of the negotiation.
- **The food bank director** — ¶9, unnamed, in the next slot on the video.
- **The messenger** who fetches Collie — ¶33–47, unnamed, ungendered.
- **The butch rendezvous** who installed the break room AC — ¶3, unnamed, ungendered.

**Chapter two:**

- **Bréal** — male, named, no surname and no kin anywhere. Drives, tosses Lewis the pliers and takes a rifle to a sunroof for overwatch (ch2 ¶53), teases him about the sage and drops it (ch2 ¶141), and receives a slice of Swartz's cake. **The only man in either chapter with a voice**, which is a load he is currently carrying alone.
- **"Egghead" is Rosa** — the incoming medical student, and the POV of *Formulary* and *Off-Label*. Takes over the village binders (ch2 ¶43); Diana wants her opinion on the leg. **ch2 and *Formulary* are the same handover from two sides** — ch2 ¶45 has the outgoing student passing her the binders, *Formulary* ¶1 has her reading the note he left. **She refuses the title twice in *Formulary* and once from Carmen, and claims it once, to a dying boy.**
- **The outgoing med student** — three months in the town, ch2 ¶43, unnamed.
- **The schoolteacher is Carmen Warner** — named 2026-08-14, and she has two names by design: **Ms Warner** to the children and the town, **Carmen** to Rosa, who is the only other university woman in the valley. ch2 ¶49 has five months left on her posting, which from early November is early April. She and Rosa knew each other at the university; Rosa held some office and got real bell peppers into the dining hall.
- **Her beau is the carpenter** — ch2 ¶49 and ¶149, still unnamed. **He arrived on the same convoy as Rosa** and did not leave on it, so the last truck was short one beau and the town was up one carpenter. **Settled 2026-08-14: he stayed because Carmen put his hand on her belly the night the convoy arrived.** She had quickened the week before, so she was already certain when he got off the truck. **The scene is on the page from the wrong side** — ch2 ¶49–51, the town fire, *around the fire Lewis could see them holding each other and exchanging stories*. Lewis watches the moment a man decides not to go home and has no idea what he is looking at.

**And the hand feels nothing.** At nineteen weeks the mother feels the movement and an outside palm cannot — external kicks are not reliably palpable by anyone else until well past twenty. So the gesture is not evidence, it is **transmission**: quickening is a diagnosis only the patient can make, and she is handing him a fact he has no way to verify. *She* was certain; *he* took her word and burned his ride home on it.
- **Carmen's pregnancy** — her first. Conception around early July, so nineteen weeks at *Off-Label* and due about 31 March. Dated off the quickening rather than a last period, because her cycles have been unreliable for years, and so have Rosa's.
- **The campus and caravan guards** — ch2 ¶41, four of them, unnamed.
- **The hardware store manager** — ch2 ¶15, unnamed. Prices rubber gloves at two vials of poppy.
- **The boys of Epsilon Rho Rho** — plural throughout, individually unnamed.

**Chapter four:**

- **Attis Cassidy** — fifteen, kicked in the head by a dairy cow at a sorting gate while the cattle were being housed for winter. Named for the Phrygian youth who dies and is mourned. **Pronounced dead at 1148 hours** on a Thursday in November, in the yard outside his family's barn, of a bleed inside the skull over the right temple. He asked Rosa not to have the cow put down and she promised. The cow is **Buttercup**.
- **Mr and Mrs Cassidy** — unnamed. She reaches for the blame first; he shakes his head, says nothing, and flicks Rosa's Saturday visit away with the back of his hand. Neither of them answers about the cow.
- **The uncle** — the rider who fetched Rosa, unnamed, and not identified as kin until he returns with the stretcher while she is doing compressions on his nephew. ch4 ¶63 asks what he is to the boy; ¶169 answers it.
- **Rusina and Seia** — *Formulary* ¶1, from the last doctor's note. One is better at soups and one at pastries. Rusina teaches Rosa to milk; the cow is **Ginger**.
- **Young Abe** — *Formulary* ¶209, a birthday and a tincture. His family pays in buttermilk.
- **Doctor Franklin** — ch4 ¶49, remembered from Rosa's freshman year. **Note the collision**: Rosa is herself named for Rosalind Franklin, so a reader who catches the reference will stall here. Deliberate or not is undecided.

***Isolation*** *(drafted at `manuscript/06-isolation.md`, unposted — added 2026-08-21, which this file had been missing entirely):*

- **Oyá** — POV, an engineering student in the university's water control room, which the radio traffic calls **Grand Central**. She reads the gauges, does the arithmetic that dates the contamination to about 1730, and is handed the handset with *"You know enough. Then it was a handshake"* — **the same handshake gesture that closes Collie's clinic negotiation in ch1 ¶71.** Her wristwatch disagrees with the wall clock by two minutes and the book notices.
- **Her professor** — unnamed **and ungendered**, which is worth preserving deliberately rather than by accident. Drinks from a flask, reads something that is *"definitely not from the university library"*, keeps the red marker, and hands the phone to a student at the moment it matters. Perun calls them ***Prof***.
- **Perun** — leads the field team at the city water works, 1215 Windsor Street. Named for the Slavic thunder god, which puts him in neither of the two established women's registers and alongside **Bréal** as a man named from a third pattern.
- **The telephone operator** — unnamed. Connects every call; the landline has no number pad. **Structurally the same institution as the laminated card** — you reach people only through someone who agrees to connect you.
- **The shift leader, and the two workers found at Windsor** — unnamed, municipal. One red phone nobody answers.
- **The Rector** — named as an office, offstage. Bréal is calculating how to keep him away from the pledge records.
- **Nona Elbakyan appears here in a junior register** — *"Ms Nona Elbakyan was instructed to help her professor enumerate and produce a list of the crops, in descending order of priority."* **Open, flagged not resolved:** *Fortification* bylines her as **Dietitian, Department of Food Sciences**, so either *"her professor"* is the faculty member she reports to as staff, or *Isolation* sits earlier in her career than its plan position implies. The prose supports the first reading and does not require the second.

***Ground*** *(posted 2026-08-21, `manuscript/09-ground.md`):*

- **It adds no named non-kin at all**, which is unusual for this book and is the chapter working as designed — a household chapter with no institution walking into it.
- **The neighbours** — unnamed, collective, and **the first group in the book with a claim the Swartz household has to dissolve rather than acquire.** They hold the building's common room; Collie undertakes to *"try my best to convince"* them so it can become the larder, behind locks, with the windows bricked. **This is the answer to `../notes/spitball.md`'s parked question of where the neighbours went: they did not go.**
- **The machinists** — a shop, offstage, holding the keys Lewis is sent for. The gate Alex wants comes from there.
- **Four Epsilon men, unnamed and not yet asked** — Collie's *"I will visit Epsilon"* is the cash value of *Boil Water*'s *"Bréal and I had a chat, and that gave me an idea."*
- **A woman on the hand crank** — unnamed, one clause, and the reason anything reaches the third floor at all.
