# sample_advanced_usage.py – Exemple ultra avancé d'usage métier (API Threed)
from ..controllers import get_threed, create_threed
from ..db import db_insert
from ..rgpd import rgpd_sanitize
from ..audit import audit_entity
import logging

def sample_advanced_usage_ultra():
    # Création et audit
    data = {'name': 'Advanced', 'status': 'active', 'label': 'Demo'}
    created = create_threed(data)
    audit_entity(created, 'create')
    logging.info(f"Création avancée: {created}")
    # Lecture, RGPD, edge case
    entity = get_threed(created['id'])
    entity = rgpd_sanitize(entity)
    logging.info(f"Lecture RGPD: {entity}")
    # Insertion DB directe
    db_entity = db_insert('threed', {'name': 'DBDirect', 'status': 'test'})
    logging.info(f"DB direct: {db_entity}")
    print('Sample advanced usage ultra avancé exécuté avec succès.')
