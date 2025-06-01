"""
Plugin métier exemple – Dihya Coding

Ce plugin ajoute un module d’audit avancé à chaque projet généré (logs structurés, conformité RGPD, export CSV).
Il démontre l’extensibilité, la sécurité, la documentation et la conformité du système de plugins Dihya.

Usage :
- À activer via l’API ou la CLI lors de la génération d’un projet.
- Ajoute automatiquement un module audit.py et la doc associée.

"""
from .generation_plugin import GenerationPluginBase
import logging

class AuditAdvancedPlugin(GenerationPluginBase):
    name = "AuditAdvanced"
    description = "Ajoute un module d’audit avancé (logs RGPD, export CSV, conformité)."
    version = "1.0.0"
    author = "Dihya Coding"
    safe = True

    def after_generation(self, code, needs):
        logging.info(f"[Plugin:{self.name}] after_generation appelé.")
        # Ajout d’un module d’audit Python
        code["backend/audit.py"] = (
            '"""\nModule d’audit avancé généré automatiquement.\nConformité RGPD, export CSV, logs structurés.\n"""\n'
            'import csv\nimport logging\n\nclass AuditLogger:\n    def __init__(self, logfile="audit.log"):\n        self.logfile = logfile\n        self.logger = logging.getLogger("audit")\n        self.logger.setLevel(logging.INFO)\n        handler = logging.FileHandler(logfile)\n        self.logger.addHandler(handler)\n\n    def log_event(self, user, action, details):\n        self.logger.info(f"{user}|{action}|{details}")\n\n    def export_csv(self, csvfile="audit_export.csv"):\n        with open(self.logfile) as fin, open(csvfile, "w", newline="") as fout:\n            writer = csv.writer(fout)\n            writer.writerow(["user", "action", "details"])\n            for line in fin:\n                parts = line.strip().split("|")\n                if len(parts) == 3:\n                    writer.writerow(parts)\n')
        # Ajout de la doc
        code["docs/audit_module.md"] = (
            """\n# Module d’audit avancé\n\nCe module permet de journaliser toutes les actions critiques, d’exporter les logs au format CSV, et d’assurer la conformité RGPD.\n- Journalisation structurée\n- Export CSV\n- Auditabilité\n- Conformité RGPD\n"""
        )
        return code
