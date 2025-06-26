"""
views.py - Vues/metiers pour vr_ar (exemple)
"""


def render_home():
    return "<h1>Bienvenue sur vr_ar</h1>"


def render_model(model):
    return f"<div>Modèle: {model.get('name', None)}</div>"
