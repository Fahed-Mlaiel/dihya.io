"""
Point d’entrée Python pour le module accessibilité API Threed.
Expose les helpers, runners et hooks d’accessibilité.
"""

from .accessibility import check_accessibility

# Expose les helpers, runners et hooks d’accessibilité
__all__ = [
    'check_accessibility',
    # Ajouter ici d’autres helpers/runners/hooks si besoin
]
