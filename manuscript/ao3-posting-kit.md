# AO3 posting kit

**Live and posted: https://archiveofourown.org/works/89851861** — *Fiat Lux*, chapter 1 *ante finem mundi*.

## The repo is canonical

Write here. AO3 is a publishing target, not a working copy.

This was tested the hard way: chapter one was edited directly in the AO3 editor on 5–7 August (eleven changes, all improvements, made on a bus) and the repo went stale behind it. Those edits were pulled back on 7 August and the two are now byte-identical.

**Why the direction matters:** AO3 keeps **no version history**. An edit overwrites, permanently, with no way back. The repo is the only place any previous draft exists. Editing on AO3 is fine when it is the machine you have — just sync it back the same day, or the previous version is gone.

**To sync AO3 → repo**, if it happens again: diff the rendered page text against a markdown-stripped copy of the chapter, then apply the changes to the `.md` rather than pasting the page in. The rendered page loses the `*italics*`, so pasting it back would silently flatten every line of dialogue.

### Never compare raw bytes — AO3 rewrites the HTML on save

The chapter body **will not** match `.ao3.html` byte-for-byte, and that is normal, not drift. AO3 normalizes on every save:

- **`\n\n<hr />\n\n` becomes ` <hr>\n\n`** — the tag is un-self-closed and hoisted onto the end of the preceding paragraph's line. Six section breaks, four characters each, so the edit-form textarea reads exactly **24 characters shorter** than the repo file.
- **A landmark `<h3>Chapter Text</h3>` lives *inside* `div.userstuff`** on the public page, inflating its `innerText` by 13 characters and 2 words. Excluding it via `cloneNode` does not work — a detached node has no layout, so `innerText` degrades to `textContent` and every paragraph break collapses.

**The check that actually works** is paragraph-level, and it is exact. Live page:

```
[...document.querySelectorAll('div.userstuff p')].map(p => p.textContent.replace(/\s+/g,' ').trim()).join('\n')
```

Repo: pull `<p>(.*?)</p>` with DOTALL out of the `.ao3.html`, strip inner tags, unescape entities, collapse whitespace, join with `\n`. SHA-256 both. As of 7 August 2026 both sides give `6adcdb9e…d561778` over 32 paragraphs and 8,206 characters.

Structural fingerprint, cheaper and usually enough: **32 paragraphs, 20 `<em>`, 6 `<hr>`**.

## Publishing a chapter

```
python3 manuscript/to-ao3.py manuscript/00-ante-finem-mundi.md
```

Writes `.ao3.html` beside the source. Paste that into the AO3 editor with **HTML mode toggled on** — AO3 does not parse markdown, so pasting the `.md` shows literal asterisks. Chapter one renders as 32 paragraphs, 20 italic runs, 6 section breaks.

## Driving that form, if it's ever scripted again

Three traps, all of which bit once:

- **Tag fields and the rating select ignore programmatic values.** Setting the input value looks like it works and is silently discarded on submit — the chips are a JS widget that rebuilds the field. You must click the visible input and *type*, using a comma to commit each tag.
- **Return inside any field submits the form.** Use the Save Draft button, not the keyboard.
- **The submit button ignores accessibility-reference clicks.** Clicking *Update* by element ref reported success and did nothing — no navigation, form still populated. A click at the button's screen **coordinates** submitted it immediately. Always confirm submission by the flash message (*"Chapter was successfully updated."*) plus the changed URL, never by the click tool's own return value.
- **The chapter body, unlike the tag and rating widgets, takes programmatic values fine.** `#content` / `chapter[content]` is a plain textarea with no rich-text layer, so setting `.value` persists through save. Check for `[contenteditable]` first if AO3 ever ships an editor.
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

**Last sync 7 August 2026, repo → AO3**: the `Nanaya` → `Maddy` rename, seven occurrences, pushed to the live chapter. The two are content-identical as of that save.

Note the stakes changed with posting: edits to chapter one are now edits to something people have read.
