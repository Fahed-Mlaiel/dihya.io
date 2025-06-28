# roles.py – Définition avancée des rôles métier A_I

ROLES = [
    "admin",
    "manager",
    "user",
    "auditor",
]

def is_valid_role(role):
    """Vérifie si le rôle fourni est un rôle métier A_I valide."""
    return role in ROLES

# Convention : tout ajout de rôle doit être documenté et testé dans tests_centralises/security/rbac/roles/test_roles.py
