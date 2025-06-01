#!/bin/bash
# Test automatisé pour tous formats et cas métiers spécifiques
set -e
cd "$(dirname "$0")"

# Test XML
for f in *.xml; do
  xmllint --noout "$f" && echo "[OK] $f : XML valide" || echo "[FAIL] $f : XML invalide"
done
# Test TOML
for f in *.toml; do
  python3 -c 'import toml,sys; toml.load(open(sys.argv[1]))' "$f" && echo "[OK] $f : TOML valide" || echo "[FAIL] $f : TOML invalide"
done
# Test Markdown
for f in *.md; do
  grep -q '|' "$f" && echo "[OK] $f : Markdown tabulaire détecté" || echo "[WARN] $f : Markdown non tabulaire"
done
# Test XLSX
for f in *.xlsx; do
  python3 -c 'import openpyxl,sys; openpyxl.load_workbook(sys.argv[1])' "$f" && echo "[OK] $f : XLSX valide" || echo "[FAIL] $f : XLSX invalide"
done
# Test PDF
for f in *.pdf; do
  python3 -c 'import PyPDF2,sys; PyPDF2.PdfReader(open(sys.argv[1],"rb"))' "$f" && echo "[OK] $f : PDF lisible" || echo "[FAIL] $f : PDF illisible"
done
