# __init__.py – Initialisation du module i18n (Python)

from .i18n_utils import translate, is_supported_lang, SUPPORTED_LANGS

def i18n(msg, lang):
    return translate(msg, lang)
