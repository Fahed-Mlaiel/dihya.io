# roles.py – Définition avancée des rôles métier Threed

ROLES = [
    "admin",
    "manager",
    "user",
    "auditor",
]

def is_valid_role(role):
    """Vérifie si le rôle fourni est un rôle métier Threed valide."""
    return role in ROLES

# Convention : tout ajout de rôle doit être documenté et testé dans tests_centralises/security/rbac/roles/test_roles.py
