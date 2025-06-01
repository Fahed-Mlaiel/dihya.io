"""
Dihya – Routage avancé pour Tourisme
- Sécurité, multilingue, audit, extensibilité
"""
from django.urls import path, include
from . import routes

urlpatterns = [
    path('', include(routes)),
]
