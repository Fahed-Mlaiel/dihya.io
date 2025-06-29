"""
Initialisation des blueprints API (Python)
Exporte tous les générateurs de routes métier et backend avancé
"""
import importlib
import os

from .routes.asset_routes import bp as asset_routes_bp
from .generators.backendApi import create_backend_api

__all__ = ['asset_routes_bp', 'create_backend_api']

# Découverte automatique d'autres routes
current_dir = os.path.dirname(__file__)
routes_dir = os.path.join(current_dir, 'routes')
for f in os.listdir(routes_dir):
    if f.endswith('.py') and f != 'asset_routes.py':
        mod = importlib.import_module(f'.routes.{f[:-3]}', __package__)
        globals()[f[:-3]] = mod
        __all__.append(f[:-3])

# Documentation intégrée
# from blueprints.api import create_backend_api, asset_routes_bp
# app = create_backend_api(metier="Inventaire", models=..., services=...)
# app.run()
