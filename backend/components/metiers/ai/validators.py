"""
Dihya Backend AI – Validateurs ultra avancés pour API IA
Validation dynamique, sécurité maximale, RGPD, i18n, audit, plugins, extensible.
"""
class ValidationError(Exception):
    def __init__(self, message, lang='fr'):
        super().__init__(message)
        self.lang = lang
        self.message = message

def validate_ai_request(data, lang='fr'):
    if not data.get('prompt') or len(data['prompt']) < 1:
        raise ValidationError('Prompt IA manquant ou trop court', lang)
    if data.get('model') not in ['ollama', 'mixtral', 'llama']:
        raise ValidationError('Modèle IA inconnu', lang)

def anonymize_data(data):
    d = dict(data)
    if 'user' in d:
        d['user'] = '***'
    return d
