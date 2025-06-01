"""
Internationalisation dynamique ultra avancée pour Arts (Django routes)
Support fr, en, ar, tzm, de, zh, ja, ko, nl, he, fa, hi, es.
"""
from typing import Dict

ARTS_I18N: Dict[str, Dict[str, str]] = {
    'fr': {'art': 'Art', 'created': 'Créé', 'deleted': 'Supprimé'},
    'en': {'art': 'Art', 'created': 'Created', 'deleted': 'Deleted'},
    'ar': {'art': 'فن', 'created': 'تم الإنشاء', 'deleted': 'تم الحذف'},
    'tzm': {'art': 'ⴰⵍⵍⴰⵍ', 'created': 'ⴰⴷⵔⴰⵔ', 'deleted': 'ⴰⴷⵔⴰⵔ'},
    'de': {'art': 'Kunst', 'created': 'Erstellt', 'deleted': 'Gelöscht'},
    'zh': {'art': '艺术', 'created': '已创建', 'deleted': '已删除'},
    'ja': {'art': 'アート', 'created': '作成済み', 'deleted': '削除済み'},
    'ko': {'art': '예술', 'created': '생성됨', 'deleted': '삭제됨'},
    'nl': {'art': 'Kunst', 'created': 'Aangemaakt', 'deleted': 'Verwijderd'},
    'he': {'art': 'אמנות', 'created': 'נוצר', 'deleted': 'נמחק'},
    'fa': {'art': 'هنر', 'created': 'ایجاد شد', 'deleted': 'حذف شد'},
    'hi': {'art': 'कला', 'created': 'बनाया गया', 'deleted': 'हटाया गया'},
    'es': {'art': 'Arte', 'created': 'Creado', 'deleted': 'Eliminado'},
}

def translate(term: str, lang: str = 'fr') -> str:
    return ARTS_I18N.get(lang, ARTS_I18N['fr']).get(term, term)
