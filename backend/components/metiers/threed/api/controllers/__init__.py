# Point d'entrée du module controllers

from .threed_controller import get_threed, create_threed, update_threed, delete_threed
# Expose explicitement les méthodes du contrôleur Threed
__all__ = [
    'get_threed',
    'create_threed',
    'update_threed',
    'delete_threed',
    # Ajouter ici d’autres contrôleurs ou helpers si besoin
]
