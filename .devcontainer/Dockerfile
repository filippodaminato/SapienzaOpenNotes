# Immagine base leggera ma completa per dev
FROM mcr.microsoft.com/devcontainers/universal:2

# Installiamo latexmk e i pacchetti più usati
RUN sudo apt-get update && sudo apt-get install -y \
    latexmk \
    texlive-latex-recommended \
    texlive-latex-extra \
    texlive-fonts-recommended \
    texlive-science \
    texlive-lang-italian \
    && sudo apt-get clean && sudo rm -rf /var/lib/apt/lists/*
