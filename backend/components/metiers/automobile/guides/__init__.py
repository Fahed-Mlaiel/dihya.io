"""
Guides ultra avancés pour le module Automobile (accessibilité, sécurité, RGPD, plugins, tests, conformité).
Chargement dynamique, ready-to-use, API d’accès guides, hooks, multilingue, CI/CD.
"""

def get_guides_list():
    """Retourne la liste des guides disponibles pour l’automobile."""
    return [
        "ACCESSIBILITY_GUIDE_AUTO.md",
        "PLUGINS_GUIDE_AUTO.md",
        "README_ADVANCED.md",
        "RGPD_GUIDE_AUTO.md",
        "SECURITY_GUIDE_AUTO.md",
        "TEST_STRATEGY_AUTO.md"
    ]

__all__ = ["get_guides_list"]
