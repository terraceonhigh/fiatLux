# Publishing

The manifest records external state. It can become stale. Check AO3 before a
live update.

## Commands

```bash
make
make copy CH=01-continuity-test
make publish CH=01-continuity-test
make publish CH=01-continuity-test POST=1
```

`make publish` is a dry run unless `POST=1` is present. A live update requires
explicit authorization from Terrace.

Credentials belong in the ignored `.ao3-cookie` file or `AO3_COOKIE`. Never
commit or print them.

`tools/ao3-chapters.tsv` remains the machine input for the publisher during the
migration. `ao3-manifest.yml` owns the fuller external-state record.
