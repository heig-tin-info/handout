ARTIFACTS_URL=https://github.com/heig-vd-tin/artifacts/raw/master
ARTIFACTS_DIR=_artifacts

SPHINXOPTS ?=
SPHINXBUILD ?= sphinx-build
SOURCEDIR = .
BUILDDIR = _build

DOCKER_IMAGE = nowox/latex:2.0
DOCKER = docker run -v "$$(pwd -P):/srv" -w/srv $(DOCKER_IMAGE)

all: html man pdf

html: Makefile | artifacts
	$(DOCKER) $(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

man: Makefile
	$(DOCKER) $(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

pdf: Makefile
	$(DOCKER) $(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

latex: Makefile | artifacts
	$(DOCKER) $(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

$(ARTIFACTS_DIR):
	mkdir $@

$(ARTIFACTS_DIR)/heig-vd.pdf:
	$(DOCKER) wget -P$(ARTIFACTS_DIR) $(ARTIFACTS_URL)/heig-vd.pdf

artifacts: $(ARTIFACTS_DIR)/heig-vd.pdf

pull:
    docker pull $(DOCKER_IMAGE)

clean:
	$(RM) -rf _build _static

.PHONY: all clean artifacts dist pull
