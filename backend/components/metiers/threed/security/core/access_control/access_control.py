# access_control.py – Contrôle d'accès centralisé
from ..policy.policy import enforce_policy

def check_access(user, resource, action):
    return enforce_policy(user, action, resource)
