# sample_public.py
"""Exemple d'utilisation des public views (Python)"""
from ..public import public_views
print(getattr(public_views, 'render_public_info', lambda x: 'Public info sample')('Bienvenue'))
