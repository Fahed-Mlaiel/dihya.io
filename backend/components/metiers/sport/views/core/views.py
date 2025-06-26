"""
views.py - Vues/metiers pour Sport (exemple)
"""


def render_home():
    return "<h1>Bienvenue sur Sport</h1>"


def render_model(model):
    return f"<div>Modèle: {model.get('name', None)}</div>"
