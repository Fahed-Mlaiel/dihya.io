"""
Module de reporting de conformité pour Dihya Coding.

Ce script agrège et génère des rapports anonymisés sur la conformité RGPD et l’accessibilité,
afin de faciliter le suivi, l’audit et la communication avec les parties prenantes.

Bonnes pratiques :
- Ne jamais inclure de données personnelles ou sensibles dans les rapports
- Générer des rapports horodatés et archivables
- Prévoir l’extensibilité pour d’autres types de conformité (sécurité, souveraineté, etc.)
- Documenter chaque type de rapport généré

Utilisation :
    python compliance/reporting.py
"""

import os
import json
import datetime

from . import audit_rgpd_report, audit_accessibilite_report

REPORT_PATH = os.getenv("COMPLIANCE_REPORT_PATH", "compliance/compliance_report.json")

def aggregate_reports():
    """
    Agrège les résultats des audits RGPD et accessibilité dans un rapport global.
    """
    # Génère les rapports individuels (ils écrivent sur disque)
    audit_rgpd_report()
    audit_accessibilite_report()

    # Charge les rapports individuels
    with open("compliance/rgpd_audit_report.json") as f:
        rgpd = json.load(f)
    with open("compliance/accessibilite_audit_report.json") as f:
        access = json.load(f)

    now = datetime.datetime.utcnow().isoformat() + "Z"
    report = {
        "timestamp": now,
        "rgpd": rgpd,
        "accessibilite": access,
        "note": "Aucune donnée personnelle n’est incluse dans ce rapport."
    }
    with open(REPORT_PATH, "w") as f:
        json.dump(report, f, indent=2)
    print(f"Rapport global de conformité généré : {REPORT_PATH}")

if __name__ == "__main__":
    aggregate_reports()