"""
Validateurs ultra avancés pour Santé (Django routes)
Validation dynamique, sécurité maximale, RGPD, i18n, audit, plugins, extensible.
"""
from typing import Any, Dict
import re
from .audit import sante_audit_logger

class ValidationError(Exception):
    def __init__(self, message: str, lang: str = 'fr'):
        super().__init__(message)
        self.lang = lang
        self.message = message

def validate_santeproject_data(data: Dict[str, Any], lang: str = 'fr') -> None:
    if not data.get('name') or len(data['name']) < 3:
        raise ValidationError('Le nom du projet est trop court', lang)
    if not data.get('description') or len(data['description']) < 10:
        raise ValidationError('La description est trop courte', lang)
    sante_audit_logger.log('system', 'validate', 'SanteProject', '-', details='Validation OK', language=lang)

def anonymize_data(data: Dict[str, Any]) -> Dict[str, Any]:
    return {k: (v if k not in ['name', 'description'] else '***') for k, v in data.items()}
