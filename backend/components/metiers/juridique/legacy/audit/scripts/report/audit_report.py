"""
Script de génération de rapport d’audit legacy Juridique (Python)
Ultra avancé, extensible, conforme au cahier des charges.
"""

from ..export.audit_export import export_audit_logs_to_json


def generate_audit_report(filepath):
    # Exemple : générer un rapport JSON à partir des logs exportés
    export_audit_logs_to_json(filepath)
    print(f"Rapport d’audit généré : {filepath}")


if __name__ == "__main__":
    generate_audit_report("audit_report.json")
