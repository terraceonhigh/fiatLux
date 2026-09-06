# Setting map

*The geography, as a graph. Companion to [`setting-map.dot`](setting-map.dot) — open it with a Graphviz preview, same as the pedigree.*

**This is a transit map and a texture map, not a model.** It records what is where, what flows between, and who holds it. Nothing here is meant to be plugged into a simulator, and no quantity on it is load-bearing.

**The setting is a blend and is not pinned.** The university is a fictionalised melange of three real coastal campuses; the level above is never resolved as one capital or another. Retail names on the graph are **shorthand for types** — a big-box electronics retailer, a big-box general retailer with a sporting-goods counter, a standalone home-improvement warehouse. The function survives the blend; the sign over the door does not.

## How to read it

| Node fill | Jurisdiction |
|---|---|
| white | campus |
| grey | municipal |
| light blue | the regional utility authority |
| pink | the level above, or absent |
| **yellow** | not a place — a **stock** that drains |

| Edge | Layer |
|---|---|
| solid black | **transit** — a route someone travels on the page |
| blue | **water**, source to tap |
| gold | **power**, generation to load |
| dashed grey | **trade**, direction of goods |
| dotted | an **institutional** input, not a physical one |

**Three layers over one node set, because they fail on different clocks.** A place can be reachable, dry and dark in any combination, and the combination is the texture. Dashed nodes are unresolved.

## The spine

The transit layer is a line, not a web: **campus → the standalone home-improvement store → the electronics box → the general retailer → the town → the copper site → the lodge.** That is chapter two's itinerary in order.

It carries a hard constraint. Governed at sixty kilometres an hour (ch2 ¶13), arriving before sundown (ch2 ¶41), with a stop en route — which puts the town in the low hundreds of kilometres and fixes the map's scale whether or not a distance is ever stated.

## The three stocks

Everything that drains is yellow, and there are three.

**Suburbia** holds the population at year zero and is deliberately amorphous — a distribution rather than a place, which is why it has no geometry. **It is the upstream driver of nearly every failure on the graph.** Its emptying starves the tax base, which starves the utility requisition, which is how the water dies; and the same emptying is what makes the big-box ring safe to strip. Chapter one's whole geography — the red and blue bus routes, the supermarket, the daycare, the park, the father's place with the lights going out — lives inside this node.

**Salvage** is the ring and the copper site: a stock, not a flow, and the only economy the book currently runs on. The cut chain lying two feet from where they cut it that spring (ch2 ¶53) is a stock being worked, not a place being visited.

**Import capacity** is the port, and it is the odd one out — see below.

## The port is the only node that fails institutionally

Its inputs are **administrative capacity, economic clearing, and political stability**. Its output is import goods. Nothing physical enters that list.

So the port fails on the **administrative clock, not the infrastructure clock** — the pier, the cranes and the ships stay perfectly serviceable while the goods stop. That is the structural answer to why "Alibaba was spotty" (ch2 ¶1) can coexist with a crew stripping thirty kilos of copper by hand: the channel is *technically reachable and financially unreachable*. Mead and poppy do not clear internationally.

Drawing it this way also means the port's failure is **recoverable in principle and by nobody in practice**, which is a different flavour of loss from a burst main.

## Downtown is on the map and never entered

Salvage follows parking lots. Every location the crew works is a big box with its own lot, on an arterial with signals — which is also why the flashing red at ch2 ¶15 is a *suburban* intersection and not a dense grid. A downtown core is multi-storey, hard to drive into, and expensive to work.

So downtown is named, visible, adjacent and declined. It also earns a second job: **it is where the municipality was.** It is the node whose jurisdiction colour goes to *absent* while the buildings are still standing, which is the book's thesis in one node.

## What the graph decides by being drawn

Two questions the continuity audit filed as open resolve the moment a node has to be placed:

- **The water source.** Drawn gravity-fed from a protected upland watershed through a treatment works to a balancing reservoir — which is what supplies pressure, which is what *Isolation* races. Treatment sits *upstream* of the valve, so ch1 ¶13's UV budget line has a physical location, and cutting the municipal connection does not cut the university's treatment.
- **The campus power.** Still dashed. Whether the university has its own district energy, or hangs off the substation like everyone else, is undecided — and the dashed gold edge to the ring, labelled *the flashing signals?*, is the same question asked from the other end.

## The climate is pinned even though the place is not

The blend leaves the jurisdiction unresolved; it does not leave the weather unresolved, because *Isolation* runs on the deficit.

**Mediterranean-shaped year, rain-shadowed, roughly 640 mm annually** — concentrated October to May, with July and August near-desert at 15–25 mm. Choose the drier of the plausible coastal figures deliberately: it puts the setting **just above the threshold where dry farming remains a real practice rather than a comfortable default**, so an unirrigated season is survivable, argued about, and not free. The wetter figure would remove the argument.

Consequence for the graph: **the campus farm is irrigation-dependent from May to September in every year, not only the bad ones.** The blue layer is therefore a food dependency as well as a drinking-water one, and cutting the municipal connection cuts both at once. No city is named and none needs to be.

## The household building, added 2026-08-21 from *Ground*

***Ground* is a chapter about a place and this map had no node for it.** Everything here is stated in `manuscript/09-ground.md` unless marked. **Not yet in [`setting-map.dot`](setting-map.dot)** — the graph still stops at the district scale, and whether the building earns its own subgraph or a single node with a note is a call left open.

**The fabric.** Third floor of the red brick (ch1 ¶19), **at least five storeys**, with a lift shaft. The **car is gone** — Alex was there when they took it out — and what remains is a **winch to the top floor, a cargo basket rated 500 kg with *DO NOT EXCEED 100 KG* painted on it**, a garden gate across the opening so nobody falls in, and a hand crank at the bottom worked by whoever is free. Instructions are hollered down the well. **The building's motive power is therefore at ground level and human**, which makes the ground floor its engine room and every upper floor expensive to supply.

**Three floors are doing three different jobs.**

| Floor | What it is now |
|---|---|
| **Fifth** | **A stock being worked, like the copper site.** Brick, foyer tiles, shelves, and apartments Lewis picks the locks on. Stripping it also *removes dead load* from the frame, which the storeroom argument leans on |
| **Third** | The household. **Two flats merging into one dwelling**: a waist-high brick wall encloses their chunk of the corridor into a *xuanguan* with the shoe racks in it, the threshold between units is coming out, and the new doorframe is deliberately half the wall's thickness to take a security grille from the machinists. The second living room is being subdivided — Nona is complaining about the sawdust |
| **Ground** | **The larder, as of this chapter, and contested.** The **common room** is to be enclosed with its windows bricked and locks fitted, which needs six men for two days. Also on this floor: a **parking lot** and **abandoned stores**, the runner-up site because it would be harder to secure |

**The neighbours are a jurisdiction and the map should treat them as one.** The common room is theirs as much as anyone's, and Collie's standing is what converts it. **The floor was an allocation written down in an office; the common room is an appropriation argued in a corridor.** That is a different colour of claim from anything else on this graph.

**Water confirms the blue layer's worst prediction.** Alex runs the tap into a bucket before he sits down, and water stands on the shower floor. **Upper storeys lose pressure first — that is just head** — so a third-floor household stores opportunistically and carries the rest up. This is post-*Isolation* behaviour presented without explanation, which is the correct way round.

**In errand range, all named in dialogue:** the greenhouses, the apiary, the dining hall, the bakery, the hospital, the machinists, the archives, the chemists, and **the river, which has a men's part** and is where the men wash after concrete.

## University country — orthography ruled 2026-08-25

**Written *University country*.** Capital U, lowercase c. Terrace's ruling; it is the standard and does not vary.

**What it names:** the area the university administers, which is **polis-administered rather than polis** — Terrace's distinction. Not dangerous. Roads are safe enough to send three teenagers out on a three-day circuit, and safe *because* the trucks are armed and the towns have posted guards, not instead of it.

**On the page once**, in Bréal's requisition check: *"Three-day circuit inside University country, radio check-ins every eight hours"* (`../manuscript/10-wild-oats.md:33`). The bare noun *the country* appears earlier and separately — `06-isolation.md:186`, *"pickles and biscuits from the country"* — so the capitalised term reads as a formalisation of something already in the characters' mouths rather than a new coinage.

## Open adjacencies

1. Is the village (ch2 ¶43) the town (ch2 ¶41), or a smaller settlement on the same circuit?
2. Is Diana's own town — the one she goes to on the alternating week — this town or another?
3. ~~Is Collie's flat (ch1 ¶9) the third-floor red brick (ch1 ¶19), or two residences?~~ **Closed 2026-08-21. Both, and then one.** ch1 ¶75 already had Maia and her husband take a *separate* flat on the same landing after wintering with Collie, so it was two residences on one floor; *Ground* is the chapter where the wall goes up and they stop being two. **Note the desync this resolves:** [`../notes/spitball.md`](../notes/spitball.md) claimed to settle this on 2026-08-12 under *The floor math* and this list was never updated, so the two files disagreed for nine days. **Where they disagree in future, the manuscript governs and this file is the place to write the answer down.**
4. Where is the campus relative to suburbia — inside it, at its edge, or across water from it?
5. Does the university generate, or only consume?

## What this is for

It is the input to a collapse-sequencing pass: given these nodes, these dependencies and these jurisdictions, **what fails when.** The layers are separated precisely so that question can be answered per-layer rather than as one undifferentiated slide into darkness.

## Proper names — settled 2026-09-05

**Three names fixed by Terrace in the session of 2026-09-05.** The note above that "the setting is a blend and is not pinned" still holds: these are invented names in the region's real morphology, not claims on real municipalities.

### The university — **Arbutus University**

*Arbutus menziesii*, the madrona, which grows in the coastal strip around the Salish Sea and almost nowhere else. Chosen over the alternatives on one principle: **a tree carries no biography.** Every person-name candidate dragged a referent that had to be managed — Lougheed brings an Alberta premier and a Burnaby shopping centre, Astor is Manhattan, Mackenzie brings two Prime Ministers, Hecate brings a goddess who knows far too much about this particular family. Malaspina was the strongest rival (a real Salish Sea institution name, retired in 2008 when Malaspina University-College became Vancouver Island University) but reads Spanish against a book whose manners are Commonwealth.

*Arbutus* is also the **northern** name for the tree — Washington says madrona, Oregon says madrone — which tilts the composite toward the UBC/UVic end. That agrees with the register already on the page: **"Senior Lecturer"** in `00-ante-finem-mundi.md` is a Commonwealth rank, and the book runs on *Madam*, *Doctor* as address, a curtsy and a courtly bow.

It harmonises with the seal already established on the currency in `08-druzhina.md`: **a Dogwood flower wrapped in a Mahonia wreath** — BC's floral emblem inside Oregon's. With Arbutus the naming system is three regional plants and no dead jurisdiction.

**Nobody says it.** Everyone in the book says *the university*. The proper name's job is to sit on a seal, a banknote, a laminated card, and an envelope addressed to Admissions.

### Fleming's town — **Aldermere**

Inland, **east** of the water, per `08-druzhina.md`: *"Same town as you, most likely, the one to the east."* Dairy country, in the real pattern of the Fraser Valley and the Whatcom lowlands. *Alder* is a genuine PNW tree, *mere* is lowland standing water. Soft, liquid consonants; sounds like a meadow.

### The Swartz town — **Weirwick**

The coastal town of `10-wild-oats.md` — guard tower, mayor, diner, **shipyard**, fishwives, and the household that wrote to Collie and Alex unprompted.

A **weir** is a tidal fish trap, genuine historical practice on this coast, so the name reads as *the inlet with the fish traps* — substantively what the town is, in a word nobody parses. ***-wick*** is the Norse-derived suffix for an inlet or trading place (Berwick, Lerwick), which fits the region's real Scandinavian settlement at Poulsbo and Sointula.

**Chosen partly on sound, against Aldermere.** Aldermere is all liquids; Weirwick is hard and ends on a *k*. **Fleming's town sounds like a meadow and the Swartz town sounds like work**, which does quiet characterisation every time either name appears.

**Naming rule observed throughout:** invented names recombine **settler-English and Scandinavian morphology only.** Saanich, Chemainus, Nooksack, Sechelt and Quilcene derive from living languages; manufacturing plausible-sounding fakes would be inventing words that belong to actual peoples. Any Indigenous place name in this setting should be a real one, used deliberately.
