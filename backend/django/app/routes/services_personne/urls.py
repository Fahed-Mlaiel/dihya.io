"""
Dihya – Routage avancé pour Services à la Personne
- Sécurité, multilingue, audit, extensibilité
"""
from django.urls import path, include
from . import routes

urlpatterns = [
    path('', include(routes)),
]
