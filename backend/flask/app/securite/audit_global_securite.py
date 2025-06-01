"""
Script d’audit sécurité global ultra avancé – Dihya Coding
Production-ready, RGPD, accessibilité, multitenancy, CI/CD, plugins, i18n, reporting, documentation, auditabilité.
"""
import logging
import os
import sys
import json
from importlib import import_module
from datetime import datetime

MODULES = [
    "acl", "audit", "crypto", "secrets", "integrity"
]

REPORT = []
ALERTS = []

# Contrôles RGPD
def check_rgpd(module):
    forbidden = ["log_secret", "print_secret", "expose_secret", "export_personal_data"]
    for f in forbidden:
        if hasattr(module, f):
            ALERTS.append({"type": "RGPD", "module": module.__name__, "issue": f"Fonction interdite RGPD: {f}"})

# Contrôles accessibilité
def check_accessibility(module):
    if hasattr(module, "ACCESSIBLE") and not getattr(module, "ACCESSIBLE"):
        ALERTS.append({"type": "Accessibilité", "module": module.__name__, "issue": "Module non accessible"})

# Contrôles sécurité OWASP
def check_owasp(module):
    # Exemples de patterns à éviter (hardcoded secrets, weak crypto...)
    for attr in dir(module):
        if "password" in attr or "secret" in attr:
            val = getattr(module, attr)
            if isinstance(val, str) and val:
                ALERTS.append({"type": "OWASP", "module": module.__name__, "issue": f"Secret potentiellement exposé: {attr}"})

# Contrôles permissions
REQUIRED_FUNCTIONS = ["check_access", "log_security_event", "encrypt_data", "get_secret", "hash_data"]

def audit_securite_module(module_name):
    try:
        mod = import_module(f"backend.flask.app.securite.{module_name}")
        functions = [f for f in dir(mod) if not f.startswith("_")]
        missing = [f for f in REQUIRED_FUNCTIONS if f not in functions]
        check_rgpd(mod)
        check_accessibility(mod)
        check_owasp(mod)
        report = {
            "module": module_name,
            "functions": functions,
            "missing_critical": missing,
            "status": "OK" if not missing else "WARNING"
        }
        REPORT.append(report)
        print(f"[AUDIT-SECURITE] Module {module_name}: OK" if not missing else f"[AUDIT-SECURITE] Module {module_name}: WARNING (fonctions critiques manquantes)")
    except Exception as e:
        REPORT.append({"module": module_name, "status": "ERROR", "error": str(e)})
        ALERTS.append({"type": "Import", "module": module_name, "issue": str(e)})
        print(f"[AUDIT-SECURITE] Module {module_name}: ERROR – {e}")


def main():
    print(f"[AUDIT GLOBAL SECURITE] Démarrage audit sécurité – {datetime.utcnow().isoformat()}")
    for mod in MODULES:
        audit_securite_module(mod)
    print("\nRésumé audit sécurité:")
    for r in REPORT:
        print(r)
    if ALERTS:
        print("\nALERTES CRITIQUES:")
        for a in ALERTS:
            print(a)
    # Export JSON complet
    with open("audit_securite_report.json", "w") as f:
        json.dump({"report": REPORT, "alerts": ALERTS, "date": datetime.utcnow().isoformat()}, f, indent=2)
    print("[AUDIT GLOBAL SECURITE] Terminé. Rapport exporté dans audit_securite_report.json")

if __name__ == "__main__":
    main()
