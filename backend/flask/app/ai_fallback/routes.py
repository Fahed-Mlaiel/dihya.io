"""
Fallback IA API routes for Dihya Coding (Flask).
"""
from flask import Blueprint, request, jsonify
from backend.flask.app.ai_fallback import fallback

fallback_bp = Blueprint('ai_fallback', __name__)

@fallback_bp.route('/api/ai/fallback', methods=['POST'])
def fallback_ia():
    data = request.get_json(force=True)
    prompt = data.get('prompt')
    provider = data.get('provider', 'mixtral')
    result = fallback.generate_with_model(provider, prompt, data.get('task_type', 'webapp'))
    return jsonify({"provider": provider, "fallback": True, "result": result})

__all__ = ["fallback_bp"]
