"""
Schéma de validation pour les plugins Dihya Coding.

Ce module définit la structure et la validation des plugins personnalisés.
Il garantit que chaque plugin respecte les contraintes de sécurité, d’extensibilité et de documentation.

Bonnes pratiques :
- Validation stricte des champs (nom, version, config, hooks)
- Prévoir l’extensibilité (paramètres dynamiques, hooks, etc.)
- Ne jamais stocker de secrets dans la config du plugin
- Documenter chaque champ pour faciliter l’intégration
"""

from typing import Dict, Any

class PluginSchema:
    """
    Schéma de plugin pour Dihya Coding.
    """
    REQUIRED_FIELDS = {"name", "version", "enabled", "config"}

    @staticmethod
    def validate(data: Dict[str, Any]) -> bool:
        if not isinstance(data, dict):
            raise ValueError("Plugin : données invalides (dict attendu)")
        missing = PluginSchema.REQUIRED_FIELDS - set(data.keys())
        if missing:
            raise ValueError(f"Plugin : champs manquants {missing}")
        if not isinstance(data["name"], str) or not data["name"].strip():
            raise ValueError("Plugin : nom manquant ou invalide")
        if not isinstance(data["version"], str) or not data["version"].strip():
            raise ValueError("Plugin : version manquante ou invalide")
        if not isinstance(data["enabled"], bool):
            raise ValueError("Plugin : champ 'enabled' invalide")
        if not isinstance(data["config"], dict):
            raise ValueError("Plugin : config doit être un dictionnaire")
        # Optionnel : hooks
        if "hooks" in data and not isinstance(data["hooks"], dict):
            raise ValueError("Plugin : hooks doit être un dictionnaire si présent")
        # Sécurité : pas de secrets dans la config
        for key in data["config"]:
            if "secret" in key.lower():
                raise ValueError("Plugin : la config ne doit pas contenir de secrets")
        return True

    @staticmethod
    def default():
        return {
            "name": "example_plugin",
            "version": "1.0.0",
            "enabled": True,
            "config": {},
            "hooks": {}
        }