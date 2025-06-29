"""
views_helper.py - Fonctions utilitaires avancées pour les vues Mobile (Python)
"""


def render_title(title):
    return f"<h1>{title}</h1>"


def render_model(model):
    return f"<div>Modèle: {model.get('name', None)}</div>"


def render_error(msg):
    return f"<div class='error'>{msg}</div>"
