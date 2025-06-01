"""
Internationalisation dynamique ultra avancée pour Assurance (Dihya)
Support fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.
"""
from typing import Dict

ASSURANCE_I18N: Dict[str, Dict[str, str]] = {
    'fr': {'project': 'Projet Assurance', 'asset': 'Document', 'created': 'Créé', 'deleted': 'Supprimé'},
    'en': {'project': 'Insurance Project', 'asset': 'Document', 'created': 'Created', 'deleted': 'Deleted'},
    'ar': {'project': 'مشروع تأمين', 'asset': 'وثيقة', 'created': 'تم الإنشاء', 'deleted': 'تم الحذف'},
    'ber': {'project': 'ⴰⵙⵙⵓⵏⴰⵏ ⴰⵙⵓⵏⴰⵏ', 'asset': 'ⴰⵙⴰⵏⴻⵔ', 'created': 'ⴰⴷⵔⴰⵙ', 'deleted': 'ⴰⴷⵔⴰⵙ'},
    'de': {'project': 'Versicherungsprojekt', 'asset': 'Dokument', 'created': 'Erstellt', 'deleted': 'Gelöscht'},
    'zh': {'project': '保险项目', 'asset': '文件', 'created': '已创建', 'deleted': '已删除'},
    'ja': {'project': '保険プロジェクト', 'asset': 'ドキュメント', 'created': '作成済み', 'deleted': '削除済み'},
    'ko': {'project': '보험 프로젝트', 'asset': '문서', 'created': '생성됨', 'deleted': '삭제됨'},
    'nl': {'project': 'Verzekeringsproject', 'asset': 'Document', 'created': 'Aangemaakt', 'deleted': 'Verwijderd'},
    'he': {'project': 'פרויקט ביטוח', 'asset': 'מסמך', 'created': 'נוצר', 'deleted': 'נמחק'},
    'fa': {'project': 'پروژه بیمه', 'asset': 'سند', 'created': 'ایجاد شد', 'deleted': 'حذف شد'},
    'hi': {'project': 'बीमा परियोजना', 'asset': 'दस्तावेज़', 'created': 'बनाया गया', 'deleted': 'हटाया गया'},
    'es': {'project': 'Proyecto de Seguro', 'asset': 'Documento', 'created': 'Creado', 'deleted': 'Eliminado'},
}

def translate(term: str, lang: str = 'fr') -> str:
    return ASSURANCE_I18N.get(lang, ASSURANCE_I18N['fr']).get(term, term)
