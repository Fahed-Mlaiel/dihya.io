"""
Dihya – Routage avancé pour Transport
- Sécurité, multilingue, audit, extensibilité
"""
from django.urls import path, include
from . import routes

urlpatterns = [
    path('', include(routes)),
]
