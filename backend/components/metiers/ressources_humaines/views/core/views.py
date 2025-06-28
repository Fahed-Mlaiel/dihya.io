"""
views.py - Vues/metiers pour Ressources_humaines (exemple)
"""


def render_home():
    return "<h1>Bienvenue sur Ressources_humaines</h1>"


def render_model(model):
    return f"<div>Modèle: {model.get('name', None)}</div>"
