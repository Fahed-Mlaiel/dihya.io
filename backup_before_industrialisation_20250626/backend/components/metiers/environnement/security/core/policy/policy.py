# policy.py – Politiques de sécurité avancées


REQUIRED_POLICY_FIELDS = ["id", "title", "rules", "owner"]

def validate_policy(policy: dict) -> bool:
    """
    Valide une politique de sécurité.
    """
    if not isinstance(policy, dict):
        return False
    
    # Vérifier les champs requis
    if not all(field in policy for field in REQUIRED_POLICY_FIELDS):
        return False

    # Vérifier les types des champs requis
    if not isinstance(policy.get("id"), int):
        return False
    if not isinstance(policy.get("title"), str):
        return False
    if not isinstance(policy.get("rules"), list) or not policy.get("rules"): # Doit être une liste non vide
        return False
    if not isinstance(policy.get("owner"), str):
        return False
        
    return True

def enforce_policy(user, action, resource):
    if getattr(user, "is_admin", False):
        return True
    if hasattr(user, "permissions") and action in user.permissions:
        return True
    return False
