# sample_partials.py
"""Exemple d'utilisation des partials views (Python)"""
from ..partials import partials_views
print(getattr(partials_views, 'render_widget', lambda x, y: 'Widget sample')('badge', 'OK'))
