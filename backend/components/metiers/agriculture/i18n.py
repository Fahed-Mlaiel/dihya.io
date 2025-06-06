# Internationalisation pour Agriculture

TRANSLATIONS = {
    'fr': {
        'bienvenue': 'Bienvenue dans Agriculture'
    },
    'en': {
        'bienvenue': 'Welcome to Agriculture'
    },
    'ar': {
        'bienvenue': 'مرحبا بكم في الزراعة'
    },
    'tzm': {
        'bienvenue': 'ⴰⵏⴰⵡⴰⵢ ⴷ ⴰⴳⵔⵉⴳⵓⵍ'
    }
}

def translate(key, lang='fr'):
    return TRANSLATIONS.get(lang, TRANSLATIONS['fr']).get(key, key)
