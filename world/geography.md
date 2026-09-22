# Geography

## Scope

This file owns places, terrain, elevation, watercourses, political reach,
distance, travel time, and seasonal access.

## Established in the manuscript

- `TEXT` Aldermere is east of the university and supplies butter.
  (`manuscript/08-druzhina.md:69-77`)
- `TEXT` Weirwick is a fishing town on a three-day university circuit. It has
  a diner, a guard tower, a mayor, and a shipyard.
  (`manuscript/10-wild-oats.md:31-35`, `:89-153`, `:255-265`)
- `TEXT` University country contains more than one town.
  (`manuscript/10-wild-oats.md:187-193`)

## Terrace decisions

## Quantities and assumptions

`MODEL` University country contains approximately twelve townships. Weirwick
and Aldermere are two of them. Most townships do not need names in the story.

`MODEL` A township includes a central settlement, hamlets, farms, and resource
lands. Its total population is usually 2,000–3,000.

`MODEL` The full farm system uses approximately 90–130 km² of productive land.
Forest, settlements, steep slopes, and fishing water are additional areas.

## Dependencies

## Failure modes

## Substitutes and adaptations

## Place-name construction

`TERRACE` Invented names use settler-English and Scandinavian components.
Do not manufacture names that resemble words from living Indigenous languages.

The component list is in `place-name-components.tsv`. The list contains only
the components that produced Aldermere and Weirwick. Add a component only
after its meaning, origin, and terrain use are established.

Run this command to list candidate recombinations:

```bash
tools/place-names.py --explain
```

Use `--terrain coastal`, `--count 10`, or `--seed 4` to filter the output.
Generated names are planning material. Terrace selects names for the story.
Before selection, examine real place names and trademarks for collisions.

## Open questions

- `OPEN` Which township produces most of the grain, pulses, and potatoes?
- `OPEN` Is Aldermere the town that contains Diana's home?
- `OPEN` Which towns share the three-day circuit in *Wild Oats*?

## Sources
