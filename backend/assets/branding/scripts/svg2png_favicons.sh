#!/bin/bash
# Script de conversion SVG -> PNG pour favicons API backend Dihya
# Nécessite : inkscape

SRC_DIR="$(dirname "$0")/../api_favicons/svg"
DST_DIR="$(dirname "$0")/../api_favicons/png"
mkdir -p "$DST_DIR"

for svg in "$SRC_DIR"/*.svg; do
  name=$(basename "$svg" .svg)
  inkscape "$svg" --export-type=png --export-filename="$DST_DIR/$name.png" --export-width=64 --export-height=64
done
