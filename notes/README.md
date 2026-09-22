# Notes index

> **Migration status:** This directory is a legacy record. New planning belongs
> in [`../planning/`](../planning/). Use these files for recovery and provenance,
> not as active authority.

The manuscript is the authority for facts that appear in the story. Read
[`manuscript-ledger.md`](manuscript-ledger.md) before you use another note.

## Provenance labels

Use one label for each claim in a new or revised note:

- `TEXT` means that the manuscript states the claim. Give a file and line.
- `TERRACE` means that Terrace made the decision. Preserve Terrace's words when possible.
- `SOURCE` means that a cited source supports the claim.
- `MODEL` means that a model proposed or inferred the claim.
- `OPEN` means that the repository does not settle the claim.

Do not convert a `MODEL` claim into a `TEXT` claim by rewriting it. Do not
convert a repeated proposal into a decision.

## Active references

| File | Purpose | Authority |
|---|---|---|
| [`manuscript-ledger.md`](manuscript-ledger.md) | Facts and draft state taken from the current manuscript | `TEXT` |
| [`chapter-plan.md`](chapter-plan.md) | Sequence, future chapters, and Terrace's planning decisions | Mixed |
| [`revision-worklist.md`](revision-worklist.md) | Candidate repairs to existing prose | Mixed |
| [`parked-prose.md`](parked-prose.md) | Unused prose written by Terrace | `TERRACE` |
| [`terrace-zone-deployment.md`](terrace-zone-deployment.md) | Website work | Operational |

## Historical and supporting notes

| File | Purpose | Treatment |
|---|---|---|
| [`spitball.md`](spitball.md) | Dated design discussion | Evidence input, not a source of truth |
| [`2026-09-13-notions-fleming-session.md`](2026-09-13-notions-fleming-session.md) | One mixed-provenance session record | Extract supported claims before reuse |
| [`druzhina-elements.md`](druzhina-elements.md) | Planning material for a written chapter | Reconcile against the manuscript before reuse |
| [`external-critique.md`](external-critique.md) | Model critique and reading tests | Criticism, not story fact |
| [`stripped-canon.md`](stripped-canon.md) | Inventory of deliberately removed material | Historical recovery record |

Keep the historical files unchanged until an audit extracts their supported
claims. Git history preserves deleted text, but an unchanged archive makes the
audit easier to review.
