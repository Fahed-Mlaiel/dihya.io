# sample_admin.py
"""Exemple d'utilisation des admin views (Python)"""
from ..admin import admin_views
print(getattr(admin_views, 'get_admin_dashboard', lambda: 'Admin dashboard sample')())
