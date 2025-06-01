"""
Déclaration des routes principales du backend Dihya (Flask)
- REST/GraphQL, multilingue, sécurité, audit, plugins, RGPD, extensibilité, CI/CD-ready
"""
from flask import Blueprint, jsonify, request
from .security import require_role

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/api/generate', methods=['POST'])
@require_role('ai_user')
def generate_project():
    # Exemple de génération automatique (mock)
    return jsonify({
        'status': 'success',
        'message': {
            'fr': "Projet généré avec succès",
            'en': "Project generated successfully",
            'ar': "تم إنشاء المشروع بنجاح",
            'tzm': "Iɣewwaṛ amezruy s wul"
        }.get(request.headers.get('X-Dihya-Lang', 'fr'), "Projet généré avec succès")
    }), 200

@routes_bp.route('/api/auth/login', methods=['POST'])
def login():
    # Authentification mock (à remplacer par JWT réel)
    return jsonify({'token': 'mock-jwt-token', 'role': 'user'}), 200

@routes_bp.route('/api/user/profile', methods=['GET'])
@require_role('user')
def user_profile():
    return jsonify({'user': 'demo', 'role': 'user'}), 200

@routes_bp.route('/api/plugins', methods=['GET'])
@require_role('user')
def list_plugins():
    # Plugins mock
    return jsonify({'plugins': ['example_plugin']}), 200

@routes_bp.route('/api/templates', methods=['GET'])
def list_templates():
    return jsonify({'templates': ['template1', 'template2']}), 200

def register_routes(app):
    app.register_blueprint(routes_bp)
