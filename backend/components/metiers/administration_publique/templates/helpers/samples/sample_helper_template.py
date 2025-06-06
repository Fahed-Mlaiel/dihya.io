# sample_helper_template.py – Exemple ultra avancé helper template
def sample_helper_template(data):
    if not data:
        return {'helper': True, 'empty': True}
    result = data.copy() if isinstance(data, dict) else {'value': data}
    result['helper'] = True
    return result
