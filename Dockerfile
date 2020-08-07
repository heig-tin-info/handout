FROM nowox/latex:2.0

RUN apt-get update
RUN apt-get install -y fonts-firacode
RUN apt-get install -y latex-cjk-all
