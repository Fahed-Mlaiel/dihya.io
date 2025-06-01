"""
Schémas de validation centralisés pour Dihya Coding.

Ce module regroupe les schémas et fonctions de validation utilisés dans tout le backend.
Il permet de garantir la cohérence, la sécurité et la maintenabilité des données échangées via l’API.

Bonnes pratiques :
- Validation stricte des champs (types, présence, formats)
- Extensible pour supporter de nouveaux schémas métiers
- Ne jamais valider ou exposer de secrets ici
- Documenter chaque schéma pour faciliter l’intégration
"""

from typing import Dict, Any

def validate_user(data: Dict[str, Any]) -> bool:
    """
    Valide le schéma d'un utilisateur.
    Champs requis : username (str), email (str), role (str)
    """
    if not isinstance(data, dict):
        raise ValueError("User : données invalides (dict attendu)")
    for field in ("username", "email", "role"):
        if field not in data or not isinstance(data[field], str) or not data[field].strip():
            raise ValueError(f"User : champ '{field}' manquant ou invalide")
    return True

def validate_project(data: Dict[str, Any]) -> bool:
    """
    Valide le schéma d'un projet (voir schemas/project.py pour détails).
    """
    from backend.flask.app.schemas.project import ProjectSchema
    return ProjectSchema.validate(data)

def validate_plugin(data: Dict[str, Any]) -> bool:
    """
    Valide le schéma d'un plugin (voir schemas/plugin.py pour détails).
    """
    from backend.flask.app.schemas.plugin import PluginSchema
    return PluginSchema.validate(data)

def validate_notification(data: Dict[str, Any]) -> bool:
    """
    Valide le schéma d'une notification utilisateur.
    Champs requis : user_id (str), notif_type (str), content (str)
    """
    if not isinstance(data, dict):
        raise ValueError("Notification : données invalides (dict attendu)")
    for field in ("user_id", "notif_type", "content"):
        if field not in data or not isinstance(data[field], str) or not data[field].strip():
            raise ValueError(f"Notification : champ '{field}' manquant ou invalide")
    return True

# Ajouter ici d'autres schémas métiers selon les besoins du backend Dihya Coding.