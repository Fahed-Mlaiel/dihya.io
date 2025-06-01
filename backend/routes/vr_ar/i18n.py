"""
Internationalisation dynamique ultra avancée pour VR/AR (Django routes)
Support fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.
"""
from typing import Dict

VR_AR_I18N: Dict[str, Dict[str, str]] = {
    'fr': {'scene': 'Scène', 'asset': 'Asset', 'created': 'Créé', 'deleted': 'Supprimé'},
    'en': {'scene': 'Scene', 'asset': 'Asset', 'created': 'Created', 'deleted': 'Deleted'},
    'ar': {'scene': 'مشهد', 'asset': 'عنصر', 'created': 'تم الإنشاء', 'deleted': 'تم الحذف'},
    'ber': {'scene': 'ⵙⴽⴰⵏⴰ', 'asset': 'ⴰⵙⴰⵏⴻⵔ', 'created': 'ⴰⴷⵔⴰⵙ', 'deleted': 'ⴰⴷⵔⴰⵙ'},
    'de': {'scene': 'Szene', 'asset': 'Asset', 'created': 'Erstellt', 'deleted': 'Gelöscht'},
    'zh': {'scene': '场景', 'asset': '资产', 'created': '已创建', 'deleted': '已删除'},
    'ja': {'scene': 'シーン', 'asset': 'アセット', 'created': '作成済み', 'deleted': '削除済み'},
    'ko': {'scene': '장면', 'asset': '에셋', 'created': '생성됨', 'deleted': '삭제됨'},
    'nl': {'scene': 'Scene', 'asset': 'Asset', 'created': 'Aangemaakt', 'deleted': 'Verwijderd'},
    'he': {'scene': 'סצנה', 'asset': 'נכס', 'created': 'נוצר', 'deleted': 'נמחק'},
    'fa': {'scene': 'صحنه', 'asset': 'دارایی', 'created': 'ایجاد شد', 'deleted': 'حذف شد'},
    'hi': {'scene': 'दृश्य', 'asset': 'संपत्ति', 'created': 'बनाया गया', 'deleted': 'हटाया गया'},
    'es': {'scene': 'Escena', 'asset': 'Recurso', 'created': 'Creado', 'deleted': 'Eliminado'},
}

def translate(term: str, lang: str = 'fr') -> str:
    return VR_AR_I18N.get(lang, VR_AR_I18N['fr']).get(term, term)
