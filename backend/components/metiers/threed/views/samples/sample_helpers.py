# sample_helpers.py
"""Exemple d'utilisation des helpers views (Python)"""
from ..helpers import render_helper_view
print(render_helper_view('Test') if 'render_helper_view' in dir() else 'Helper view sample')
