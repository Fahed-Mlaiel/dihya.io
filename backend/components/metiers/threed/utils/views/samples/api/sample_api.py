# sample_api.py
"""Exemple d'utilisation des api views (Python)"""
from ..api import api_views
print(getattr(api_views, 'render_api_response', lambda x: 'API response sample')('ok'))
