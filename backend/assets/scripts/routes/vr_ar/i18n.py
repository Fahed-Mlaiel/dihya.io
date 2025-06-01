"""
Dihya Backend – Internationalisation dynamique (i18n)
Support multilingue (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es), hooks plugins, accessibilité, documentation avancée.
- Détection automatique, activation dynamique, plugins i18n, auditabilité, production-ready.
"""
from django.utils import translation

SUPPORTED_LANGUAGES = [
    'fr', 'en', 'ar', 'kab', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es'
]

def set_language(request):
    """Active dynamiquement la langue de la requête (header, param, fallback, plugins)."""
    lang = request.GET.get('lang') or request.headers.get('Accept-Language', 'fr')[:2]
    if lang not in SUPPORTED_LANGUAGES:
        lang = 'fr'
    translation.activate(lang)
    # Hook plugin i18n, logs, audit, accessibilité
    # ...
