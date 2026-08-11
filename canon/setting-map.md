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

- **The water source.** Drawn gravity-fed from a protected upland watershed through a treatment works to a balancing reservoir — which is what supplies pressure, which is what ch3 races. Treatment sits *upstream* of the valve, so ch1 ¶13's UV budget line has a physical location, and cutting the municipal connection does not cut the university's treatment.
- **The campus power.** Still dashed. Whether the university has its own district energy, or hangs off the substation like everyone else, is undecided — and the dashed gold edge to the ring, labelled *the flashing signals?*, is the same question asked from the other end.

## The climate is pinned even though the place is not

The blend leaves the jurisdiction unresolved; it does not leave the weather unresolved, because ch3 runs on the deficit.

**Mediterranean-shaped year, rain-shadowed, roughly 640 mm annually** — concentrated October to May, with July and August near-desert at 15–25 mm. Choose the drier of the plausible coastal figures deliberately: it puts the setting **just above the threshold where dry farming remains a real practice rather than a comfortable default**, so an unirrigated season is survivable, argued about, and not free. The wetter figure would remove the argument.

Consequence for the graph: **the campus farm is irrigation-dependent from May to September in every year, not only the bad ones.** The blue layer is therefore a food dependency as well as a drinking-water one, and cutting the municipal connection cuts both at once. No city is named and none needs to be.

## Open adjacencies

1. Is the village (ch2 ¶43) the town (ch2 ¶41), or a smaller settlement on the same circuit?
2. Is Diana's own town — the one she goes to on the alternating week — this town or another?
3. Is Collie's flat (ch1 ¶9) the third-floor red brick (ch1 ¶19), or two residences?
4. Where is the campus relative to suburbia — inside it, at its edge, or across water from it?
5. Does the university generate, or only consume?

## What this is for

It is the input to a collapse-sequencing pass: given these nodes, these dependencies and these jurisdictions, **what fails when.** The layers are separated precisely so that question can be answered per-layer rather than as one undifferentiated slide into darkness.
