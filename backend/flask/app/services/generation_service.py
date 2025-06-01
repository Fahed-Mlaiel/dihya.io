"""
Service de génération automatique – Dihya Coding

Ce module centralise la logique métier pour générer un projet numérique à partir d’un cahier des charges (texte ou vocal).
Il orchestre l’analyse du besoin, la sélection des stacks, la génération du code, la gestion des plugins, la traçabilité et la sécurité.

Bonnes pratiques :
- Ne jamais exécuter de code non validé ou non sandboxé
- Logger chaque étape pour auditabilité (sans fuite de données sensibles)
- Modulariser la génération (backend, frontend, mobile, IA, DevOps, blockchain)
- Supporter l’extensibilité via plugins et templates
- Gérer les erreurs de façon robuste et sécurisée
- Respecter la conformité RGPD (pas de données sensibles, audit, purge)
"""

import logging
from typing import Dict, Any, Optional, List

# Correction import pour compatibilité Docker et workspace
try:
    from backend.flask.app.core.core import ServiceResponse, get_logger
except ImportError:
    try:
        from app.core.core import ServiceResponse, get_logger
    except ImportError:
        from core.core import ServiceResponse, get_logger

from backend.flask.app.core.validators import is_valid_project_name
from backend.flask.app.schemas.project import ProjectSchema
from backend.flask.app.generation_logs import log_generation_event
from backend.flask.app.plugins.generation_plugin import GenerationPluginBase
from backend.flask.app.plugins.templates.generation_template import GenerationTemplateBase

logger = get_logger("dihya.generation")

class GenerationError(Exception):
    """Exception spécifique à la génération automatique."""
    pass

def analyze_spec(spec: str) -> Dict[str, Any]:
    """
    Analyse le cahier des charges (texte libre) et extrait les besoins du projet.

    Args:
        spec (str): Cahier des charges utilisateur.

    Returns:
        dict: Dictionnaire structuré des besoins (stack, modules, options…).
    """
    # TODO: Intégrer NLP/IA (GPT, fallback open source) pour analyse avancée
    # Pour l’instant, démo simple :
    needs = {
        "project_name": "Projet Dihya",
        "stack": "fullstack",
        "frontend": "react",
        "backend": "flask",
        "mobile": False,
        "ai": False,
        "devops": True,
        "blockchain": False,
        "i18n": True,
        "seo": True,
        "auth": True,
        "roles": ["admin", "user"],
        "plugins": [],
        "template": None
    }
    logger.info("Analyse du cahier des charges terminée.")
    return needs

def generate_project_code(needs: Dict[str, Any]) -> Dict[str, str]:
    """
    Génère le code source du projet selon les besoins analysés.

    Args:
        needs (dict): Besoins structurés du projet.

    Returns:
        dict: Dictionnaire { chemin_fichier: contenu_code }
    """
    # TODO: Appeler les générateurs spécialisés (backend, frontend, etc.)
    # TODO: Utiliser le template métier si précisé
    code = {
        "README.md": f"# {needs['project_name']}\nProjet généré automatiquement.",
        "backend/app.py": "# Flask app auto-générée",
        "frontend/App.js": "// React app auto-générée"
    }
    logger.info("Code du projet généré (démo).")
    return code

def apply_plugins(code: Dict[str, str], plugins: Optional[List[GenerationPluginBase]] = None) -> Dict[str, str]:
    """
    Applique les plugins sélectionnés à la génération du code.

    Args:
        code (dict): Code source généré.
        plugins (list): Liste des plugins à appliquer.

    Returns:
        dict: Code source enrichi par les plugins.
    """
    if not plugins:
        return code
    for plugin in plugins:
        if hasattr(plugin, "after_generation") and plugin.is_safe():
            try:
                code = plugin.after_generation(code, {})
                logger.info(f"Plugin {plugin.name} appliqué avec succès.")
            except Exception as e:
                logger.warning(f"Erreur plugin {plugin.name}: {e}")
    return code

def generate_code_from_template(template, data):
    """Stub: Generiert Code aus Template und Daten."""
    return f"// Code für {template['template']} mit {data}"

def generate_project(spec: str, user_id: Optional[str] = None) -> ServiceResponse:
    """
    Pipeline principal de génération automatique.

    Args:
        spec (str): Cahier des charges utilisateur (texte ou vocal).
        user_id (str, optional): ID utilisateur pour la traçabilité.

    Returns:
        ServiceResponse: Résultat de la génération (succès, code, erreur).
    """
    try:
        logger.info(f"Début de génération pour user={user_id}")
        if not spec or len(spec) < 10:
            return ServiceResponse(False, error="Cahier des charges trop court.")

        needs = analyze_spec(spec)
        if not is_valid_project_name(needs.get("project_name", "")):
            return ServiceResponse(False, error="Nom de projet invalide.")

        code = generate_project_code(needs)
        # Charger dynamiquement les plugins si besoin
        plugins = needs.get("plugins", [])
        code = apply_plugins(code, plugins)

        # Validation finale du schéma projet
        project = ProjectSchema(name=needs["project_name"], files=list(code.keys()))
        log_generation_event(user_id, needs, code)

        logger.info("Génération terminée avec succès.")
        return ServiceResponse(True, data={"project": project, "code": code})
    except Exception as e:
        logger.error(f"Erreur lors de la génération : {e}")
        return ServiceResponse(False, error="Erreur interne lors de la génération.")
