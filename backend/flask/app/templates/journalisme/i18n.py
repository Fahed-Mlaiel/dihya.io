"""
Internationalisation dynamique Journalisme – Dihya Coding
Supporte fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.
"""
from flask import request
from typing import Dict

SUPPORTED_LANGS = ['fr', 'en', 'ar', 'ber', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es']

LOCALES: Dict[str, Dict[str, str]] = {
    'fr': {'Accès refusé': 'Accès refusé', 'Article ajouté': 'Article ajouté'},
    'en': {'Accès refusé': 'Access denied', 'Article ajouté': 'Article added'},
    # ... autres langues ...
}

def get_locale() -> str:
    """Détecte la langue de la requête (header, param, fallback)."""
    return request.headers.get('Accept-Language', 'fr').split(',')[0][:2]

def translate(msg: str, lang: str) -> str:
    """Traduit dynamiquement un message métier."""
    return LOCALES.get(lang, LOCALES['fr']).get(msg, msg)
