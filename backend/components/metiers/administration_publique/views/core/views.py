"""
views.py - Vues/metiers pour administration_publique (exemple)
"""


def render_home():
    return "<h1>Bienvenue sur administration_publique</h1>"


def render_model(model):
    return f"<div>Modèle: {model.get('name', None)}</div>"
