# Agriculture in Cascadia

## Scope

This file owns climate, soils, crops, rotations, livestock, apiaries, irrigation,
preservation, seed life, yields, and the farm calendar.

## Established in the manuscript

- `TEXT` Affiliated bakeries use a standard loaf with wholemeal flour and
  oatmeal. (`manuscript/02-fortification.md:1-33`)
- `TEXT` The university uses greenhouses, field plots, apiaries, and a farm.
  (`manuscript/06-isolation.md:135-174`; `manuscript/12-notions.md:143-235`)
- `TEXT` The dry season can make half of the university farm brown after a
  water-system failure. (`manuscript/06-isolation.md:178-186`)
- `TEXT` Town agriculture uses oxen and university seed distribution.
  (`manuscript/10-wild-oats.md:187-193`)
- `TEXT` Commercial bakery pastry uses lard, not butter. A private-estate loaf
  is described as "lard and dill." (`manuscript/08-druzhina.md:25`)
- `TEXT` Whipped cream still exists, but only at the top of the class ladder.
  The Swartz household calls it a thing they might never find; Fleming's
  estate serves it as a topping. It is a rank marker, not a lost good.
  (`manuscript/02-fortification.md:61`; `manuscript/08-druzhina.md:163`)
- `TEXT` Butter supply is not flat across townships. A pie eaten on the road
  in another town has "less butter than they were used to."
  (`manuscript/12-notions.md:1`)
- `TEXT` Cheese comes in several kinds: cheddar and colby at the clinic
  (`manuscript/03-formulary.md:209`), gouda and parmesan at Fleming's estate
  (`manuscript/08-druzhina.md:69-95`).
- `TEXT` Ginger is a home-patch garden crop, not a traded or greenhouse good.
  (`manuscript/01-continuity-test.md:13`)

## Terrace decisions

`TERRACE` Arbutus University has access to a nearby, UW-style breadbasket. The
model uses comparable terrain and climate without the population of Seattle.

`TERRACE` The campus does not feed the campus core from its own grounds. Rural
townships provide most food through a regional farm system.

## Quantities and assumptions

### Food requirement

`MODEL` The campus-core calculation uses 2,300 edible kcal per person each
day. A population of 20,000 therefore needs 16.8 billion edible kcal each year.

`MODEL` Campus gardens, greenhouses, household plots, and small livestock
supply 10–15% of this food. The rural territory supplies approximately 14–15
billion edible kcal to the campus each year.

This rural supply is an export surplus. Rural households also consume food.
The farm system must also supply seed, animal feed, and reserves.

### Productive land

`MODEL` The working land ranges are:

| Use | Area |
|---|---:|
| Staple crops | 3,000–4,000 ha |
| Vegetables, pulses, oil crops, and orchards | 2,000–3,000 ha |
| Hay, forage, pasture, and fallow | 4,000–6,000 ha |
| Total productive land | 9,000–13,000 ha |

These ranges include lower yields, crop rotation, seed retention, and storage
losses. They do not use current industrial yields.

### Township network

`MODEL` University country contains approximately twelve townships. Ten are
not yet named. A working mix contains:

- Three grain-and-pulse townships.
- Two potato-and-field-vegetable townships.
- Two mixed livestock and forage townships.
- One orchard, oilseed, and preservation township.
- Two fishing settlements, including Weirwick.
- Aldermere as a dairy and mixed-farming township.
- One flexible mixed-farming and reserve district.

These are primary functions. Each township also produces other food.

### Production zones

`MODEL` The farm system has three broad production zones:

- The campus and near shore contain gardens, orchards, poultry, seed plots,
  apiaries, and greenhouses.
- Nearby townships produce potatoes, vegetables, dairy products, pigs, hay,
  and other fresh food.
- The outer breadbasket produces grain, pulses, oil crops, cattle, and reserve
  food.

Water transport moves much of the outer breadbasket surplus to the campus
core. Roads serve local movement and routes that do not reach navigable water.

## Dependencies

## Failure modes

## Substitutes and adaptations

## Open questions

- `OPEN` What fraction of campus calories comes from grain, potatoes, pulses,
  dairy, fish, meat, and oil?
- `OPEN` Where is the main grain and milling district?
- `OPEN` Which farm inputs survive, and which inputs have local substitutes?
- `OPEN` How large is the food reserve at the start of the dry season?

## Sources

- [`../research/briefs/cropping-a-summer-dry-coast.md`](../research/briefs/cropping-a-summer-dry-coast.md)
- [`../research/briefs/prepper-beekeeping.md`](../research/briefs/prepper-beekeeping.md)
- [`../research/briefs/the-national-loaf.md`](../research/briefs/the-national-loaf.md)
- [Statistics Canada potato production for 2024](https://www150.statcan.gc.ca/n1/daily-quotidien/241205/dq241205f-eng.htm)
- [British Columbia summary of Vancouver Island agriculture](https://archive.news.gov.bc.ca/releases/news_releases_2017-2021/2020AGRI0036-001244.htm)
