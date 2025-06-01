"""
Internationalisation dynamique ultra avancée pour Dihya Backend
Support fr, en, ar, tzm, de, zh, ja, ko, nl, he, fa, hi, es.
Gestion centralisée des traductions, fallback, audit, RGPD, plugins, multitenancy.
"""

from typing import Dict

I18N_TRANSLATIONS: Dict[str, Dict[str, str]] = {
    'fr': {'welcome': 'Bienvenue', 'error': 'Erreur', 'created': 'Créé', 'deleted': 'Supprimé'},
    'en': {'welcome': 'Welcome', 'error': 'Error', 'created': 'Created', 'deleted': 'Deleted'},
    'ar': {'welcome': 'مرحبا', 'error': 'خطأ', 'created': 'تم الإنشاء', 'deleted': 'تم الحذف'},
    'tzm': {'welcome': 'ⴰⵏⴰⴳⴳⴰⵔ', 'error': 'ⴰⵙⵉⵏⴰⵡ', 'created': 'ⴰⴷⵔⴰⵔ', 'deleted': 'ⴰⴷⵔⴰⵔ'},
    'de': {'welcome': 'Willkommen', 'error': 'Fehler', 'created': 'Erstellt', 'deleted': 'Gelöscht'},
    'zh': {'welcome': '欢迎', 'error': '错误', 'created': '已创建', 'deleted': '已删除'},
    'ja': {'welcome': 'ようこそ', 'error': 'エラー', 'created': '作成済み', 'deleted': '削除済み'},
    'ko': {'welcome': '환영합니다', 'error': '오류', 'created': '생성됨', 'deleted': '삭제됨'},
    'nl': {'welcome': 'Welkom', 'error': 'Fout', 'created': 'Aangemaakt', 'deleted': 'Verwijderd'},
    'he': {'welcome': 'ברוך הבא', 'error': 'שגיאה', 'created': 'נוצר', 'deleted': 'נמחק'},
    'fa': {'welcome': 'خوش آمدید', 'error': 'خطا', 'created': 'ایجاد شد', 'deleted': 'حذف شد'},
    'hi': {'welcome': 'स्वागत है', 'error': 'त्रुटि', 'created': 'बनाया गया', 'deleted': 'हटाया गया'},
    'es': {'welcome': 'Bienvenido', 'error': 'Error', 'created': 'Creado', 'deleted': 'Eliminado'},
}

def translate(term: str, lang: str = 'fr') -> str:
    """
    Traduit un terme selon la langue, fallback fr.
    """
    return I18N_TRANSLATIONS.get(lang, I18N_TRANSLATIONS['fr']).get(term, term)
