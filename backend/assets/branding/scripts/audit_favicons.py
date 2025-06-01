#!/usr/bin/env python3
"""
Script d'audit automatique des favicons API backend Dihya.
- Vérifie l'intégrité (hash SHA-256)
- Vérifie la présence des métadonnées multilingues
- Vérifie l'accessibilité (présence alt, contraste AAA)
- Génère un rapport d'audit JSON
"""
import os
import json
import hashlib
from datetime import datetime

FAVICON_DIR = os.path.join(os.path.dirname(__file__), '../api_favicons/svg')
META_DIR = os.path.join(os.path.dirname(__file__), '../meta')
REPORT_PATH = os.path.join(os.path.dirname(__file__), 'audit_favicons_report.json')

LANGS = ["fr", "en", "de", "ar", "es", "it", "pt", "nl", "pl", "tr", "ru", "zh", "kab"]

def sha256sum(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def audit_favicons():
    report = {"date": datetime.utcnow().isoformat() + 'Z', "favicons": []}
    for fname in os.listdir(FAVICON_DIR):
        if not fname.endswith('.svg'):
            continue
        path = os.path.join(FAVICON_DIR, fname)
        meta_path = os.path.join(META_DIR, f"meta_{fname.replace('.svg','')}.json")
        entry = {"filename": fname, "exists": True, "meta": False, "hash_ok": False, "langs_ok": False, "accessibility_ok": False}
        if os.path.exists(meta_path):
            entry["meta"] = True
            with open(meta_path) as f:
                meta = json.load(f)
            # Vérif hash
            entry["hash_ok"] = (meta.get("hash") == f"sha256:{sha256sum(path)}")
            # Vérif multilingue
            entry["langs_ok"] = all(lang in meta.get("alt", {}) for lang in LANGS)
            # Vérif accessibilité
            acc = meta.get("accessibility", {})
            entry["accessibility_ok"] = acc.get("contrast") == "AAA" and acc.get("aria") and acc.get("tested")
        report["favicons"].append(entry)
    with open(REPORT_PATH, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"Audit terminé. Rapport : {REPORT_PATH}")

if __name__ == "__main__":
    audit_favicons()
