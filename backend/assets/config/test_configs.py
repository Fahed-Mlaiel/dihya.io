"""
test_configs.py – CI/CD : tests configs backend (lint YAML/JSON/TOML, RGPD, sécurité)
"""
import os
import sys
import json
import tomllib
import yaml

DIR = os.path.dirname(os.path.abspath(__file__))

CRITICAL_FIELDS = ["app", "security", "rgpd", "logging"]

# Lint YAML
def lint_yaml(path):
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    for champ in CRITICAL_FIELDS:
        assert champ in data, f"[ERREUR] {path} : champ {champ} manquant"
    print(f"[OK] {path} : YAML valide et champs critiques présents")

# Lint JSON
def lint_json(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    for champ in CRITICAL_FIELDS:
        assert champ in data, f"[ERREUR] {path} : champ {champ} manquant"
    print(f"[OK] {path} : JSON valide et champs critiques présents")

# Lint TOML
def lint_toml(path):
    with open(path, "rb") as f:
        data = tomllib.load(f)
    for champ in CRITICAL_FIELDS:
        assert champ in data, f"[ERREUR] {path} : champ {champ} manquant"
    print(f"[OK] {path} : TOML valide et champs critiques présents")

def main():
    for fname in os.listdir(DIR):
        if fname.endswith(".yaml"):
            lint_yaml(os.path.join(DIR, fname))
        if fname.endswith(".json"):
            lint_json(os.path.join(DIR, fname))
        if fname.endswith(".toml"):
            lint_toml(os.path.join(DIR, fname))
    print("Tous les tests de configs sont passés.")

if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(e)
        sys.exit(1)
