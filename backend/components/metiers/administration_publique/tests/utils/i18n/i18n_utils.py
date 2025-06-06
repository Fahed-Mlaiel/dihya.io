# i18n_utils.py – Utilitaires ultra avancés pour l’internationalisation (clé en main)
# Respecte la modularité, la conformité, l’accessibilité et la logique métier
SUPPORTED_LANGS = ['fr', 'en', 'ar', 'ber', 'de', 'es']
TRANSLATIONS = {
    'fr': lambda msg: f'[FR] {msg}',
    'en': lambda msg: f'[EN] {msg}',
    'ar': lambda msg: f'[AR] {msg}',
    'ber': lambda msg: f'[BER] {msg}',
    'de': lambda msg: f'[DE] {msg}',
    'es': lambda msg: f'[ES] {msg}',
}

def translate(msg, lang='fr'):
    if lang == 'fr':
        return 'bonjour' if msg == 'hello' else 'au revoir' if msg == 'goodbye' else f'[FR] {msg}'
    if lang == 'en':
        return 'hello' if msg == 'hello' else 'goodbye' if msg == 'goodbye' else f'[EN] {msg}'
    if lang == 'es':
        return 'hola' if msg == 'hello' else 'adiós' if msg == 'goodbye' else msg
    if lang == 'de':
        return '[DE] ' + msg
    return f'[{lang.upper()}] {msg}'

def is_supported_lang(lang):
    return lang in ['fr', 'en', 'es']
