#!/bin/bash
export DOCNAME=amunpaper
export COMPILER=xelatex
#python abbreviate.py
$COMPILER $DOCNAME
bibtex $DOCNAME
$COMPILER $DOCNAME
$COMPILER $DOCNAME


