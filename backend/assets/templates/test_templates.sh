#!/bin/bash
# test_templates.sh – Audit automatisé des templates Dihya (accessibilité, RGPD, multilingue)
# Usage: ./test_templates.sh

TEMPLATES_DIR="$(dirname "$0")"
REPORT="$TEMPLATES_DIR/test_templates_report.txt"
echo "# Rapport d’audit des templates Dihya – $(date)" > "$REPORT"

check_aria() {
  grep -q 'aria-' "$1" && echo "[OK] $1 : balises ARIA présentes" || echo "[WARN] $1 : balises ARIA absentes"
}

check_rgpd() {
  grep -qi 'RGPD' "$1" && echo "[OK] $1 : mention RGPD présente" || echo "[WARN] $1 : mention RGPD absente"
}

check_multilingue() {
  grep -Eq '\[FR\]|\[EN\]|\[AR\]|\[KAB\]|lang="fr"|lang="en"|lang="ar"|lang="kab"' "$1" && echo "[OK] $1 : multilingue détecté" || echo "[WARN] $1 : multilingue absent"
}

check_labels() {
  grep -q 'label' "$1" && echo "[OK] $1 : labels présents" || echo "[WARN] $1 : labels absents"
}

check_contrast() {
  grep -Eq '#fff|#222|#0057b8' "$1" && echo "[OK] $1 : couleurs de contraste détectées" || echo "[WARN] $1 : couleurs de contraste faibles ou absentes"
}

check_headings() {
  grep -Eq '<h1|<h2|<main|<footer' "$1" && echo "[OK] $1 : structure sémantique HTML détectée" || echo "[WARN] $1 : structure sémantique HTML absente"
}

check_links_accessible() {
  grep -Eq 'aria-label|role="link"' "$1" && echo "[OK] $1 : liens accessibles détectés" || echo "[WARN] $1 : liens accessibles absents"
}

check_sovereignty() {
  grep -qi 'Souveraineté numérique' "$1" && echo "[OK] $1 : mention souveraineté numérique présente" || echo "[WARN] $1 : mention souveraineté numérique absente"
}

check_multilang_full() {
  grep -q '\[FR\]' "$1" && grep -q '\[EN\]' "$1" && grep -q '\[AR\]' "$1" && grep -q '\[KAB\]' "$1" && echo "[OK] $1 : multilingue complet (FR, EN, AR, KAB)" || echo "[WARN] $1 : multilingue incomplet"
}

for f in "$TEMPLATES_DIR"/*.{html,txt,tex}; do
  [ -e "$f" ] || continue
  echo "\n## Audit de $f" >> "$REPORT"
  check_aria "$f"    | tee -a "$REPORT"
  check_rgpd "$f"    | tee -a "$REPORT"
  check_multilingue "$f" | tee -a "$REPORT"
  check_labels "$f"  | tee -a "$REPORT"
  check_contrast "$f"| tee -a "$REPORT"
done

for f in "$TEMPLATES_DIR"/*.{html,txt,xml,json,tex}; do
  [ -e "$f" ] || continue
  echo "\n## Audit avancé de $f" >> "$REPORT"
  check_headings "$f"    | tee -a "$REPORT"
  check_links_accessible "$f" | tee -a "$REPORT"
  check_sovereignty "$f" | tee -a "$REPORT"
  check_multilang_full "$f" | tee -a "$REPORT"
done

echo "\nAudit terminé. Rapport généré : $REPORT"
