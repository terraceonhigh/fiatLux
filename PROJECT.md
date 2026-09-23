# Fiat Lux project contract

Terrace writes the novel. Models support research, planning, critique, checks,
and publication tooling.

## Authority

Use this order when sources conflict:

1. The current manuscript.
2. A current decision from Terrace.
3. Canon with valid provenance.
4. A primary source for an external fact.
5. A model proposal.
6. A historical or superseded note.

Repeated model output does not become canon. If the repository does not settle
a claim, label the claim `OPEN`.

## Manuscript boundary

Do not draft narrative prose, sample prose, or dialogue. Terrace owns all
finished prose in `manuscript/`.

These actions are permitted:

- Perform a mechanical copyedit when Terrace explicitly requests it.
- Write an in-world document when Terrace explicitly requests it.
- Add a single-line `[STORYBOARD: ...]` marker when Terrace requests storyboarding.

A storyboard can state beats, constraints, missing decisions, or continuity
work. It cannot contain finished narration or dialogue. A model cannot replace
a storyboard with prose.

Re-read a manuscript file before you make claims about it. Cite the file and
line for each textual claim.

## Provenance

Use these labels in active reference files:

- `TEXT`: The manuscript states the claim.
- `TERRACE`: Terrace made the decision.
- `SOURCE`: A cited source supports the claim.
- `MODEL`: A model proposed or inferred the claim.
- `OPEN`: The repository does not settle the claim.
- `REJECTED`: Terrace rejected the proposal.
- `SUPERSEDED`: A later decision replaced the claim.
- `UNKNOWN ORIGIN`: The surviving record does not establish authorship.

Do not rewrite a claim in a way that upgrades its authority.

## Planning and canon

Put future chapter work in `planning/`. Put system constraints in `world/`.
Put settled names, relations, places, and chronology in `canon/`.

Preserve competing ideas. Mark decisions, rejections, and corrections beside
their source. Do not synthesize disagreement into a false consensus.

Historical and mixed-author material lives under `planning/legacy/`,
`planning/sessions/`, and `planning/idea-bank.md`. It can supply ideas and
attribution evidence, but it is not active authority.

## Research

Prefer primary sources. Attach a source to the claim that it supports. Separate
a sourced fact from a model extrapolation.

## Critique

Name the device and the failure together. Identify the sentence that can cause
a reread and the strongest beat in the same response. Flag a problem and let
Terrace repair the prose.

## Build and publication

Use repository commands. Do not invoke Pandoc by hand.

- `make check` runs local validation.
- `make` builds AO3 HTML.
- `make copy CH=<slug>` copies one clean chapter.
- `make publish CH=<slug>` prepares a dry run.
- Add `POST=1` only when Terrace explicitly authorizes live publication.

Never publish a chapter that contains a storyboard marker. Never publish based
on a note that claims an AO3 chapter is still a draft. Check external state.

## Commits

A model that makes a commit ends the message with a trailer that names the
model and its lab:

```
Co-Authored-By: <Model Name> <noreply@<lab domain>>
```

For example, `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Use
the lab's primary domain. Terrace's own commits carry no trailer.

## Output style

Keep chat and critique brief. Use plain, direct sentences. Remove filler,
decorative headings, promotional language, and unsupported significance.

Do not apply style-rewrite skills to the manuscript, quotations from Terrace,
primary sources, or dense canon entries unless Terrace explicitly requests it.
