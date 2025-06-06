# Exemple ultra avancé clé en main des middlewares API Threed (Python)
from ..middlewares.middlewares import audit_request, rgpd_middleware, accessibility_middleware
from fastapi import FastAPI
import logging

def sample_middlewares_ultra():
    app = FastAPI()
    app.middleware('http')(rgpd_middleware)
    app.middleware('http')(accessibility_middleware)
    app.middleware('http')(audit_request)
    logging.info('Middlewares ultra avancé appliqués')
    print('Middlewares ultra avancé exécuté avec succès.')
