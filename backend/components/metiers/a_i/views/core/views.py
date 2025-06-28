"""
views.py - Vues/metiers pour A_I (exemple)
"""


def render_home():
    return "<h1>Bienvenue sur A_I</h1>"


def render_model(model):
    return f"<div>Modèle: {model.get('name', None)}</div>"
