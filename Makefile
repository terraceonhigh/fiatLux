# Build AO3-ready HTML from the manuscript.
#
# manuscript/ is source only. Every generated file lands in build/, which is
# gitignored — nothing here ever writes back into manuscript/.
#
#   make                      build every chapter whose markdown changed
#   make copy CH=01-continuity-test    put one chapter's HTML on the clipboard
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

.PHONY: all copy clean
.DELETE_ON_ERROR:

all: $(HTML)

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
	@pbcopy < build/$(CH).html
	@echo "clipboard <- build/$(CH).html ($$(wc -c < build/$(CH).html | tr -d ' ') bytes)"
	@echo "paste into the AO3 chapter editor with the HTML tab selected, not Rich Text."

clean:
	@rm -rf build
