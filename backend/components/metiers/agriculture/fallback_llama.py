# Fallback Llama pour Agriculture – Ultra avancé

def fallback_llama(input_text, lang='fr'):
    """Fallback IA open source multilingue"""
    responses = {
        'fr': 'Réponse fallback Llama',
        'en': 'Llama fallback response',
        'ar': 'استجابة لاما الاحتياطية',
        'tzm': 'ⵉⴷⴷⴰⵔ ⵏ ⵍⵍⴰⵎⴰ'
    }
    return responses.get(lang, responses['fr'])
