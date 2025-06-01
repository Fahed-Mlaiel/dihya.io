"""
Dihya Backend AI – Internationalisation dynamique ultra avancée
Support fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.
"""
from typing import Dict

AI_I18N: Dict[str, Dict[str, str]] = {
    'fr': {'ai': 'Intelligence Artificielle', 'generate': 'Générer', 'error': 'Erreur'},
    'en': {'ai': 'Artificial Intelligence', 'generate': 'Generate', 'error': 'Error'},
    'ar': {'ai': 'الذكاء الاصطناعي', 'generate': 'توليد', 'error': 'خطأ'},
    'tzr': {'ai': 'ⵉⵏⵜⴰⵍⵍⵉⴰⵏⴻ ⴰⵙⵉⵏⴰⵡⴰⵏ', 'generate': 'ⴰⴷⵔⴰⵙ', 'error': 'ⴰⴷⵔⴰⵙ'},
    'de': {'ai': 'Künstliche Intelligenz', 'generate': 'Generieren', 'error': 'Fehler'},
    'zh': {'ai': '人工智能', 'generate': '生成', 'error': '错误'},
    'ja': {'ai': '人工知能', 'generate': '生成', 'error': 'エラー'},
    'ko': {'ai': '인공지능', 'generate': '생성', 'error': '오류'},
    'nl': {'ai': 'Kunstmatige intelligentie', 'generate': 'Genereren', 'error': 'Fout'},
    'he': {'ai': 'בינה מלאכותית', 'generate': 'לְהוֹלִיד', 'error': 'שְׁגִיאָה'},
    'fa': {'ai': 'هوش مصنوعی', 'generate': 'تولید', 'error': 'خطا'},
    'hi': {'ai': 'कृत्रिम बुद्धिमत्ता', 'generate': 'उत्पन्न करें', 'error': 'त्रुटि'},
    'es': {'ai': 'Inteligencia Artificial', 'generate': 'Generar', 'error': 'Error'},
}

def translate(term: str, lang: str = 'fr') -> str:
    return AI_I18N.get(lang, AI_I18N['fr']).get(term, term)
