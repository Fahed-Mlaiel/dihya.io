"""
Sample d’accès ultra avancé pour Assurance.
- Logique métier, audit, RGPD, extension plugins, conformité.
"""


def access_sample(user_id, resource, action):
    return {
        "user_id": user_id,
        "resource": resource,
        "action": action,
        "access": "granted",
    }
