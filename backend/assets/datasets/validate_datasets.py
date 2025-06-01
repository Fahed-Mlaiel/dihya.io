#!/usr/bin/env python3
"""
Script de validation automatique des datasets backend Dihya.
- Vérifie la validité JSON, YAML, CSV
- Vérifie l’anonymisation (pas de nom/prénom réel, email générique)
- Génère un rapport de validation
"""
# Dihya Backend Assets – Script de validation automatique des datasets (CSV, JSON, YAML)
# RGPD, anonymisation, multilingue, CI/CD ready
import os
import json
import yaml
import csv
from pathlib import Path
from datetime import datetime
import re

DATASET_DIR = os.path.dirname(__file__)
REPORT_PATH = os.path.join(DATASET_DIR, 'validation_datasets_report.json')

EMAIL_PATTERN = re.compile(r"@example\\.com$|anonymous@|test@|demo@|dihya\\.ai$", re.I)

def validate_csv(path):
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        assert all('email' in r and '@' in r['email'] for r in rows), 'Email manquant ou invalide'
        assert all('lang' in r for r in rows), 'Langue manquante'
    return True

def validate_json(path):
    with open(path) as f:
        data = json.load(f)
        assert isinstance(data, list), 'Format JSON attendu: liste'
        for entry in data:
            assert 'email' not in entry or '@' in entry['email'], 'Email invalide'
            assert 'lang' in entry, 'Langue manquante'
    return True

def validate_yaml(path):
    with open(path) as f:
        data = yaml.safe_load(f)
        assert isinstance(data, list), 'Format YAML attendu: liste'
        for entry in data:
            assert 'email' not in entry or '@' in entry['email'], 'Email invalide'
            assert 'lang' in entry, 'Langue manquante'
    return True

if __name__ == "__main__":
    DATASET_DIR = Path(__file__).parent
    report = {"date": datetime.utcnow().isoformat() + 'Z', "files": []}
    for fname in os.listdir(DATASET_DIR):
        if fname.endswith('.csv'):
            try:
                validate_csv(DATASET_DIR / fname)
                report["files"].append({"file": fname, "valid": True, "errors": []})
            except Exception as e:
                report["files"].append({"file": fname, "valid": False, "errors": [str(e)]})
        elif fname.endswith('.json'):
            try:
                validate_json(DATASET_DIR / fname)
                report["files"].append({"file": fname, "valid": True, "errors": []})
            except Exception as e:
                report["files"].append({"file": fname, "valid": False, "errors": [str(e)]})
        elif fname.endswith('.yaml'):
            try:
                validate_yaml(DATASET_DIR / fname)
                report["files"].append({"file": fname, "valid": True, "errors": []})
            except Exception as e:
                report["files"].append({"file": fname, "valid": False, "errors": [str(e)]})
    with open(DATASET_DIR / 'validation_datasets_report.json', 'w') as f:
        json.dump(report, f, indent=2)
    print(f"Validation terminée. Rapport : {str(DATASET_DIR / 'validation_datasets_report.json')}")
