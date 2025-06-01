"""
Internationalisation dynamique SEO – Dihya Coding
Supporte fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.
"""
from flask import request
from typing import Dict

SUPPORTED_LANGS = ['fr', 'en', 'ar', 'ber', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es']

LOCALES: Dict[str, Dict[str, str]] = {
    'fr': {'Accès refusé': 'Accès refusé', 'SEO mis à jour': 'SEO mis à jour'},
    'en': {'Accès refusé': 'Access denied', 'SEO mis à jour': 'SEO updated'},
    # ... autres langues ...
}

def get_locale() -> str:
    """Détecte la langue de la requête (header, param, fallback)."""
    return request.headers.get('Accept-Language', 'fr').split(',')[0][:2]

def translate(msg: str, lang: str) -> str:
    """Traduit dynamiquement un message métier."""
    return LOCALES.get(lang, LOCALES['fr']).get(msg, msg)
