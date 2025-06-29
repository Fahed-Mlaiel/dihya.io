"""
views.py - Vues/metiers pour Automobile (exemple)
"""


def render_home():
    return "<h1>Bienvenue sur Automobile</h1>"


def render_model(model):
    return f"<div>Modèle: {model.get('name', None)}</div>"
