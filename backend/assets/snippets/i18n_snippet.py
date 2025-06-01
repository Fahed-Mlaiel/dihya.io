"""
Dihya Backend Assets – i18n Snippet
Détection et activation dynamique de la langue (fr, en, ar, kab, de, zh, ja, ko, nl, he, fa, hi, es)
"""
def get_preferred_language(headers: dict, default: str = 'fr') -> str:
    accept_lang = headers.get('Accept-Language', default)
    lang = accept_lang.split(',')[0][:2]
    supported = ['fr', 'en', 'ar', 'kab', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es']
    return lang if lang in supported else default

def activate_language(lang: str):
    # Exemple pour Django
    try:
        from django.utils import translation
        translation.activate(lang)
    except ImportError:
        pass  # Pour d'autres frameworks, adapter ici

# Exemple d'utilisation
# headers = {'Accept-Language': 'ar,en;q=0.9'}
# lang = get_preferred_language(headers)
# activate_language(lang)
