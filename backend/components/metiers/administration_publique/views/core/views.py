"""
views.py - Vues/metiers pour Threed (exemple)
"""

def render_home():
    return "<h1>Bienvenue sur Threed</h1>"

def render_model(model):
    return f"<div>Modèle: {model['name']}</div>"
