"""
test_signatures.py – CI/CD : tests signatures email (lint HTML, accessibilité, hash, RGPD)
"""
import os
import json
import hashlib
import sys

DIR = os.path.dirname(os.path.abspath(__file__))

def lint_html(html_path):
    with open(html_path, encoding="utf-8") as f:
        content = f.read()
    assert 'alt=' in content, f"[ERREUR] {html_path} : attribut alt manquant"
    assert 'aria-label' in content, f"[ERREUR] {html_path} : aria-label manquant"
    print(f"[OK] {html_path} : accessibilité HTML validée")

def check_metadata(fpath):
    base = os.path.basename(fpath)
    meta = os.path.join(DIR, f"meta_{base[:-5]}.json") if base.endswith('.html') else os.path.join(DIR, f"meta_{base[:-4]}.json")
    assert os.path.isfile(meta), f"[ERREUR] {meta} manquant pour {fpath}"
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
        if fname.endswith(".html"):
            lint_html(os.path.join(DIR, fname))
            check_metadata(os.path.join(DIR, fname))
        if fname.endswith(".txt"):
            check_metadata(os.path.join(DIR, fname))
    for fname in os.listdir(DIR):
        if fname.endswith((".html", ".txt", ".json")):
            print_hash(os.path.join(DIR, fname))
    print("Tous les tests de signatures email sont passés.")

if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(e)
        sys.exit(1)
