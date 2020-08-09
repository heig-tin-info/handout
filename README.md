# Polycopié d'informatique

![.github/workflows/ci.yml](https://github.com/heig-tin-info/handout/workflows/.github/workflows/ci.yml/badge.svg?branch=master)

![version](https://img.shields.io/github/v/release/heig-tin-info/handout)
![downloads](https://img.shields.io/github/downloads/heig-tin-info/handout/latest/total)

Ce référentiel contient le polycopié d'informatique 1 et 2 disponible en formats:

- PDF (voir [releases](https://github.com/heig-tin-info/info-handout/releases))
- HTML (https://heig-tin-info.github.io/handout/)
- Manpage (voir [releases](https://github.com/heig-tin-info/info-handout/releases))

## Install

```bash
git clone https://github.com/heig-vd-tin/info-handout.git
cd info-handout
git submodule init
git submodulee update
make
```

## Intégration continue

Les nouvelles releases sont automatiquement générées par GitHub Actions :

- A chaque nouveau tag, les version PDF et MAN sont généréesws
- A chaque commit sur la branche `master` une version HTML est générée

## Build

Make sure you have `sphinx` and the HTML theme installed `sphinx-heigvd-theme`.

```bash
sudo apt-get install -y librsvg2-bin
sudo apt-get install -y python3 python3-pip python3-sphinx

sudo pip3 install sphinx-heigvd-theme
sudo pip3 install sphinxcontrib-svg2pdfconverter
```

Then if you would like to generate the PDF version you need LaTeX as well.

```bash
sudo apt-get install librsvg2-bin # For conversion from svg to pdf

sudo apt-get install texlive-latex-base
sudo apt-get install texlive-fonts-recommended
sudo apt-get install texlive-fonts-extra
sudo apt-get install texlive-latex-extra

sudo apt-get install latexmk

sudo pip install sphinx
sudo pip install sphinxcontrib-svg2pdfconverter
```
