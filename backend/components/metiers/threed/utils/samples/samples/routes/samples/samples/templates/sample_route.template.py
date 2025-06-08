# sample_route.template.py - Template Python avancé route imbriquée
def sample_route_template(role='user'):
    return {
        'role': role,
        'allowed': role == 'admin' or role == 'user'
    }
