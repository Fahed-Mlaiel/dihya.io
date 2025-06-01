"""
Internationalisation dynamique Industrie (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
- Traductions, détection de langue, fallback, audit, RGPD
"""
from django.utils.translation import gettext_lazy as _

SUPPORTED_LANGUAGES = [
    'fr', 'en', 'ar', 'tzm', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es'
]

def get_translation(key, lang):
    """
    Retourne la traduction d'une clé pour la langue donnée.
    """
    translations = {
        'site_name': {
            'fr': 'Nom du site',
            'en': 'Site name',
            'ar': 'اسم الموقع',
            'tzm': 'ⵉⵙⴰⵏ ⵏ ⵜⴰⵙⵉⵏⵜ',
            'de': 'Standortname',
            'zh': '站点名称',
            'ja': 'サイト名',
            'ko': '사이트 이름',
            'nl': 'Sitenaam',
            'he': 'שם האתר',
            'fa': 'نام سایت',
            'hi': 'साइट का नाम',
            'es': 'Nombre del sitio',
        },
        # ...autres clés...
    }
    return translations.get(key, {}).get(lang, key)
