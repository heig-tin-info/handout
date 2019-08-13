# Polycopié d'informatique

Ce référentiel contient le polycopié d'informatique 1 et 2 disponible en formats:

- PDF
- HTML
- Manpage

## Install

```bash
git clone https://github.com/heig-vd-tin/info-handout.git
cd info-handout
git submodule init
git submodulee update
make html
make pdf
```

## Build

Make sure you have `sphinx` and the HTML theme installed `sphinx-press-theme`.

```bash
sudo apt-get install python3 python3-pip
sudo pip3 install sphinx sphinx-press-theme recommonmark
```

Then if you would like to generate the PDF version you need LaTeX as well.

```bash
sudo apt-get install xindy # Index parser
sudo apt-get install librsvg2-bin # For conversion from svg to pdf

sudo apt-get install texlive-latex-base
sudo apt-get install texlive-fonts-recommended
sudo apt-get install texlive-fonts-extra
sudo apt-get install texlive-latex-extra

sudo apt-get install latexmk

sudo pip install sphinx
sudo pip install sphinxcontrib-svg2pdfconverter
```
