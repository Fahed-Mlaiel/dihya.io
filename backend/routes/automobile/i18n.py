"""
Internationalisation dynamique ultra avancée pour Automobile (Django routes)
Support fr, en, ar, tzm, de, zh, ja, ko, nl, he, fa, hi, es.
"""

from typing import Dict

AUTOMOBILE_I18N: Dict[str, Dict[str, str]] = {
    'fr': {'created': 'Projet automobile créé', 'deleted': 'Projet automobile supprimé'},
    'en': {'created': 'Automobile project created', 'deleted': 'Automobile project deleted'},
    'ar': {'created': 'تم إنشاء مشروع السيارات', 'deleted': 'تم حذف مشروع السيارات'},
    'tzm': {'created': 'ⴰⴷⵔⴰⵔ ⴰⵎⴰⵙⴳⴰⴹ', 'deleted': 'ⴰⴷⵔⴰⵔ ⴰⵎⴰⵙⴳⴰⴹ'},
    'de': {'created': 'Automobilprojekt erstellt', 'deleted': 'Automobilprojekt gelöscht'},
    'zh': {'created': '汽车项目已创建', 'deleted': '汽车项目已删除'},
    'ja': {'created': '自動車プロジェクト作成済み', 'deleted': '自動車プロジェクト削除済み'},
    'ko': {'created': '자동차 프로젝트 생성됨', 'deleted': '자동차 프로젝트 삭제됨'},
    'nl': {'created': 'Automobielproject aangemaakt', 'deleted': 'Automobielproject verwijderd'},
    'he': {'created': 'פרויקט רכב נוצר', 'deleted': 'פרויקט רכב נמחק'},
    'fa': {'created': 'پروژه خودرو ایجاد شد', 'deleted': 'پروژه خودرو حذف شد'},
    'hi': {'created': 'ऑटोमोबाइल परियोजना बनाई गई', 'deleted': 'ऑटोमोबाइल परियोजना हटाई गई'},
    'es': {'created': 'Proyecto de automóvil creado', 'deleted': 'Proyecto de automóvil eliminado'},
}


def translate(term: str, lang: str = 'fr') -> str:
    return AUTOMOBILE_I18N.get(lang, AUTOMOBILE_I18N['fr']).get(term, term)
