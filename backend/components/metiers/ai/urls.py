"""
Dihya Backend AI – Définition des routes API (Flask/Django/GraphQL)
"""
from .ai import ai_bp
# Pour Flask : app.register_blueprint(ai_bp)
# Pour Django : urlpatterns = [path('api/ai/', include('dihya.backend.components.metiers.ai.urls'))]
# Pour GraphQL : brancher le schéma sur /api/ai/graphql
