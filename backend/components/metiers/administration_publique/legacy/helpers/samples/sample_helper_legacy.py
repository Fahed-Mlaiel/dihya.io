# sample_helper_legacy.py – Exemple ultra avancé helper legacy
def sample_helper_legacy(data):
    if not data:
        return {'helper': True, 'empty': True}
    result = data.copy() if isinstance(data, dict) else {'value': data}
    result['helper'] = True
    return result
