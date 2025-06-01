"""
Dihya – Routage avancé pour Sport
- Sécurité, multilingue, audit, extensibilité
"""
from django.urls import path, include
from . import routes

urlpatterns = [
    path('', include(routes)),
]
