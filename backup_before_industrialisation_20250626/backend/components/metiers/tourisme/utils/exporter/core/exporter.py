"""
exporter.py – Export CSV/JSON, anonymisation, RGPD, audit pour Tourisme (tourisme)
"""

import json
import csv


def export_to_json(data, filepath):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return filepath


def export_to_csv(data, filepath):
    if not data:
        return filepath
    keys = data[0].keys()
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    return filepath


def anonymize(data):
    # Simule l'anonymisation RGPD
    if isinstance(data, list):
        return [{**row, "user": "anonyme"} for row in data]
    return {**data, "user": "anonyme"}
