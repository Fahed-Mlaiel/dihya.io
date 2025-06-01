"""
Dihya – Routage avancé pour Social
- Sécurité, multilingue, audit, extensibilité
"""
from django.urls import path, include
from . import routes

urlpatterns = [
    path('', include(routes)),
]
