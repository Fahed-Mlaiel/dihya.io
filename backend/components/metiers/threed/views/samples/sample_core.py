# sample_core.py
"""Exemple d'utilisation des core views (Python)"""
from ..core import render_core_view
print(render_core_view('Test') if 'render_core_view' in dir() else 'Core view sample')
