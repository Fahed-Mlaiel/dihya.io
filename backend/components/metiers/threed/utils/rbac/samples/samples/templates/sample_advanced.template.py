# sample_advanced.template.py - Template Python avancé RBAC
def sample_advanced_template(role='user'):
    return {
        'role': role,
        'allowed': role == 'admin' or role == 'user'
    }
