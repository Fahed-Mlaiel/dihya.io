"""
views.py - Vues/metiers pour Juridique (exemple)
"""


def render_home():
    return "<h1>Bienvenue sur Juridique</h1>"


def render_model(model):
    return f"<div>Modèle: {model.get('name', None)}</div>"
