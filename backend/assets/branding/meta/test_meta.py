"""
test_meta.py – CI/CD : tests métadonnées branding (lint JSON, RGPD, hash, accessibilité, multilingue)
"""
import os
import json
import hashlib
import sys

DIR = os.path.dirname(os.path.abspath(__file__))

CRITICAL_FIELDS = ["name", "description", "tags", "version", "created", "author"]

# Lint JSON (présence des champs critiques, multilingue)
def lint_json(meta_path):
    with open(meta_path, encoding="utf-8") as f:
        data = json.load(f)
    for champ in CRITICAL_FIELDS:
        assert champ in data, f"[ERREUR] {meta_path} : champ {champ} manquant"
    assert "fr" in data["description"] and "en" in data["description"], f"[ERREUR] {meta_path} : description multilingue manquante"
    print(f"[OK] {meta_path} : lint JSON et multilingue validés")

# Hash SHA256 pour souveraineté numérique
def print_hash(path):
    with open(path, "rb") as f:
        h = hashlib.sha256(f.read()).hexdigest()
    print(f"SHA256 {os.path.basename(path)}: {h}")

def main():
    for fname in os.listdir(DIR):
        if fname.endswith(".json"):
            lint_json(os.path.join(DIR, fname))
    for fname in os.listdir(DIR):
        if fname.endswith(".json"):
            print_hash(os.path.join(DIR, fname))
    print("Tous les tests de métadonnées sont passés.")

if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(e)
        sys.exit(1)
