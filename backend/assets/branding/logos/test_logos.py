"""
test_logos.py – CI/CD : tests logos backend (lint SVG, accessibilité, hash, RGPD)
"""
import os
import json
import hashlib
import sys

DIR = os.path.dirname(os.path.abspath(__file__))

def lint_svg(svg_path):
    with open(svg_path, encoding="utf-8") as f:
        content = f.read()
    assert 'aria-labelledby' in content, f"[ERREUR] {svg_path} : aria-labelledby manquant"
    assert '<title' in content, f"[ERREUR] {svg_path} : balise <title> manquante"
    assert '<desc' in content, f"[ERREUR] {svg_path} : balise <desc> manquante"
    assert 'role="img"' in content, f"[ERREUR] {svg_path} : role=img manquant"
    print(f"[OK] {svg_path} : accessibilité SVG validée")

def check_metadata(svg_path):
    meta = os.path.join(DIR, f"meta_{os.path.basename(svg_path)[:-4]}.json")
    assert os.path.isfile(meta), f"[ERREUR] {meta} manquant pour {svg_path}"
    with open(meta, encoding="utf-8") as f:
        data = json.load(f)
    assert "description" in data, f"[ERREUR] {meta} : description manquante"
    print(f"[OK] {meta} : métadonnées présentes et valides")

def print_hash(path):
    with open(path, "rb") as f:
        h = hashlib.sha256(f.read()).hexdigest()
    print(f"SHA256 {os.path.basename(path)}: {h}")

def main():
    for fname in os.listdir(DIR):
        if fname.endswith(".svg"):
            svg_path = os.path.join(DIR, fname)
            lint_svg(svg_path)
            check_metadata(svg_path)
    for fname in os.listdir(DIR):
        if fname.endswith(".svg") or fname.endswith(".json"):
            print_hash(os.path.join(DIR, fname))
    print("Tous les tests de logos sont passés.")

if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(e)
        sys.exit(1)
