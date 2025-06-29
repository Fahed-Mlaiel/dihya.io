"""
Initialisation des blueprints webApp (Python)
Exporte tous les générateurs d'applications web métiers
"""
from .webapp import create_web_app, WebHook

__all__ = ['create_web_app', 'WebHook']
