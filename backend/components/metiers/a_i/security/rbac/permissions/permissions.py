# permissions.py – Définition avancée des permissions métier A_I

PERMISSIONS = [
    "read",
    "write",
    "delete",
    "audit",
]

def is_valid_permission(permission):
    """Vérifie si la permission fournie est une permission métier A_I valide."""
    return permission in PERMISSIONS

# Convention : tout ajout de permission doit être documenté et testé dans tests_centralises/security/rbac/permissions/test_permissions.py
