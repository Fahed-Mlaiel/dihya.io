"""
views.py - Vues/metiers pour Culture (exemple)
"""


def render_home():
    return "<h1>Bienvenue sur Culture</h1>"


def render_model(model):
    return f"<div>Modèle: {model.get('name', None)}</div>"
