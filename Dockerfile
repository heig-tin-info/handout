FROM ubuntu:focal
LABEL maintainer="Yves Chevallier <yves.chevallier@heig-vd.ch>"

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y make git wget

# Texlive
RUN apt-get install -y texlive-xetex
RUN apt-get install -y texlive-lang-french
RUN apt-get install -y texlive-fonts-extra
RUN apt-get install -y texlive-science
RUN apt-get install -y fonts-firacode
RUN apt-get install -y latex-cjk-all
RUN apt-get install -y libenchant-dev
RUN apt-get install -y hunspell-fr hunspell-fr-comprehensive
RUN apt-get install -y latexmk
RUN apt-get install -y docker-compose

# Python Sphinx
RUN apt-get install -y librsvg2-bin
RUN apt-get install -y python3 python3-pip

RUN pip3 install -U docutils==0.15.2
RUN pip3 install sphinx==3.2.1
RUN pip3 install sphinxcontrib-spelling
RUN pip3 install sphinxcontrib-svg2pdfconverter
RUN pip3 install git+https://github.com/heig-vd-tin/sphinx-heigvd-theme.git@d94eb8791106a84abfb49ee683d061ce4d66e889

RUN apt-get update

# Update font cache
RUN fc-cache -fv

ENV USER=latex
