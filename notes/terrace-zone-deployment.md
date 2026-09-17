# Terrace.zone deployment coordination

The website currently lives in a separate repository:

- `terrace-zone`: `https://github.com/terraceonhigh/terrace-zone.git`
- Published site: `https://terrace.zone`
- GitHub Pages serves `main` from the repository root.
- The generated Fiat Lux page is `writing/fiat-lux.html`.
- The source copy used by the site is `terrace-zone/writing/posts/fiat-lux.md`.

## Intended setup

Coordinate the repositories so that `terrace-zone` is available as a named remote from this repository. Do not replace the existing Proton Drive `origin` until the remote arrangement is agreed. A likely arrangement is:

```text
fiatLux
  origin       Proton Drive mirror
  terrace-zone GitHub repository, if the project is moved or mirrored there
```

The direction of synchronization needs to stay explicit. The manuscript in `fiatLux/manuscript/` is the source of truth. The website copy is a canary publication and may contain newer or rougher prose than AO3.

## GitHub work

- Decide whether the GitHub repository should receive a push from `fiatLux`, or whether a workflow should pull from a GitHub-visible `fiatLux` repository.
- If `fiatLux` is published to GitHub, add a workflow that copies the manuscript chapters into `terrace-zone/writing/posts/fiat-lux.md`, preserves the site front matter and canary notice, runs `python3 build.py`, and commits the generated HTML.
- Prefer a pull request from the workflow over a direct push to `terrace-zone/main` unless branch protection is deliberately not wanted.
- Keep `pandoc` available in the workflow, since `build.py` shells out to it.
- Limit the workflow to the Fiat Lux source and generated page. It must not overwrite other posts or the site's index unless the normal build changes that index.
- Add a fidelity or diff check so an empty manuscript chapter produces a heading but no invented prose.
- Record the chosen remote names, token or deploy-key ownership, branch names, and whether the workflow runs on push or on manual dispatch.

## Before wiring automation

- Agree which repository owns the synchronization workflow.
- Agree whether the workflow may commit to `terrace-zone/main` or must open a pull request.
- Decide how the site source handles manuscript chapters that are empty locally.
- Test the generated page locally and check that the canary notice remains at the top of the post.

## Open todos (2026-09-17)

- Copy this repository to Forgejo. Decide whether Forgejo becomes a mirror, a new remote alongside Proton Drive `origin`, or the arrangement described above under `terrace-zone`.
- Figure out how to stand up a VSCode tunnel from `humboldt` (presumably a home server or workstation), so the machine is reachable for remote editing.
