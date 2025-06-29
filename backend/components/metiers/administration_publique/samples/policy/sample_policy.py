# Exemple avancé de politique (Python)
def enforce_policy(user, policy):
    return user.id in getattr(policy, "allowed_users", [])
