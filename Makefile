# Build AO3-ready HTML from the manuscript.
#
# manuscript/ is source only. Every generated file lands in build/, which is
# gitignored — nothing here ever writes back into manuscript/.
#
#   make check                validate repository rules and tool self-tests
#   make                      build every chapter whose markdown changed
#   make storyboards          list unresolved manuscript storyboards
#   make ledger               refresh the mechanical manuscript ledger
#   make copy CH=01-continuity-test    put one chapter's HTML on the clipboard
#   make publish CH=01-continuity-test dry-run the AO3 chapter update
#   make publish CH=... POST=1         actually push it (needs $AO3_COOKIE or .ao3-cookie)
#   make clean                remove build/
#
# The pandoc flags are load-bearing, not stylistic:
#   -f markdown-smart   the -smart SUFFIX DISABLES smart quotes. Without it
#                       pandoc curls the author's straight apostrophes into ’
#                       and silently alters the prose.
#   --ascii             emits non-ASCII as entities (Bréal -> Br&#xE9;al).
#                       Pasting real UTF-8 into the AO3 editor via the macOS
#                       pasteboard reinterprets it as MacRoman — é becomes √©.
#                       Entities have no non-ASCII bytes left to misread.

PANDOC_FLAGS := -f markdown-smart -t html --ascii

SRC  := $(wildcard manuscript/*.md)
HTML := $(patsubst manuscript/%.md,build/%.html,$(SRC))

.PHONY: all check ledger storyboards copy publish clean
.DELETE_ON_ERROR:

all: $(HTML)

check:
	@tools/check-project.py
	@tools/verify-fidelity.py --self-test
	@tools/ao3-publish.py --self-test

ledger:
	@tools/manuscript-ledger.py

storyboards:
	@grep -nH '^\[STORYBOARD' manuscript/*.md || true

build:
	@mkdir -p build

# Every build runs the fidelity check, so a silent pandoc surprise fails here
# rather than on the Archive.
build/%.html: manuscript/%.md tools/verify-fidelity.py | build
	@pandoc $(PANDOC_FLAGS) $< -o $@
	@tools/verify-fidelity.py $< $@

copy: $(HTML)
	@test -n "$(CH)" || { \
	  echo "usage: make copy CH=<chapter-slug>"; \
	  echo "available:"; ls -1 build/*.html 2>/dev/null | sed 's|build/|  |;s|\.html$$||'; \
	  exit 2; }
	@test -f build/$(CH).html || { echo "no such chapter: build/$(CH).html"; exit 2; }
	@tools/verify-fidelity.py --no-storyboard manuscript/$(CH).md
	@tools/copy-html.py build/$(CH).html
	@echo "paste into the AO3 chapter editor with the HTML tab selected, not Rich Text."

# Headless replacement for copy-then-paste. Dry run unless POST=1. The chapter
# id comes from tools/ao3-chapters.tsv, or CHID=<id> to override. The login
# cookie is Terrace's: $AO3_COOKIE, or a .ao3-cookie file (gitignored).
publish: $(HTML)
	@test -n "$(CH)" || { \
	  echo "usage: make publish CH=<chapter-slug> [CHID=<ao3 id>] [POST=1]"; \
	  echo "available:"; ls -1 build/*.html 2>/dev/null | sed 's|build/|  |;s|\.html$$||'; \
	  exit 2; }
	@test -f build/$(CH).html || { echo "no such chapter: build/$(CH).html"; exit 2; }
	@tools/verify-fidelity.py --no-storyboard manuscript/$(CH).md
	@tools/ao3-publish.py --slug $(CH) --html build/$(CH).html \
	  $(if $(CHID),--chid $(CHID)) \
	  $(if $(wildcard .ao3-cookie),--cookie-file .ao3-cookie) \
	  $(if $(POST),--post)

clean:
	@rm -rf build
