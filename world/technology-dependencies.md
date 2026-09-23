# Technology dependencies

## Scope

This file owns technical dependency graphs. Each object can record its inputs,
consumables, skills, tools, energy, maintenance, outputs, substitutes, and failure modes.

## Established in the manuscript

- `TEXT` A jar of liver paste has a lid button that pops when opened
  (`manuscript/08-druzhina.md:135`). `MODEL` Vacuum-sealed jars therefore
  exist in the setting.

## Terrace decisions

- `TERRACE` The Weirwick cannery preserves salmon by high-pressure canning in
  glass jars, not tin. (Decision 2026-09-22.)

## Quantities and assumptions

## Dependencies

- `SOURCE` USDA guidance for fish: pint jars only; 100 minutes at 10 psi on a
  weighted gauge or 11 psi on a dial gauge, at low altitude. Gut the fish
  within two hours of the catch and keep it chilled until processing
  (National Center for Home Food Preservation, "Fish (pint jars, USDA)").
- `MODEL` Glass-jar canning needs pressure vessels with working gauges and
  gaskets, jars, lids or seals, fuel to hold pressure for 100 minutes per
  batch, and ice or cold water for the two-hour window.

## Failure modes

- `MODEL` Under-processing risks botulism.
- `MODEL` One-use lids run out long before jars break.
- `MODEL` An inaccurate gauge fails silently.

## Substitutes and adaptations

- `MODEL` Glass lids or zinc caps with rubber rings are reusable, but they
  need rubber.
- `MODEL` Salting, smoking, and drying need no jars, but they need salt. See
  `flows.md`.

## Open questions

- `OPEN` What lids or seals the cannery uses.
- `OPEN` Who owns the pressure vessels.
- `OPEN` Whether jar canning replaces salting or supplements it.

## Sources

Use the relevant brief in [`../research/briefs/`](../research/briefs/) for each
object. A source supports an input or failure mode; it does not settle that the
object exists in the story.

- [NCHFP: Fish (pint jars, USDA)](https://nchfp.uga.edu/how/can/preparing-and-canning-poultry-red-meats-and-seafoods/fish-pint-jars-usda/)
