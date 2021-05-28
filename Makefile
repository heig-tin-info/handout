SPHINXOPTS ?=
SPHINXBUILD ?= sphinx-build
SOURCEDIR = src
BUILDDIR = build
DISTDIR = dist

DOCKER ?= docker-compose run latex

all: $(DISTDIR)/html.tar.gz $(DISTDIR)/handout.pdf $(DISTDIR)/info.1

$(BUILDDIR)/latex/handout.pdf: pdf
$(BUILDDIR)/man/info.1: man

$(DISTDIR)/%: $(BUILDDIR)/latex/% | $(DISTDIR)
	cp $< $@

$(DISTDIR)/%: $(BUILDDIR)/man/% | $(DISTDIR)
	cp $< $@

$(DISTDIR)/%: html | $(DISTDIR)
	tar cvzf $(DISTDIR)/html.tar.gz $(BUILDDIR)/html

html: Makefile
	$(DOCKER) $(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

man: Makefile
	$(DOCKER) $(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

pdf latexpdf: Makefile
	@$(DOCKER) $(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

latex: Makefile
	@$(DOCKER) $(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

$(ARTIFACTS_DIR):
	mkdir $@

$(ARTIFACTS_DIR)/heig-vd.pdf:
	@$(DOCKER) wget -P$(ARTIFACTS_DIR) $(ARTIFACTS_URL)/heig-vd.pdf

pull:
	docker-compose build

clean:
	$(DOCKER) $(RM) -rf $(BUILDDIR) _static

spellcheck:
	@$(DOCKER) $(SPHINXBUILD) -b spelling "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

$(DISTDIR):
	mkdir -p $@

# Because sphinx calls it...
all-pdf:

.PHONY: all pdf html latexpdf clean artifacts dist pull all-pdf spellcheck
