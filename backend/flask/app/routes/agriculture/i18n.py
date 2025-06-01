"""
Internationalisation dynamique ultra avancée pour Agriculture
Support fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es.
"""
from typing import Dict
AGRICULTURE_I18N: Dict[str, Dict[str, str]] = {
    'fr': {'created': 'Projet agriculture créé', 'deleted': 'Projet agriculture supprimé'},
    'en': {'created': 'Agriculture project created', 'deleted': 'Agriculture project deleted'},
    'ar': {'created': 'تم إنشاء مشروع زراعي', 'deleted': 'تم حذف مشروع زراعي'},
    'de': {'created': 'Agrarprojekt erstellt', 'deleted': 'Agrarprojekt gelöscht'},
    'zh': {'created': '农业项目已创建', 'deleted': '农业项目已删除'},
    'ja': {'created': '農業プロジェクトが作成されました', 'deleted': '農業プロジェクトが削除されました'},
    'ko': {'created': '농업 프로젝트 생성됨', 'deleted': '농업 프로젝트 삭제됨'},
    'nl': {'created': 'Landbouwproject aangemaakt', 'deleted': 'Landbouwproject verwijderd'},
    'he': {'created': 'פרויקט חקלאות נוצר', 'deleted': 'פרויקט חקלאות נמחק'},
    'fa': {'created': 'پروژه کشاورزی ایجاد شد', 'deleted': 'پروژه کشاورزی حذف شد'},
    'hi': {'created': 'कृषि परियोजना बनाई गई', 'deleted': 'कृषि परियोजना हटाई गई'},
    'es': {'created': 'Proyecto de agricultura creado', 'deleted': 'Proyecto de agricultura eliminado'},
}
def translate(term: str, lang: str = 'fr') -> str:
    return AGRICULTURE_I18N.get(lang, AGRICULTURE_I18N['fr']).get(term, term)
