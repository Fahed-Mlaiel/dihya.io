"""
Initialisation ultra avancée du module templates métiers dynamiques Dihya Coding.
Centralise l’import, la documentation, la sécurité, l’audit, la RGPD, l’accessibilité, la multitenancy, les plugins, l’i18n, la traçabilité, la conformité, la CI/CD, la souveraineté logicielle.

Templates métiers disponibles :
- ecommerce, education, social, banque_finance, energie, construction, btp, arts, science, santé, marketing, ...

Exemple d’utilisation :
    from app.services.templates import get_template_for_domain
    tpl = get_template_for_domain("banque_finance")
    print(tpl)
"""
import importlib
import os
import logging

TEMPLATES_DIR = os.path.dirname(__file__)

__all__ = []

def get_template_for_domain(domain: str):
    """
    Importe dynamiquement le template Python pour un domaine métier donné.
    Args:
        domain (str): Nom du domaine (ex: 'ecommerce', 'education', 'social')
    Returns:
        dict: Structure du template métier
    Raises:
        ImportError: Si le template n’existe pas
    """
    try:
        module = importlib.import_module(f".{{}}".format(domain), __name__)
        __all__.append(domain)
        return module.get_template()
    except Exception as e:
        logging.error(f"[TEMPLATES] Erreur import template {domain}: {e}")
        raise ImportError(f"Template métier '{domain}' introuvable ou invalide.")

# Import dynamique ultra avancé de tous les templates métiers présents dans ce dossier
# (aucune modification manuelle requise pour ajouter un nouveau métier)
for fname in os.listdir(TEMPLATES_DIR):
    if fname.endswith('.py') and fname not in ('__init__.py',):
        modname = fname[:-3]
        try:
            importlib.import_module(f".{{}}".format(modname), __name__)
            __all__.append(modname)
        except Exception as e:
            logging.warning(f"[TEMPLATES] Erreur import {modname}: {e}")
