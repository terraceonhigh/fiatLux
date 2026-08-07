# AO3 posting kit

**Live and posted: https://archiveofourown.org/works/89851861** — *Fiat Lux*, chapter 1 *ante finem mundi*.

## The repo is canonical

Write here. AO3 is a publishing target, not a working copy.

This was tested the hard way: chapter one was edited directly in the AO3 editor on 5–7 August (eleven changes, all improvements, made on a bus) and the repo went stale behind it. Those edits were pulled back on 7 August and the two are now byte-identical.

**Why the direction matters:** AO3 keeps **no version history**. An edit overwrites, permanently, with no way back. The repo is the only place any previous draft exists. Editing on AO3 is fine when it is the machine you have — just sync it back the same day, or the previous version is gone.

**To sync AO3 → repo**, if it happens again: diff the rendered page text against a markdown-stripped copy of the chapter, then apply the changes to the `.md` rather than pasting the page in. The rendered page loses the `*italics*`, so pasting it back would silently flatten every line of dialogue.

## Publishing a chapter

```
python3 manuscript/to-ao3.py manuscript/00-ante-finem-mundi.md
```

Writes `.ao3.html` beside the source. Paste that into the AO3 editor with **HTML mode toggled on** — AO3 does not parse markdown, so pasting the `.md` shows literal asterisks. Chapter one renders as 32 paragraphs, 20 italic runs, 6 section breaks.

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

## State

Chapter one is **posted and public** as of 4 August 2026. Chapter two exists only in the repo — AO3 shows `1/?`.

Note the stakes changed with posting: edits to chapter one are now edits to something people have read.
