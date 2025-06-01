"""
Script d’audit avancé pour Dihya (RGPD, sécurité, logs, anonymisation, export)
"""
import logging
import json
from backend.audit import export_logs, anonymize_logs, audit_all

def main():
    """
    Lance l’audit complet du backend Dihya (sécurité, RGPD, accessibilité, SEO).
    """
    logging.basicConfig(level=logging.INFO)
    logging.info("Démarrage de l’audit Dihya...")
    audit_report = audit_all()
    anonymized = anonymize_logs(audit_report)
    export_logs(anonymized, "audit_report.txt")
    logging.info("Audit terminé. Rapport exporté.")

if __name__ == "__main__":
    main()
