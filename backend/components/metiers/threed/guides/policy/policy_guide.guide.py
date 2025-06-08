# Guide ultra avancé pour la gestion des politiques (Python)
def enforce_policy(user, policy):
    """Logique d’application de politique avancée"""
    return user.id in getattr(policy, 'allowed_users', [])

def audit_policy(policy):
    """Audit avancé de politique"""
    return policy and isinstance(getattr(policy, 'allowed_users', None), list)
