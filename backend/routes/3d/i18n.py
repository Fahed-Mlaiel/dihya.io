"""
Internationalisation dynamique ultra avancée pour 3D (Django routes)
Support fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.
"""
from typing import Dict

THREED_I18N: Dict[str, Dict[str, str]] = {
    'fr': {'project': 'Projet 3D', 'asset': 'Asset 3D', 'created': 'Créé', 'deleted': 'Supprimé'},
    'en': {'project': '3D Project', 'asset': '3D Asset', 'created': 'Created', 'deleted': 'Deleted'},
    'ar': {'project': 'مشروع ثلاثي الأبعاد', 'asset': 'عنصر ثلاثي الأبعاد', 'created': 'تم الإنشاء', 'deleted': 'تم الحذف'},
    'ber': {'project': 'ⴰⵙⴽⴰⵏⴰ 3D', 'asset': 'ⴰⵙⴰⵏⴻⵔ 3D', 'created': 'ⴰⴷⵔⴰⵙ', 'deleted': 'ⴰⴷⵔⴰⵙ'},
    'de': {'project': '3D-Projekt', 'asset': '3D-Asset', 'created': 'Erstellt', 'deleted': 'Gelöscht'},
    'zh': {'project': '三维项目', 'asset': '三维资产', 'created': '已创建', 'deleted': '已删除'},
    'ja': {'project': '3Dプロジェクト', 'asset': '3Dアセット', 'created': '作成済み', 'deleted': '削除済み'},
    'ko': {'project': '3D 프로젝트', 'asset': '3D 에셋', 'created': '생성됨', 'deleted': '삭제됨'},
    'nl': {'project': '3D Project', 'asset': '3D Asset', 'created': 'Aangemaakt', 'deleted': 'Verwijderd'},
    'he': {'project': 'פרויקט תלת מימד', 'asset': 'נכס תלת מימד', 'created': 'נוצר', 'deleted': 'נמחק'},
    'fa': {'project': 'پروژه سه‌بعدی', 'asset': 'دارایی سه‌بعدی', 'created': 'ایجاد شد', 'deleted': 'حذف شد'},
    'hi': {'project': '3डी परियोजना', 'asset': '3डी संपत्ति', 'created': 'बनाया गया', 'deleted': 'हटाया गया'},
    'es': {'project': 'Proyecto 3D', 'asset': 'Recurso 3D', 'created': 'Creado', 'deleted': 'Eliminado'},
}

def translate(term: str, lang: str = 'fr') -> str:
    return THREED_I18N.get(lang, THREED_I18N['fr']).get(term, term)
