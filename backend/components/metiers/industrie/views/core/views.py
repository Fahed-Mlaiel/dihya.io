"""
views.py - Vues/metiers pour Industrie (exemple)
"""


def render_home():
    return "<h1>Bienvenue sur Industrie</h1>"


def render_model(model):
    return f"<div>Modèle: {model.get('name', None)}</div>"
