FROM ubuntu:latest

SHELL ["/bin/bash", "-c"]

WORKDIR /local/npm

RUN apt-get update -y && \
    apt-get install -y asciidoctor make nodejs npm pandoc && \
    npm install asciidoctor asciidoctor-pdf asciidoc-link-check
