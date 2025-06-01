"""
Dihya Backend AI – Définition des routes API (Flask/Django/GraphQL-ready)
Ultra avancé, sécurisé, multilingue, REST & GraphQL, plugins, audit, RGPD, multitenancy.
"""
from .ai import ai_bp

# Pour Flask :
# app.register_blueprint(ai_bp)

# Pour Django/DRF :
# from django.urls import path, include
# urlpatterns = [path('api/ai/', include('Dihya.backend.ai.urls'))]

# Pour GraphQL :
# Brancher le schéma GraphQL sur /api/ai/graphql
