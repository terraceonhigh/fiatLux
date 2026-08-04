# AO3 posting kit — chapter one, *ante finem mundi*

Live draft: **https://archiveofourown.org/works/89851861** — work title *Fiat Lux*, chapter 1 *ante finem mundi*. Filled and saved, **not posted**. Unposted drafts are deleted after about a month.

Chapter body: **`00-ante-finem-mundi.ao3.html`** — paste into the AO3 editor with **HTML mode toggled on**, not rich text. 38 blocks, 20 `<em>` runs for the dialogue, 6 `<hr />` section breaks. No stray asterisks or backticks.

## Driving that form, if it's ever scripted again

Three traps, all of which bit once:

- **Tag fields and the rating select ignore programmatic values.** Setting the input value looks like it works and is silently discarded on submit — the chips are a JS widget that rebuilds the field. You must click the visible input and *type*, using a comma to commit each tag.
- **Return inside any field submits the form.** Use the Save Draft button, not the keyboard.
- **Scroll-wheel over a native `<select>` changes its value.** This silently flipped the rating once. Never scroll with the cursor at an x-coordinate inside a select; use element references instead of coordinates.

And **the multiple-chapters checkbox controls whether the Chapter Title field is visible at all** — if it's unchecked, there is nowhere to put a chapter title.

## Tags — all verified canonical on AO3, with live use counts

Every tag below was checked against the tag search with **Canonical** filter on. Nothing here is invented. Counts as of checking.

### Fandom (required)
- **Original Work** — 509,678

### Characters
- **Original Female Character(s)** — 471,843

### Freeform, strongest fit first
| Tag | Uses | Why |
|---|---|---|
| **Found Family** | 226,875 | The household absorbing Lewis, then Maia and her husband. The engine of the whole thing |
| **Slice of Life** | 193,415 | Buses, poke bowls, break-room AC, a controller that stopped rumbling |
| **Worldbuilding** | 57,349 | Signals the register to exactly the readers who want it |
| **Vignette** | 20,902 | Names the form honestly — seven discrete scenes, no continuous narrative |
| **Post-Apocalypse** | 19,987 | Canonical and general. Note the plain form beats `Alternate Universe - Post-Apocalypse` (6,575) for original work, since the AU framing is a fanfic convention |
| **Apocalypse** | 18,193 | Broader net than Post-Apocalypse; both is fine |
| **Dystopia** | 10,829 | Optional. Fits the trajectory more than the current chapter |
| **Academia** | 2,069 | Small but precisely on target — the readers in it are the readers for this |

### Searched and unavailable — do not invent these
- **"Societal Collapse"** — 0 canonical results
- **"Collapse"** — 30 results, every one fandom-specific (Destiny, Murderbot, Rain World). No general tag exists
- **"Post-Apocalyptic"** (adjectival) — only `Post-Apocalyptic Hawkins (Stranger Things)`. The canonical noun form is `Post-Apocalypse`
- **"Post-Time Skip"** exists at 16,104 but reads as an anime convention (Haikyuu, Naruto, AoT dominate it). Wrong signal for this work despite the structure fitting

## Set on the draft

- **Rating** — Mature, deliberately.
- **Archive Warnings** — *Creator Chose Not To Use Archive Warnings*. Chosen over *No Archive Warnings Apply* because the warning covers the whole work, and this one is heading into a famine.
- **Summary** — *At the beginning, a restaurant advertised that they used locally grown tomatoes.*
- Language English, multiple chapters checked, `1/?`.

## Not done

**The work has not been posted.** Publishing is yours to trigger.
