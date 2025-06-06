# rbac_helper.py
"""Helper RBAC (Python)"""
def validate_role(role):
    return isinstance(role, str) and len(role) > 0
