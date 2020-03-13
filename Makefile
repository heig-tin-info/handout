ARTIFACTS_URL=https://github.com/heig-vd-tin/artifacts/raw/master
ARTIFACTS_DIR=_artifacts

SPHINXOPTS ?=
SPHINXBUILD ?= sphinx-build
SOURCEDIR = .
BUILDDIR = _build

DOCKER = docker run -v "$$(pwd -P |  sed s@^/mnt@@):/srv" -w/srv nowox/latex:1.2

all: artifacts html man pdf

html: Makefile
	$(DOCKER) @$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

man: Makefile
	$(DOCKER) @$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

pdf: Makefile
	$(DOCKER) @$(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

latex: Makefile
	$(DOCKER) @$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

$(ARTIFACTS_DIR):
	mkdir $@

$(ARTIFACTS_DIR)/heig-vd.pdf:
	$(DOCKER) wget -P$(ARTIFACTS_DIR) $(ARTIFACTS_URL)/heig-vd.pdf

artifacts: $(ARTIFACTS_DIR)/heig-vd.pdf

clean:
	$(RM) -rf _build _static

.PHONY: all clean artifacts dist