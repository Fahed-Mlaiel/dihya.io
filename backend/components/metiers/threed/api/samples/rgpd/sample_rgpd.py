# Exemple ultra avancé clé en main du module RGPD API Threed (Python)
from ..rgpd.rgpd import rgpd_sanitize
from ..audit.audit import audit_entity
import logging

def sample_rgpd_ultra():
    entity = {'name': 'Test', 'email': 'test@dihya.io'}
    sanitized = rgpd_sanitize(entity)
    audit_entity(sanitized, 'rgpd_sanitize')
    logging.info(f"Sanitized: {sanitized}")
    # Edge case: données déjà anonymisées
    sanitized2 = rgpd_sanitize({'name': None, 'email': None})
    logging.info(f"Sanitized edge: {sanitized2}")
    print('RGPD ultra avancé exécuté avec succès.')
