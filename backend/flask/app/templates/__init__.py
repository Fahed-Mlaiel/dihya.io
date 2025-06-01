"""
Init du package templates métiers pour Dihya Coding.

Ce module permet d’importer dynamiquement les templates métiers (e-commerce, éducation, social, etc.)
pour la génération automatique de projets selon le domaine détecté.

Bonnes pratiques :
- Utiliser la fonction `get_template_for_domain(domain)` pour sélectionner le template adapté.
- Ajouter chaque nouveau template dans le mapping ci-dessous.
- Documenter chaque template dans son module dédié.
"""

from .ecommerce import get_template as ecommerce_template
from .education import get_template as education_template
from .social import get_template as social_template

TEMPLATE_MAP = {
    "ecommerce": ecommerce_template,
    "education": education_template,
    "social": social_template,
    # Ajouter ici d'autres domaines si besoin
}

def get_template_for_domain(domain):
    """
    Retourne le template adapté au domaine métier.
    :param domain: str (ex: "ecommerce", "education", "social")
    :return: dict (structure du template) ou None si inconnu
    """
    func = TEMPLATE_MAP.get(domain)
    if func:
        return func()
    return None