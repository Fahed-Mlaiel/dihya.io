# Validateurs pour Agriculture

def validate_culture(data):
    if not data.get('nom'):
        raise ValueError('Nom requis')
    return True

def validate_multilingue(data):
    langs = ['fr', 'en', 'ar', 'tzm']
    for l in langs:
        if not data.get('nom', {}).get(l):
            raise ValueError(f'Nom manquant pour {l}')
    return True
