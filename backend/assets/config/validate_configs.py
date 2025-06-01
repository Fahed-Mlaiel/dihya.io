#!/usr/bin/env python3
"""
Script de validation automatique des fichiers de configuration backend Dihya.
- Vérifie la validité JSON, YAML, TOML
- Vérifie la présence des champs critiques (sécurité, RGPD, accessibilité, plugins, meta)
- Génère un rapport de validation
"""
import os
import json
import yaml
import toml
from datetime import datetime

CONFIG_DIR = os.path.dirname(__file__)
REPORT_PATH = os.path.join(CONFIG_DIR, 'validation_config_report.json')

REQUIRED_FIELDS = [
    'app_name', 'version', 'log_level', 'audit', 'languages', 'plugins',
    'security', 'rgpd', 'accessibility', 'ci_cd', 'meta'
]

# Pour TOML, mapping des champs critiques vers leur section/clé
TOML_FIELD_MAP = {
    'app_name': ('app', 'name'),
    'version': ('app', 'version'),
    'log_level': ('audit', 'log_level'),
    'audit': ('audit', 'enabled'),
    'languages': ('languages', 'list'),
    'plugins': ('plugins', 'list'),
    'security': ('security', None),
    'rgpd': ('rgpd', None),
    'accessibility': ('accessibility', None),
    'ci_cd': ('ci_cd', None),
    'meta': ('meta', None)
}

files = [f for f in os.listdir(CONFIG_DIR) if f.endswith(('.json', '.yaml', '.yml', '.toml'))]
report = {"date": datetime.utcnow().isoformat() + 'Z', "files": []}

for fname in files:
    path = os.path.join(CONFIG_DIR, fname)
    entry = {"file": fname, "valid": False, "fields_ok": False, "errors": []}
    try:
        if fname.endswith('.json'):
            with open(path) as f:
                data = json.load(f)
            entry["valid"] = True
            entry["fields_ok"] = all(f in data for f in REQUIRED_FIELDS)
        elif fname.endswith(('.yaml', '.yml')):
            with open(path) as f:
                data = yaml.safe_load(f)
            entry["valid"] = True
            entry["fields_ok"] = all(f in data for f in REQUIRED_FIELDS)
        elif fname.endswith('.toml'):
            data = toml.load(path)
            entry["valid"] = True
            # Vérification avancée pour TOML
            def toml_has_field(section, key):
                if key is None:
                    # Section doit exister et ne pas être un booléen/valeur simple
                    return section in data and isinstance(data[section], dict)
                return section in data and key in data[section]
            entry["fields_ok"] = all(toml_has_field(*TOML_FIELD_MAP[f]) for f in REQUIRED_FIELDS)
        else:
            raise Exception('Format non supporté')
    except Exception as e:
        entry["errors"].append(str(e))
    report["files"].append(entry)

with open(REPORT_PATH, 'w') as f:
    json.dump(report, f, indent=2)
print(f"Validation terminée. Rapport : {REPORT_PATH}")
