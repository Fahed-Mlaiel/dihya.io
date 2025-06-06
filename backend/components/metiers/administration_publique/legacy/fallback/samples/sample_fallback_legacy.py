# sample_fallback_legacy.py – Exemple ultra avancé fallback legacy
def sample_fallback_legacy(data):
    if not data:
        return {'fallback': True, 'empty': True}
    result = data.copy() if isinstance(data, dict) else {'value': data}
    result['fallback'] = True
    return result
