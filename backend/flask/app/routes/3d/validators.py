"""
Validateurs ultra avancés pour 3D
Validation dynamique, sécurité maximale, RGPD, i18n, audit, plugins, extensible.
Support fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.
"""
from typing import Any, Dict
import re
from .i18n import translate
from .audit import threed_audit_logger

class ValidationError(Exception):
    """Exception personnalisée pour erreurs de validation."""
    def __init__(self, message: str, lang: str = 'fr'):
        super().__init__(translate(message, lang))
        self.lang = lang
        self.message = translate(message, lang)

def validate_threedproject_data(data: Dict[str, Any], lang: str = 'fr') -> None:
    """
    Valide les données d'un projet 3D.
    Args:
        data: Dictionnaire des données du projet 3D.
        lang: Code langue pour les messages d'erreur.
    Raises:
        ValidationError: Si une validation échoue.
    """
    if not data.get('name') or len(data['name']) < 3:
        raise ValidationError('Le nom du projet est trop court', lang)
    if not data.get('description') or len(data['description']) < 10:
        raise ValidationError('La description est trop courte', lang)
    if data.get('lang') not in translate('project', lang):
        threed_audit_logger.log('system', 'warn', 'ThreeDProject', '-', details=f"Langue inconnue: {data.get('lang')}", language=lang)

def validate_threedasset_data(data: Dict[str, Any], lang: str = 'fr') -> None:
    """
    Valide les données d'un asset 3D.
    Args:
        data: Dictionnaire des données de l'asset 3D.
        lang: Code langue pour les messages d'erreur.
    Raises:
        ValidationError: Si une validation échoue.
    """
    if not data.get('file') or not re.match(r'.+\.(glb|gltf|fbx|obj|mp4|jpg|png)$', data['file'], re.IGNORECASE):
        raise ValidationError('Fichier asset 3D non supporté', lang)
    if not data.get('type') or len(data['type']) < 2:
        raise ValidationError('Type d’asset 3D invalide', lang)
    if data.get('lang') not in translate('asset', lang):
        threed_audit_logger.log('system', 'warn', 'ThreeDAsset', '-', details=f"Langue inconnue: {data.get('lang')}", language=lang)

def anonymize_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Anonymise les données sensibles pour conformité RGPD.
    Args:
        data: Dictionnaire à anonymiser.
    Returns:
        Dictionnaire anonymisé.
    """
    anonymized = data.copy()
    if 'file' in anonymized:
        anonymized['file'] = 'anonymized'
    return anonymized
