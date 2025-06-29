"""
views.py - Vues/metiers pour Environnement (exemple)
"""


def render_home():
    return "<h1>Bienvenue sur Environnement</h1>"


def render_model(model):
    return f"<div>Modèle: {model.get('name', None)}</div>"
