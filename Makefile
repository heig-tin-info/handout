SPHINXOPTS ?=
SPHINXBUILD ?= sphinx-build
SOURCEDIR = src
BUILDDIR = build
DISTDIR = dist

all: $(DISTDIR)/html.tar.gz $(DISTDIR)/handout.pdf $(DISTDIR)/info.1

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

$(BUILDDIR)/latex/handout.pdf: pdf
$(BUILDDIR)/man/info.1: man

$(DISTDIR)/%: $(BUILDDIR)/latex/% | $(DISTDIR)
	cp $< $@

$(DISTDIR)/%: $(BUILDDIR)/man/% | $(DISTDIR)
	cp $< $@

$(DISTDIR)/%: html | $(DISTDIR)
	tar cvzf $(DISTDIR)/html.tar.gz $(BUILDDIR)/html

html: Makefile
	$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

man: Makefile
	$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

pdf latexpdf: Makefile
	@$(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

latex: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

$(ARTIFACTS_DIR):
	mkdir $@

$(ARTIFACTS_DIR)/heig-vd.pdf:
	@wget -P$(ARTIFACTS_DIR) $(ARTIFACTS_URL)/heig-vd.pdf

pull:
	docker-compose build

clean:
	$(RM) -rf $(BUILDDIR) _static

spellcheck:
	@$(SPHINXBUILD) -b spelling "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

$(DISTDIR):
	mkdir -p $@

# Because sphinx calls it...
all-pdf:

.PHONY: all pdf html latexpdf clean artifacts dist pull all-pdf spellcheck help
