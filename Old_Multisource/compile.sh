#!/bin/bash
export DOCNAME=amunpaper
#python abbreviate.py
xelatex $DOCNAME
bibtex $DOCNAME
xelatex $DOCNAME
xelatex $DOCNAME

