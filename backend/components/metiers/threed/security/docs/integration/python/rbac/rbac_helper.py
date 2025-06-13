# rbac_helper.py – Helper Python pour gestion RBAC
def check_role(user, role):
    return role in getattr(user, "roles", [])
