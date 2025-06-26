"""
Initialisation des hooks métier (Python)
Expose tous les hooks asset ultra avancés : validation, transformation, notification, audit, extension.
"""
from .asset_hooks import before_asset_create, after_asset_create, run_before_asset_create, run_after_asset_create

__all__ = ['before_asset_create', 'after_asset_create', 'run_before_asset_create', 'run_after_asset_create']

# Exemple d’utilisation :
# from blueprints.hooks import before_asset_create, run_before_asset_create
# @before_asset_create
def validate(data):
    ...
# data = run_before_asset_create(data)
