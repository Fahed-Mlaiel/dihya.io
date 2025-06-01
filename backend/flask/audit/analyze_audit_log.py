"""
Script d’analyse et d’export des logs d’audit pour Dihya Coding.

Ce module permet de filtrer, rechercher, agréger et exporter les logs d’audit
pour répondre aux besoins de conformité, de sécurité et de traçabilité.

Bonnes pratiques :
- Ne jamais afficher ou exporter de secrets ou de données confidentielles.
- Restreindre l’accès à ce script aux administrateurs ou responsables conformité.
- Documenter chaque filtre ou mode d’analyse proposé.
- Prévoir des exports CSV/JSON pour l’audit externe.
- Logger chaque accès ou export de logs d’audit.

Exécution :
    python analyze_audit_log.py --user alice --action delete_project --export csv

"""

import argparse
import csv
import json
from datetime import datetime

AUDIT_LOG_FILE = "audit/audit.log"

def parse_log_line(line):
    """
    Parse une ligne de log d’audit au format standard.
    """
    try:
        timestamp, user, action, resource, status, details = [x.strip() for x in line.split("|", 5)]
        return {
            "timestamp": timestamp,
            "user": user,
            "action": action,
            "resource": resource,
            "status": status,
            "details": details
        }
    except Exception:
        return None

def filter_logs(logs, user=None, action=None, status=None):
    """
    Filtre les logs selon les critères donnés.
    """
    for log in logs:
        if user and log["user"] != user:
            continue
        if action and log["action"] != action:
            continue
        if status and log["status"] != status:
            continue
        yield log

def export_logs(logs, export_format="csv", output_file=None):
    """
    Exporte les logs filtrés au format CSV ou JSON.
    """
    if export_format == "csv":
        fieldnames = ["timestamp", "user", "action", "resource", "status", "details"]
        with open(output_file, "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for log in logs:
                writer.writerow(log)
    elif export_format == "json":
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(list(logs), f, indent=2, ensure_ascii=False)

def main():
    parser = argparse.ArgumentParser(description="Analyse et export des logs d’audit Dihya Coding")
    parser.add_argument("--user", type=str, help="Filtrer par utilisateur")
    parser.add_argument("--action", type=str, help="Filtrer par action")
    parser.add_argument("--status", type=str, help="Filtrer par statut (SUCCESS/FAIL)")
    parser.add_argument("--export", type=str, choices=["csv", "json"], help="Exporter le résultat")
    parser.add_argument("--output", type=str, help="Nom du fichier d’export")
    args = parser.parse_args()

    with open(AUDIT_LOG_FILE, "r", encoding="utf-8") as f:
        logs = [parse_log_line(line) for line in f if parse_log_line(line)]

    filtered_logs = list(filter_logs(logs, user=args.user, action=args.action, status=args.status))

    print(f"Résultats trouvés : {len(filtered_logs)}")
    for log in filtered_logs:
        print(log)

    if args.export and args.output:
        export_logs(filtered_logs, export_format=args.export, output_file=args.output)
        print(f"Export effectué dans {args.output}")

if __name__ == "__main__":
    main()