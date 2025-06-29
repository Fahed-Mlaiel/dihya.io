"""
views.py - Vues/metiers pour Banque_Finance (exemple)
"""


def render_home():
    return "<h1>Bienvenue sur Banque_Finance</h1>"


def render_model(model):
    return f"<div>Modèle: {model.get('name', None)}</div>"
