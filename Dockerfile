FROM nowox/latex:2.0

RUN apt-get update
RUN apt-get install -y fonts-firacode
RUN apt-get install -y latex-cjk-all
RUN apt-get install -y libenchant-dev
RUN apt-get install -y hunspell-fr hunspell-fr-comprehensive
RUN pip3 install sphinxcontrib-spelling

# .devcontainer
RUN apt-get install -y docker-compose