"""
Initialisation des services métier (Python)
Expose tous les services ultra avancés : CRUD, hooks, validation, extension, doc, exemples.
"""
from .asset_service import get_all_assets, create_asset, register_pre_create_hook, register_post_create_hook

__all__ = ['get_all_assets', 'create_asset', 'register_pre_create_hook', 'register_post_create_hook']

# Exemple d’utilisation :
# from blueprints.services import create_asset, register_pre_create_hook
# @register_pre_create_hook
def validate(data):
    ...
# create_asset({"name": "Ordinateur", "owner": "Alice"})
