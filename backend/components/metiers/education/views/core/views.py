"""
views.py - Vues/metiers pour Education (exemple)
"""


def render_home():
    return "<h1>Bienvenue sur Education</h1>"


def render_model(model):
    return f"<div>Modèle: {model.get('name', None)}</div>"
