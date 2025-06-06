# core_utils.py – Utilitaires ultra avancés, clé en main, pour tests métiers 3D
# Respecte la modularité, la conformité RGPD, l’audit, la sécurité et la performance
import uuid
import re
from datetime import datetime

def generate_id(prefix='obj'):
    return f"{prefix}-{uuid.uuid4()}"

def deep_clone(obj):
    import copy
    return copy.deepcopy(obj)

def is_valid_email(email):
    return re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email) is not None

def audit_log(action, user, meta=None):
    if meta is None:
        meta = {}
    return {
        'id': generate_id('audit'),
        'action': action,
        'user': user,
        'meta': meta,
        'timestamp': datetime.utcnow().isoformat() + 'Z'
    }
