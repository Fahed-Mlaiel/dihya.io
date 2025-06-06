# sample_threed.py
"""Exemple d'utilisation des threed views (Python)"""
from ..threed import threed_views
print(getattr(threed_views, 'render_3d', lambda x: '3D view sample')('Cube'))
