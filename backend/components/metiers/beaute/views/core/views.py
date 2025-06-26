"""
views.py - Vues/metiers pour Beaute (exemple)
"""


def render_home():
    return "<h1>Bienvenue sur Beaute</h1>"


def render_model(model):
    return f"<div>Modèle: {model.get('name', None)}</div>"
