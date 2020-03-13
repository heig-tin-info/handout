ARTIFACTS_URL=https://github.com/heig-vd-tin/artifacts/raw/master
ARTIFACTS_DIR=_artifacts

SPHINXOPTS ?=
SPHINXBUILD ?= sphinx-build
SOURCEDIR = .
BUILDDIR = _build

DOCKER = docker run -v "$$(pwd -P |  sed s@^/mnt@@):/srv" -w/srv latex1.2

all: artifacts html man

html: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

man: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

pdf: Makefile
	@$(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

latex: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

$(ARTIFACTS_DIR):
	mkdir $@

$(ARTIFACTS_DIR)/heig-vd.pdf:
	wget -P$(ARTIFACTS_DIR) $(ARTIFACTS_URL)/heig-vd.pdf

artifacts: $(ARTIFACTS_DIR)/heig-vd.pdf

clean:
	$(RM) -rf _build _static

run:
	$(DOCKER) make

build:
	docker build -t local .

.PHONY: all clean artifacts dist