"""
legacy_helper.py - Fonctions utilitaires avancées pour la gestion de l’héritage Threed (Python)
"""

def is_legacy_model(obj):
    return bool(obj.get('legacy_id'))

def convert_all(legacy_list):
    return [{**l, 'migrated': True} for l in legacy_list]

def validate_legacy(legacy):
    return bool(legacy and isinstance(legacy.get('legacy_id'), str))

# Conversion avancée de legacy vers nouveau format avec mapping dynamique

def convert_legacy_to_new(legacy):
    new = dict(legacy)
    new['id'] = legacy.get('legacy_id')
    new['name'] = legacy.get('legacy_name')
    new['migrated'] = True
    new['migratedAt'] = __import__('datetime').datetime.now().isoformat()
    return new

# Ajout de traçabilité et d’audit

def add_legacy_audit_trail(legacy):
    legacy.setdefault('auditTrail', []).append({'date': __import__('datetime').datetime.now().isoformat(), 'action': 'audit'})
    return legacy

# Documentation intégrée : helpers compatibles CI/CD, migration massive, audit
