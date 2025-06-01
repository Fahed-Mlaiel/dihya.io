"""
Dihya Backend AI – Views avancées pour API IA (Django/Flask compatible)
REST & GraphQL-ready, sécurité maximale, multilingue, RGPD, plugins, audit, multitenancy.
"""
from flask import Blueprint, request, jsonify, current_app
from .ai import ai_bp

# Pour extension Django, DRF ou GraphQL, voir /routes/vr_ar/ (exemple)
# Ici, on expose le blueprint Flask déjà ultra avancé (voir ai.py)

# Pour GraphQL, on pourrait brancher Strawberry/FastAPI/Graphene ici
# Exemples d'intégration, voir /ai/README.md et /backend/ai/README.md
