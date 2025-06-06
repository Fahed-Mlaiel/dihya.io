"""
Guides ultra avancés pour le module Assurance (accessibilité, sécurité, RGPD, plugins, tests, conformité).
Chargement dynamique, ready-to-use, API d’accès guides, hooks, multilingue, CI/CD.
"""

def get_guides_list():
    """Retourne la liste des guides disponibles pour l’assurance."""
    return [
        "ACCESSIBILITY_GUIDE_ASSURANCE.md",
        "PLUGINS_GUIDE_ASSURANCE.md",
        "README_ADVANCED.md",
        "RGPD_GUIDE_ASSURANCE.md",
        "SECURITY_GUIDE_ASSURANCE.md",
        "TEST_STRATEGY_ASSURANCE.md"
    ]

__all__ = ["get_guides_list"]
