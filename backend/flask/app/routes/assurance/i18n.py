"""
Internationalisation dynamique ultra avancée pour Assurance
Support fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es.
"""
from typing import Dict
ASSURANCE_I18N: Dict[str, Dict[str, str]] = {
    'fr': {'created': 'Contrat assurance créé', 'deleted': 'Contrat assurance supprimé'},
    'en': {'created': 'Insurance contract created', 'deleted': 'Insurance contract deleted'},
    'ar': {'created': 'تم إنشاء عقد تأمين', 'deleted': 'تم حذف عقد تأمين'},
    'de': {'created': 'Versicherungsvertrag erstellt', 'deleted': 'Versicherungsvertrag gelöscht'},
    'zh': {'created': '保险合同已创建', 'deleted': '保险合同已删除'},
    'ja': {'created': '保険契約が作成されました', 'deleted': '保険契約が削除されました'},
    'ko': {'created': '보험 계약 생성됨', 'deleted': '보험 계약 삭제됨'},
    'nl': {'created': 'Verzekeringscontract aangemaakt', 'deleted': 'Verzekeringscontract verwijderd'},
    'he': {'created': 'חוזה ביטוח נוצר', 'deleted': 'חוזה ביטוח נמחק'},
    'fa': {'created': 'قرارداد بیمه ایجاد شد', 'deleted': 'قرارداد بیمه حذف شد'},
    'hi': {'created': 'बीमा अनुबंध बनाया गया', 'deleted': 'बीमा अनुबंध हटाया गया'},
    'es': {'created': 'Contrato de seguro creado', 'deleted': 'Contrato de seguro eliminado'},
}
def translate(term: str, lang: str = 'fr') -> str:
    return ASSURANCE_I18N.get(lang, ASSURANCE_I18N['fr']).get(term, term)
