#!/bin/bash
# Copie la structure de /blueprints/blockchain (dossiers uniquement, sans fichiers)
# vers /blueprints/tests_centralises/blockchaine

set -e

SRC="/workspaces/dihya.io/blueprints/blockchain"
DEST="/workspaces/dihya.io/blueprints/tests_centralises/blockchaine"

find "$SRC" -type d | while read -r dir; do
  rel="${dir#$SRC}"
  mkdir -p "$DEST$rel"
done

echo "Structure copiée de $SRC vers $DEST (sans fichiers)."
