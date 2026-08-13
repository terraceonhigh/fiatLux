# Pedigree — chapters one and two

*Kin among the chapter one and two cast only. Authoritative for names and relations. The setting reference was `canon/the-academy-brainstorm.md`, stripped from the branch in `7330333` and recoverable with `git show 7330333^:canon/the-academy-brainstorm.md` — see [`../notes/stripped-canon.md`](../notes/stripped-canon.md).*

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

**Collie is never identified as Maddy's mother.** ¶17 gives you *"Maddy's mom is someone who is very smart, and works at the university"* and, separately, *"Auntie Collie is a nice woman … she kisses them both."* The reader infers it; nobody says it.

That is defensible and possibly better than saying it — a child holds *Maddy's mom* and *Auntie Collie* as two facts about one person, and the section is in Nadia's POV. But **the line the whole book runs through is its least-stated relation**, so it should be a choice rather than an oversight.

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

**Lewis's father is alive, and he is Chinese** — alive decided 2026-08-10, Chinese decided 2026-08-11 with the surname. Lewis is therefore mixed, and nothing in either posted chapter contradicts it or remarks on it. Chapter two does not yet reflect the *alive* half: ch2 ¶11's habitual *"His father would say"* and his absence from the ¶143 ledger both read as elegiac. A candidate posting is the relocated observatory, mounting and maintaining the instruments, which would make his absence geographic rather than mortal. **In chapter one he is written and present.** ¶25 has him take the controller apart and show Lewis where the wire to the motor had gone loose; ¶29 gives him a house where *"the lights would go out after dinner sometimes"*, and a wife who talks about selling it when they think the boy is asleep. He is the only adult male relative in the chapter, he is the reason Lewis can hold a soldering iron, and he is the one member of the household whose material circumstances are visibly failing. His marriage to Maia is stated outright in ¶75 — *"Maia and her husband"*.

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
| `[placeholder_01]` | The husband's **given** name | **Terrace wants this named (2026-08-12).** A *Chinese* given name. He takes the controller apart, puts a soldering iron to the loose motor wire, and the maxim about testing before you close the shell is his. Three directions: **(1) the light register** — *Ming*, *Kuang*, *Liang* (bright/light), which puts him in the title's register on an unremarkable name, and ch1 ¶29 already supplies the irony that *his* are the lights that go out after dinner; **(2) the corrective device again** — **An Wang**, who invented magnetic core memory and had the patent bought out from under him, an immigrant electrical engineer whose foundational work was absorbed, though *Tsien* may already be reference enough; **(3) a diaspora English given name**, realistic, and making him the one adult with no grand register at all. A workshop nickname is a separate slot — every adult here has a formal name and one a neighbour could shout |
| ~~`[placeholder_02]`~~ | Lewis's surname | **Settled 2026-08-11 — Tsien**, through his father. **Not** *Latimer*: that reference supplies his *given* name — Lewis Latimer made the carbon filament practical and is credited for none of it |
| `[placeholder_03]` | **Maddy's father**, entire name | Wholly unwritten. If he is ever named, *Swartz* is the likelier surname to be his than Collie's, given ¶29's *Mrs Swartz* — settling that also settles whether Coelia Swartz is a married name |
| `[placeholder_04]` | **Nadia's father**, entire name | Wholly unwritten, and with less support than `[placeholder_03]` — no marriage is implied for Nona anywhere. *Elbakyan* is Nona's own as far as the page goes |
| `[placeholder_05]` | **Diana's surname** | Wholly unwritten. She is introduced by given name alone (ch2 ¶71) and never gets a second one. Whether she has one the university would recognise is the same question as whether she can be treated. ***Lacks* was proposed here on 2026-08-12 and declined** — see the naming section |
| `[placeholder_06]` | **Diana's mother**, entire name | Her existence *and* the relation are on the page — Diana calls her Mother (ch2 ¶139) — so the edge is solid and only the name is open. Will equal `[placeholder_05]` if the surname passes through her |
| `[placeholder_07]` | **Diana's father**, entire name | Wholly unwritten, nil support, same standing as `[placeholder_04]` |

Rendered bare in `pedigree.dot`'s node labels — Graphviz's own bracket syntax means the literal `[placeholder_NN]` form stays in this table, not the graph.

## Naming, for consistency

The adults carry classical names that read as graduate-school nicknames which hardened — **Coelia** is a Roman *gens* name and the last Vestalis Maxima, **Maia** the eldest Pleiad and Greek for midwife, **Nona** the Parca who spins. The children split: **Medea** stays in that register (from *mēdomai*, to plan; the *med-* root of *medicine*; granddaughter of Helios), while **Nadia Elbakyan** and **Lewis** carry the corrective device — named for people the old world took from and did not credit.

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
- **"Egghead"** — the incoming medical student, female, unnamed. Takes over the village binders (ch2 ¶43). Diana wants her opinion on the leg.
- **The outgoing med student** — three months in the town, ch2 ¶43, unnamed.
- **The schoolteacher and her beau** — ch2 ¶49, both unnamed. Five months left in her posting, and the only couple in the book who touch each other in front of everyone.
- **The campus and caravan guards** — ch2 ¶41, four of them, unnamed.
- **The hardware store manager** — ch2 ¶15, unnamed. Prices rubber gloves at two vials of poppy.
- **The boys of Epsilon Rho Rho** — plural throughout, individually unnamed.
