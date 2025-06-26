"""
views.py - Vues/metiers pour Immobilier (exemple)
"""


def render_home():
    return "<h1>Bienvenue sur Immobilier</h1>"


def render_model(model):
    return f"<div>Modèle: {model.get('name', None)}</div>"
