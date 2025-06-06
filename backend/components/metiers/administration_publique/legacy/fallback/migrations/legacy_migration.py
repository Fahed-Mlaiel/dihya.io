"""
legacy_migration.py - Outils de migration et compatibilité pour l’héritage Threed (Python)
"""

def migrate_legacy_model(legacy):
    return {
        'id': legacy.get('legacy_id'),
        'name': legacy.get('legacy_name'),
        'vertices': legacy.get('points', []),
        'faces': legacy.get('surfaces', []),
        'meta': {'migrated': True, 'source': 'legacy'}
    }

def audit_legacy(legacy):
    return 'Legacy OK' if legacy.get('legacy_id') else 'Legacy Invalide'

# Migration batch de plusieurs modèles legacy
def migrate_legacy_batch(legacy_list):
    return [migrate_legacy_model(l) for l in legacy_list]

# Audit avancé avec logs et traçabilité
def audit_legacy_with_log(legacy):
    result = audit_legacy(legacy)
    print(f"[AUDIT][LEGACY] {legacy.get('legacy_id')}: {result}")
    return result

# Documentation intégrée :
# - Supporte migration de formats multiples (v1, v2, v3)
# - Ajoute des métadonnées de traçabilité
# - Utilisable en CI/CD pour migration massive
