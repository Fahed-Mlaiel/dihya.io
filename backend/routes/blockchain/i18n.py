"""
Internationalisation dynamique ultra avancée pour Blockchain (Django routes)
Support fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.
"""
from typing import Dict

BLOCKCHAIN_I18N: Dict[str, Dict[str, str]] = {
    'fr': {'project': 'Projet Blockchain', 'asset': 'Asset Blockchain', 'created': 'Créé', 'deleted': 'Supprimé'},
    'en': {'project': 'Blockchain Project', 'asset': 'Blockchain Asset', 'created': 'Created', 'deleted': 'Deleted'},
    'ar': {'project': 'مشروع بلوكشين', 'asset': 'عنصر بلوكشين', 'created': 'تم الإنشاء', 'deleted': 'تم الحذف'},
    'ber': {'project': 'ⴰⵙⴽⴰⵏⴰ ⵏ ⴱⵍⵓⴽⵛⵉⵏ', 'asset': 'ⴰⵙⴰⵏⴻⵔ ⵏ ⴱⵍⵓⴽⵛⵉⵏ', 'created': 'ⴰⴷⵔⴰⵙ', 'deleted': 'ⴰⴷⵔⴰⵙ'},
    'de': {'project': 'Blockchain-Projekt', 'asset': 'Blockchain-Asset', 'created': 'Erstellt', 'deleted': 'Gelöscht'},
    'zh': {'project': '区块链项目', 'asset': '区块链资产', 'created': '已创建', 'deleted': '已删除'},
    'ja': {'project': 'ブロックチェーンプロジェクト', 'asset': 'ブロックチェーンアセット', 'created': '作成済み', 'deleted': '削除済み'},
    'ko': {'project': '블록체인 프로젝트', 'asset': '블록체인 에셋', 'created': '생성됨', 'deleted': '삭제됨'},
    'nl': {'project': 'Blockchain Project', 'asset': 'Blockchain Asset', 'created': 'Aangemaakt', 'deleted': 'Verwijderd'},
    'he': {'project': 'פרויקט בלוקצ׳יין', 'asset': 'נכס בלוקצ׳יין', 'created': 'נוצר', 'deleted': 'נמחק'},
    'fa': {'project': 'پروژه بلاکچین', 'asset': 'دارایی بلاکچین', 'created': 'ایجاد شد', 'deleted': 'حذف شد'},
    'hi': {'project': 'ब्लॉकचेन परियोजना', 'asset': 'ब्लॉकचेन संपत्ति', 'created': 'बनाया गया', 'deleted': 'हटाया गया'},
    'es': {'project': 'Proyecto Blockchain', 'asset': 'Recurso Blockchain', 'created': 'Creado', 'deleted': 'Eliminado'},
}

def translate(term: str, lang: str = 'fr') -> str:
    return BLOCKCHAIN_I18N.get(lang, BLOCKCHAIN_I18N['fr']).get(term, term)
