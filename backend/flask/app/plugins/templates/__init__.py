"""
Module d'initialisation pour les templates intelligents par domaine dans Dihya Coding.

Ce package permet de gérer des templates dynamiques adaptés à différents domaines métiers
(e-commerce, éducation, social, etc.) pour la génération automatique de projets.

Bonnes pratiques :
- Chaque template doit être documenté, validé et versionné.
- Les templates doivent respecter la sécurité, la modularité et la souveraineté logicielle.
- Prévoir un mécanisme de sélection automatique du template selon le domaine détecté.
- Permettre l’extension par ajout de nouveaux templates sans modifier le cœur du backend.

Exemple d'import :
    from backend.flask.app.plugins.templates import get_template_for_domain

"""

def get_template_for_domain(domain):
    """
    Retourne le template adapté au domaine spécifié.
    À implémenter selon la logique métier (mapping domaine → template).
    """
    # TODO: Ajouter la logique de sélection de template
    return f"[Template pour le domaine '{domain}' non implémenté]"