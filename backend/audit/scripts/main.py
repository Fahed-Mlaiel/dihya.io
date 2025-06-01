"""
Dihya – Backend Audit Scripts Entrypoint (Python)
-------------------------------------------------
- Point d'entrée unique pour les scripts d'audit backend (multi-stack, multilingue, souveraineté, sécurité)
- Permet de lancer les audits d'intégrité, conformité, accessibilité, logs, etc.
- Prêt pour intégration Python, CI/CD, Codespaces, cloud souverain
- Documentation multilingue, logs, conformité RGPD/NIS2, fallback open source

🇫🇷 Point d'entrée scripts d'audit backend Python (sécurité, fallback, multilingue)
🇬🇧 Python backend audit scripts entry point (secure, fallback, multilingual)
🇦🇪 نقطة دخول سكريبتات تدقيق الباكند (Python) مع الأمان والدعم متعدد اللغات
ⵣ Amuddu n backend audit scripts Python (amatu, fallback, multilingual)
"""

import os
import sys
import argparse
import importlib

SCRIPTS_ROOT = os.path.dirname(os.path.abspath(__file__))

AVAILABLE_SCRIPTS = {
    "check_integrity": "check_integrity.py",
    "audit_rgpd": "audit_rgpd.py",
    "audit_accessibilite": "audit_accessibilite.py",
    "audit_logs": "audit_logs.py",
    "audit_plugins": "audit_plugins.py",
    "audit_webhooks": "audit_webhooks.py",
    # Ajouter ici d'autres scripts d'audit ultra avancés
}

def list_scripts():
    print("📝 Scripts d'audit disponibles / Available audit scripts:")
    for name, file in AVAILABLE_SCRIPTS.items():
        print(f"- {name} ({file})")

def run_script(script_name, extra_args):
    if script_name not in AVAILABLE_SCRIPTS:
        print(f"❌ Script inconnu: {script_name}")
        list_scripts()
        sys.exit(1)
    script_path = os.path.join(SCRIPTS_ROOT, AVAILABLE_SCRIPTS[script_name])
    if not os.path.isfile(script_path):
        print(f"❌ Fichier script introuvable: {script_path}")
        sys.exit(1)
    # Exécution sécurisée du script cible
    sys.argv = [script_path] + extra_args
    with open(script_path, "rb") as f:
        code = compile(f.read(), script_path, 'exec')
        exec(code, {"__name__": "__main__"})

def main():
    parser = argparse.ArgumentParser(
        description="Dihya – Backend Audit Scripts Entrypoint (multi-stack, multilingue, souveraineté, sécurité)"
    )
    parser.add_argument("script", nargs="?", help="Nom du script d'audit à lancer (ex: check_integrity)")
    parser.add_argument("args", nargs=argparse.REMAINDER, help="Arguments supplémentaires pour le script")
    parser.add_argument("--list", action="store_true", help="Lister tous les scripts d'audit disponibles")
    args = parser.parse_args()

    if args.list or not args.script:
        list_scripts()
        sys.exit(0)

    run_script(args.script, args.args)

if __name__ == "__main__":
    main()

# Utilisation :
#   python main.py --list
#   python main.py check_integrity --lang fr --csv --json
#
# Sécurité : logs, audit, conformité RGPD/NIS2, fallback open source
# Multilingue : prêt pour i18n (fr, en, ar, tzm)
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution
