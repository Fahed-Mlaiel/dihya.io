"""
Template de génération – Dihya Coding

Ce module définit la structure de base pour les templates de génération automatique.
Un template permet de générer du code adapté à un domaine ou un besoin spécifique (e-commerce, éducation, social, etc.).

Bonnes pratiques :
- Chaque template doit hériter de GenerationTemplateBase
- Documenter chaque template (usage, hooks, options, dépendances)
- Ne jamais inclure de code non validé ou non sécurisé
- Permettre l’extension via hooks/plugins
- Logger les actions critiques pour auditabilité (sans fuite de données sensibles)
- Respecter la conformité RGPD (pas de données sensibles, audit, purge)
"""

from typing import Dict, Any
import logging

class GenerationTemplateBase:
    """
    Classe de base pour tous les templates de génération Dihya Coding.

    Méthodes à surcharger :
        - get_metadata : retourne les infos du template
        - generate_files : génère les fichiers spécifiques au template

    Bonnes pratiques :
        - Documenter chaque template (usage, hooks, options, dépendances)
        - Logger les actions importantes (sans données sensibles)
        - Ne jamais inclure de code non validé ou non sécurisé
        - Respecter la conformité RGPD (pas de fuite de données)
    """

    name = "BaseTemplate"
    description = "Template de base pour la génération automatique."
    domain = "générique"
    version = "1.0.0"
    author = "Dihya Coding"
    safe = True  # Indique si le template est validé/sandboxé

    def get_metadata(self) -> Dict[str, Any]:
        """
        Retourne les métadonnées du template.

        Returns:
            dict: Métadonnées (nom, description, domaine, options…)
        """
        return {
            "name": self.name,
            "description": self.description,
            "domain": self.domain,
            "version": self.version,
            "author": self.author,
            "safe": self.safe,
            "options": []
        }

    def generate_files(self, needs: Dict[str, Any]) -> Dict[str, str]:
        """
        Génère les fichiers spécifiques à ce template.

        Args:
            needs (dict): Besoins du projet.

        Returns:
            dict: { chemin_fichier: contenu_code }
        """
        # Validation minimale des besoins (sécurité)
        if not isinstance(needs, dict):
            logging.error(f"[Template:{self.name}] Paramètre 'needs' invalide.")
            return {}
        logging.info(f"[Template:{self.name}] generate_files appelé pour domaine '{self.domain}'.")
        # À surcharger dans chaque template concret
        return {}

    def is_safe(self) -> bool:
        """
        Indique si le template est validé/sandboxé (pour activation automatique).

        Returns:
            bool: True si le template est considéré comme sûr.
        """
        return self.safe

# Exemple de template concret (à placer dans un autre fichier)
# from .generation_template import GenerationTemplateBase
#
# class EcommerceTemplate(GenerationTemplateBase):
#     name = "Ecommerce"
#     description = "Template pour boutique en ligne avec panier, paiement, gestion produits."
#     domain = "e-commerce"
#
#     def generate_files(self, needs):
#         files = {
#             "frontend/pages/Shop.js": "// Page boutique auto-générée",
#             "backend/routes/shop.py": "# Route Flask pour la boutique"
#         }
#         return files