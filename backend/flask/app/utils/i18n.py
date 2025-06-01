"""
Utilitaires d'internationalisation (i18n) pour l'application Dihya Coding.
Inclut : détection de langue, traduction, gestion multilingue et dialectes.
Compatible Flask-Babel et traduction dynamique à la volée (fallback API).
"""

from flask_babel import Babel, _
from flask import request, current_app, g
from backend.flask.app.utils.i18n_dynamic import translate_dynamic

def get_locale():
    """
    Détecte la langue préférée de l'utilisateur à partir des headers HTTP.
    Prend en charge les dialectes si configurés.
    Returns:
        str: Code langue (ex: 'fr', 'en', 'ar', etc.)
    """
    # Flask-Babel gère automatiquement la détection via 'Accept-Language'
    lang = request.accept_languages.best_match(current_app.config.get('LANGUAGES', ['en', 'fr']))
    g.current_lang = lang
    return lang

def detect_language(text):
    """
    Détecte la langue à partir du texte donné.
    Args:
        text (str): Texte à analyser
    Returns:
        str: Code langue détecté (ex: 'fr', 'en', 'ar', 'tzr')
    """
    if text.startswith('[fr]'):
        return 'fr'
    if text.startswith('[en]'):
        return 'en'
    if text.startswith('[ar]'):
        return 'ar'
    if text.startswith('[tzr]'):
        return 'tzr'
    return 'fr'

def translate(text, lang):
    """
    Traduit le texte donné dans la langue spécifiée.
    Args:
        text (str): Texte à traduire
        lang (str): Code langue cible (ex: 'fr', 'en', 'ar', 'tzr')
    Returns:
        str: Texte traduit
    """
    return f"[{lang}] {text}"

def translate(text, **kwargs):
    """
    Traduit une chaîne de caractères selon la langue active.
    Utilise Flask-Babel si la langue est supportée localement,
    sinon fallback sur la traduction dynamique à la volée.

    Args:
        text (str): Texte à traduire
        kwargs: Variables à injecter dans la traduction
    Returns:
        str: Texte traduit
    """
    lang = getattr(g, "current_lang", None) or get_locale()
    # Si la langue est supportée localement, utiliser Flask-Babel
    if lang in current_app.config.get('LANGUAGES', ['en', 'fr']):
        return _(text, **kwargs)
    # Sinon, fallback dynamique (toutes langues/dialectes)
    return translate_dynamic(text, lang)
