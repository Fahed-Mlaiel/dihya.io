"""
Helpers d’accès (MFA, SSO, provisioning, logs, audit, validation) – clé en main
Importe et expose toutes les fonctions du module helpers
"""
from .mfa.helpers_access import generate_mfa_token, provision_user
from .sso.sso_helper import initiate_sso_login
from .audit.advanced_access_helper import log_access_event, validate_access_policy

__all__ = [
    'generate_mfa_token',
    'provision_user',
    'initiate_sso_login',
    'log_access_event',
    'validate_access_policy',
]

# Exemple d’utilisation
# token = generate_mfa_token('user1')
# sso = initiate_sso_login('google', 'https://app.dihya.io/callback')
# log = log_access_event('user1', 'LOGIN', {'ip': '127.0.0.1'})
# validate_access_policy(user, resource, policy)
