"""
Validateurs ultra avancés pour VR/AR (Django routes)
Validation dynamique, sécurité maximale, RGPD, i18n, audit, plugins, extensible.
Support fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.
"""
from typing import Any, Dict, List, Optional
import re
from .i18n import translate
from .audit import vr_ar_audit_logger

class ValidationError(Exception):
    """Exception personnalisée pour erreurs de validation."""
    def __init__(self, message: str, lang: str = 'fr'):
        super().__init__(translate(message, lang))
        self.lang = lang
        self.message = translate(message, lang)


def validate_scene_data(data: Dict[str, Any], lang: str = 'fr') -> None:
    """
    Valide les données d'une scène VR/AR.
    Args:
        data: Dictionnaire des données de la scène.
        lang: Code langue pour les messages d'erreur.
    Raises:
        ValidationError: Si une validation échoue.
    """
    if not data.get('title') or len(data['title']) < 3:
        raise ValidationError('Le titre est trop court', lang)
    if not data.get('description') or len(data['description']) < 10:
        raise ValidationError('La description est trop courte', lang)
    if data.get('lang') not in translate('scene', lang):
        # On tolère la langue, mais on loggue l'audit
        vr_ar_audit_logger.log('system', 'warn', 'Scene', '-', details=f"Langue inconnue: {data.get('lang')}", language=lang)


def validate_asset_data(data: Dict[str, Any], lang: str = 'fr') -> None:
    """
    Valide les données d'un asset VR/AR.
    Args:
        data: Dictionnaire des données de l'asset.
        lang: Code langue pour les messages d'erreur.
    Raises:
        ValidationError: Si une validation échoue.
    """
    if not data.get('file') or not re.match(r'.+\.(glb|gltf|fbx|obj|mp4|jpg|png)$', data['file'], re.IGNORECASE):
        raise ValidationError('Fichier asset non supporté', lang)
    if not data.get('type') or len(data['type']) < 2:
        raise ValidationError('Type d’asset invalide', lang)
    if data.get('lang') not in translate('asset', lang):
        vr_ar_audit_logger.log('system', 'warn', 'Asset', '-', details=f"Langue inconnue: {data.get('lang')}", language=lang)

# RGPD : anonymisation simple (exemple)
def anonymize_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Anonymise les données sensibles pour conformité RGPD.
    Args:
        data: Dictionnaire à anonymiser.
    Returns:
        Dictionnaire anonymisé.
    """
    anonymized = data.copy()
    if 'created_by' in anonymized:
        anonymized['created_by'] = 'anonymized'
    if 'file' in anonymized:
        anonymized['file'] = 'anonymized_file'
    return anonymized

# Extensible : ajout de validateurs via plugins
def register_validator(name: str, func):
    """
    Permet d’ajouter dynamiquement un validateur métier via plugin/API.
    """
    globals()[f'validate_{name}'] = func
