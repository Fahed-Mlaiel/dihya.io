"""
Initialisation du module de validation pour Dihya Coding.

Ce package centralise l'import et l'utilisation des schémas de validation pour tout le backend.
Permet d'assurer la cohérence, la sécurité et la maintenabilité des données échangées via l'API.

Bonnes pratiques :
- Importer ici tous les schémas/fonctions de validation nécessaires
- Faciliter l'extension du système de validation (nouveaux schémas métiers)
- Ne jamais exposer de logique métier ou de secrets ici
"""

from .schemas import (
    validate_user,
    validate_project,
    validate_plugin,
    validate_notification,
)