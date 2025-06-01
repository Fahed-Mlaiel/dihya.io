"""
Schéma de validation pour les projets générés par Dihya Coding.

Ce module définit la structure et la validation des projets (frontend, backend, mobile, etc.).
Il garantit que chaque projet respecte les contraintes de sécurité, d’extensibilité, de documentation et de souveraineté numérique.

Bonnes pratiques :
- Validation stricte des champs (nom, stack, modules, owner, config)
- Prévoir l’extensibilité (modules dynamiques, plugins, i18n, etc.)
- Ne jamais stocker de secrets dans la config du projet
- Documenter chaque champ pour faciliter l’intégration et l’audit
- Logger les erreurs de validation pour auditabilité (sans fuite de données sensibles)
"""

from typing import Dict, Any, List, Optional
import logging

logger = logging.getLogger("dihya.schemas.project")

class ProjectSchema:
    """
    Schéma de projet pour Dihya Coding.

    Champs requis :
        - name (str) : Nom du projet
        - owner (str) : Identifiant du propriétaire
        - stack (list[str]) : Technologies utilisées
        - modules (list[dict]) : Modules du projet (backend, frontend, etc.)
        - created_at (str) : Date de création ISO8601

    Champs optionnels :
        - config (dict) : Configuration additionnelle (jamais de secrets)
        - plugins (list) : Plugins activés
        - i18n (dict) : Localisation
        - docs (str) : Documentation projet
    """
    REQUIRED_FIELDS = {"name", "owner", "stack", "modules", "created_at"}

    @staticmethod
    def validate(data: Dict[str, Any]) -> bool:
        """
        Valide la structure et le contenu d’un projet Dihya.

        Args:
            data (dict): Données du projet à valider.

        Returns:
            bool: True si valide, lève une exception sinon.

        Raises:
            ValueError: Si un champ est manquant ou invalide.
        """
        if not isinstance(data, dict):
            logger.error("Projet : données invalides (dict attendu)")
            raise ValueError("Projet : données invalides (dict attendu)")
        missing = ProjectSchema.REQUIRED_FIELDS - set(data.keys())
        if missing:
            logger.error(f"Projet : champs manquants {missing}")
            raise ValueError(f"Projet : champs manquants {missing}")
        if not isinstance(data["name"], str) or not data["name"].strip():
            logger.error("Projet : nom manquant ou invalide")
            raise ValueError("Projet : nom manquant ou invalide")
        if not isinstance(data["owner"], str) or not data["owner"].strip():
            logger.error("Projet : owner manquant ou invalide")
            raise ValueError("Projet : owner manquant ou invalide")
        if not isinstance(data["stack"], list) or not all(isinstance(s, str) for s in data["stack"]):
            logger.error("Projet : stack doit être une liste de chaînes")
            raise ValueError("Projet : stack doit être une liste de chaînes")
        if not isinstance(data["modules"], list) or not all(isinstance(m, dict) for m in data["modules"]):
            logger.error("Projet : modules doit être une liste de dictionnaires")
            raise ValueError("Projet : modules doit être une liste de dictionnaires")
        if not isinstance(data["created_at"], str) or not data["created_at"]:
            logger.error("Projet : created_at manquant ou invalide")
            raise ValueError("Projet : created_at manquant ou invalide")
        # Optionnel : config
        if "config" in data and not isinstance(data["config"], dict):
            logger.error("Projet : config doit être un dictionnaire si présent")
            raise ValueError("Projet : config doit être un dictionnaire si présent")
        # Optionnel : plugins
        if "plugins" in data and not isinstance(data["plugins"], list):
            logger.error("Projet : plugins doit être une liste si présent")
            raise ValueError("Projet : plugins doit être une liste si présent")
        # Sécurité : pas de secrets dans la config
        if "config" in data:
            for key in data["config"]:
                if "secret" in key.lower() or "password" in key.lower():
                    logger.error("Projet : la config ne doit pas contenir de secrets")
                    raise ValueError("Projet : la config ne doit pas contenir de secrets")
        # Optionnel : i18n
        if "i18n" in data and not isinstance(data["i18n"], dict):
            logger.error("Projet : i18n doit être un dictionnaire si présent")
            raise ValueError("Projet : i18n doit être un dictionnaire si présent")
        # Optionnel : docs
        if "docs" in data and not (isinstance(data["docs"], str) or data["docs"] is None):
            logger.error("Projet : docs doit être une chaîne ou None")
            raise ValueError("Projet : docs doit être une chaîne ou None")
        return True

    @staticmethod
    def default(owner: str = "user_id") -> Dict[str, Any]:
        """
        Retourne un projet par défaut conforme au schéma.

        Args:
            owner (str): Identifiant du propriétaire.

        Returns:
            dict: Projet par défaut.
        """
        return {
            "name": "Mon Projet Dihya",
            "owner": owner,
            "stack": ["react", "flask"],
            "modules": [],
            "created_at": "2025-01-01T00:00:00Z",
            "config": {},
            "plugins": [],
            "i18n": {},
            "docs": ""
        }