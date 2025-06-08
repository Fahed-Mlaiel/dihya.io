# rbac_templates.py - Templates métier RBAC (Python)
def rbac_template(role='user'):
    if role == 'admin':
        return { 'permissions': ['read', 'write', 'delete'] }
    elif role == 'user':
        return { 'permissions': ['read'] }
    return { 'permissions': [] }
