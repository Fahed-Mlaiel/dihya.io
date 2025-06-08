# helpers_access.py
# Helpers avancés pour la gestion des accès (MFA, SSO, provisioning, etc.)

import time
from datetime import datetime

def generate_mfa_token(user_id):
    """Génère un token MFA simulé"""
    return f"MFA-{user_id}-{int(time.time())}"

def provision_user(user_data):
    """Simule le provisioning d'un utilisateur"""
    user_data = dict(user_data)
    user_data['provisioned'] = True
    user_data['provisionedAt'] = datetime.utcnow().isoformat()
    return user_data
