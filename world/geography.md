# Geography

## Scope

This file owns places, terrain, elevation, watercourses, political reach,
distance, travel time, and seasonal access.

## Established in the manuscript

- `TEXT` Aldermere is east of the university and supplies butter.
  (`manuscript/08-hyperbolic.md:69-77`)
- `TEXT` Weirwick is a fishing town on a three-day university circuit. It has
  a diner, a guard tower, a mayor, and a shipyard.
  (`manuscript/10-wild-oats.md:31-35`, `:89-153`, `:255-265`)
- `TEXT` University country contains more than one town.
  (`manuscript/10-wild-oats.md:187-193`)

## Terrace decisions

`TERRACE` Arbutus University occupies a favorable Cascadian site. The setting
resembles the University of Washington region in physical form, but it does not
include Seattle or its former population.

`TERRACE` The university stands beside a navigable lake or sheltered inlet. A
short water route connects the university to the regional sea.

`TERRACE` A nearby river system connects the university to a broad, fertile
breadbasket. Farms, townships, and mills occupy this watershed.

`TERRACE` The fictional setting can combine Cascadian landforms. It does not
copy the political or settlement geography of a real region.

`TERRACE` Weirwick is set-dressed as Steveston. This governs how the town
looks, not where it sits on the map. (Decision 2026-09-22.)

`MODEL` Steveston's history includes the Japanese Canadian fishing fleet and
its seizure, which began in December 1941 (see
`research/briefs/non-white-settlers-bc.md`). The set-dressing can carry that history only if
Terrace chooses.

`TERRACE` Weirwick has a cannery, in keeping with the Steveston set-dressing.
Its process is in `technology-dependencies.md`; its salt supply is in
`flows.md`. (Adopted 2026-09-22 from a model proposal.)

`SOURCE` Edmund A. Smith's 1903 fish-butchering machine displaced Chinese
cannery butchers. Smith named it with an anti-Chinese slur (HistoryLink, File
2109). A surviving machine is at the Gulf of Georgia Cannery in Steveston.

`MODEL` Historic cannery labor was divided by race: Japanese fishermen,
Chinese butchering crews hired through contractors, Indigenous women on the
filling lines, and white management. Attach a Steveston-specific source before
use.

## Quantities and assumptions

`MODEL` University country contains approximately twelve townships. Weirwick
and Aldermere are two of them. Most townships do not need names in the story.

`MODEL` A township includes a central settlement, hamlets, farms, and resource
lands. Its total population is usually 2,000–3,000.

`MODEL` The full farm system uses approximately 90–130 km² of productive land.
Forest, settlements, steep slopes, and fishing water are additional areas.

## Dependencies

- The water route supports bulk food transport between the breadbasket and the
  campus core.
- The breadbasket supports the campus population and the township network.
- The river system creates sites for mills, ports, tolls, bridges, and flood
  control.

## Failure modes

## Substitutes and adaptations

## Place-name construction

`TERRACE` Invented names use settler-English and Scandinavian components.
Do not manufacture names that resemble words from living Indigenous languages.

The source corpus is in `place-name-corpus.tsv`. It contains 159 British
Columbia municipal names and 281 incorporated Washington place names. The BC
table was copied from a public mirror because the government directory blocked
automated retrieval.

Run this command to list candidate recombinations:

```bash
tools/place-names.py --explain
```

Use `--jurisdiction BC`, `--count 10`, or `--seed 4` to change the output.
The explanation shows both source names and their cut positions.

Generated names are planning material. Terrace selects names for the story.
Before selection, examine language origins, real names, and trademarks. Do not
use a generated fragment that imitates a living Indigenous language.

The corpus sources are:

- [British Columbia municipality list](https://www2.gov.bc.ca/gov/content/governments/local-governments/facts-framework/systems/municipalities)
- [Public mirror of the BC municipality table](https://en.wikipedia.org/wiki/List_of_municipalities_in_British_Columbia)
- [Washington State Department of Transportation city layer](https://data.wsdot.wa.gov/arcgis/rest/services/Shared/CityLimits/MapServer/0)

## Open questions

- `OPEN` What are the names of the lake, river, sound, and breadbasket?
- `OPEN` How far is the main grain plain from Arbutus University?
- `OPEN` Which authorities control the river ports and milling sites?
- `OPEN` Which township produces most of the grain, pulses, and potatoes?
- `OPEN` Is Aldermere the town that contains Diana's home?
  Yes, refer to Druzhina
- `OPEN` Which towns share the three-day circuit in *Wild Oats*?

## Sources

- [HistoryLink, File 2109: automated salmon cleaning machine, 1903](https://www.historylink.org/File/2109)
- [Tommy Ting, *Machine* (the Gulf of Georgia Cannery unit)](https://tommyting.com/Machine-Iron-Chink-invented-in-1903-found-at-the-Gulf-of-Georgia)
