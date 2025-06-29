"""
views.py - Vues/metiers pour Assurance (exemple)
"""


def render_home():
    return "<h1>Bienvenue sur Assurance</h1>"


def render_model(model):
    return f"<div>Modèle: {model.get('name', None)}</div>"
