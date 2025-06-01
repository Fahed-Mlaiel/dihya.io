"""
Gestion i18n dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
"""
MESSAGES = {
    'welcome': {
        'fr': 'Bienvenue sur Dihya Coding !',
        'en': 'Welcome to Dihya Coding!',
        'ar': 'مرحبًا بك في ديهيا كودينغ!',
        'amz': 'ⴰⵏⴰⴷⴷⴰⵙ ⴷ Dihya Coding!',
        'de': 'Willkommen bei Dihya Coding!',
        'zh': '欢迎使用Dihya Coding!',
        'ja': 'Dihya Codingへようこそ!',
        'ko': 'Dihya Coding에 오신 것을 환영합니다!',
        'nl': 'Welkom bij Dihya Coding!',
        'he': 'ברוך הבא ל-Dihya Coding!',
        'fa': 'به Dihya Coding خوش آمدید!',
        'hi': 'Dihya Coding में आपका स्वागत है!',
        'es': '¡Bienvenido a Dihya Coding!'
    }
}
def get_message(key, lang):
    return MESSAGES.get(key, {}).get(lang, MESSAGES.get(key, {}).get('en', ''))
