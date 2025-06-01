"""
Internationalisation dynamique ultra avancée pour Administration Publique
Support fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es.
"""
from typing import Dict

ADMINISTRATION_PUBLIQUE_I18N: Dict[str, Dict[str, str]] = {
    'fr': {'created': 'Projet administration publique créé', 'deleted': 'Projet administration publique supprimé'},
    'en': {'created': 'Public administration project created', 'deleted': 'Public administration project deleted'},
    'ar': {'created': 'تم إنشاء مشروع الإدارة العامة', 'deleted': 'تم حذف مشروع الإدارة العامة'},
    'de': {'created': 'Projekt öffentliche Verwaltung erstellt', 'deleted': 'Projekt öffentliche Verwaltung gelöscht'},
    'zh': {'created': '公共管理项目已创建', 'deleted': '公共管理项目已删除'},
    'ja': {'created': '行政プロジェクトが作成されました', 'deleted': '行政プロジェクトが削除されました'},
    'ko': {'created': '공공 행정 프로젝트 생성됨', 'deleted': '공공 행정 프로젝트 삭제됨'},
    'nl': {'created': 'Project openbare administratie aangemaakt', 'deleted': 'Project openbare administratie verwijderd'},
    'he': {'created': 'פרויקט מנהל ציבורי נוצר', 'deleted': 'פרויקט מנהל ציבורי נמחק'},
    'fa': {'created': 'پروژه مدیریت عمومی ایجاد شد', 'deleted': 'پروژه مدیریت عمومی حذف شد'},
    'hi': {'created': 'सार्वजनिक प्रशासन परियोजना बनाई गई', 'deleted': 'सार्वजनिक प्रशासन परियोजना हटाई गई'},
    'es': {'created': 'Proyecto de administración pública creado', 'deleted': 'Proyecto de administración pública eliminado'},
}

def translate(term: str, lang: str = 'fr') -> str:
    return ADMINISTRATION_PUBLIQUE_I18N.get(lang, ADMINISTRATION_PUBLIQUE_I18N['fr']).get(term, term)
