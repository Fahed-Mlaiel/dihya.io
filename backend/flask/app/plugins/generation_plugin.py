"""
Plugin de génération – Dihya Coding

Ce module définit la structure de base pour les plugins de génération automatique.
Les plugins permettent d’étendre ou de personnaliser la génération (ajout de fonctionnalités, templates, hooks…).

Bonnes pratiques :
- Chaque plugin doit hériter de GenerationPluginBase
- Ne jamais exécuter de code non validé ou non sandboxé
- Documenter chaque plugin et ses hooks
- Logger les actions pour auditabilité (sans fuite de données sensibles)
- Prévoir la conformité RGPD (pas de données sensibles, audit, purge)
- Prévoir l’extensibilité (ajout facile de nouveaux plugins)
"""

from typing import Dict, Any
import logging

class GenerationPluginBase:
    """
    Classe de base pour tous les plugins de génération Dihya Coding.

    Méthodes à surcharger :
        - before_generation : pour modifier les besoins avant génération
        - after_generation : pour enrichir le code généré

    Bonnes pratiques :
        - Documenter chaque plugin (usage, hooks, options)
        - Logger les actions importantes (sans données sensibles)
        - Ne jamais exécuter de code non validé ou non sandboxé
        - Respecter la conformité RGPD (pas de fuite de données)
    """

    name = "BasePlugin"
    description = "Plugin de base pour la génération automatique."
    version = "1.0.0"
    author = "Dihya Coding"
    safe = True  # Indique si le plugin est validé/sandboxé

    def before_generation(self, needs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Hook appelé avant la génération du code.

        Args:
            needs (dict): Besoins du projet.

        Returns:
            dict: Besoins éventuellement modifiés.
        """
        logging.info(f"[Plugin:{self.name}] before_generation appelé.")
        return needs

    def after_generation(self, code: Dict[str, str], needs: Dict[str, Any]) -> Dict[str, str]:
        """
        Hook appelé après la génération du code.

        Args:
            code (dict): Code source généré.
            needs (dict): Besoins du projet.

        Returns:
            dict: Code source éventuellement enrichi.
        """
        logging.info(f"[Plugin:{self.name}] after_generation appelé.")
        return code

    def get_metadata(self) -> Dict[str, Any]:
        """
        Retourne les métadonnées du plugin (pour auditabilité et documentation).

        Returns:
            dict: Métadonnées du plugin.
        """
        return {
            "name": self.name,
            "description": self.description,
            "version": self.version,
            "author": self.author,
            "safe": self.safe
        }

    def is_safe(self) -> bool:
        """
        Indique si le plugin est validé/sandboxé (pour activation automatique).

        Returns:
            bool: True si le plugin est considéré comme sûr.
        """
        return self.safe

# Exemple de plugin custom (à placer dans plugins/custom_plugin.py)
# from .generation_plugin import GenerationPluginBase
#
# class AnalyticsPlugin(GenerationPluginBase):
#     name = "Analytics"
#     description = "Ajoute un tracking analytics au frontend."
#
#     def after_generation(self, code, needs):
#         if "frontend/App.js" in code:
#             code["frontend/App.js"] += "\n// Analytics script ajouté"
#         return code