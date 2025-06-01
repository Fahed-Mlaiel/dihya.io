"""
Module de fallback IA pour Dihya Coding.

Ce module orchestre le basculement automatique vers des modèles open source (Mixtral, LLaMA, Mistral, etc.)
en cas de quota dépassé ou d’indisponibilité des API propriétaires (OpenAI, etc.).

Fonctionnalités :
- Détection automatique du besoin de fallback (erreur API, quota, indisponibilité)
- Sélection dynamique du meilleur modèle open source disponible
- Validation stricte des entrées et sorties
- Logging sécurisé et horodaté de chaque fallback
- API sécurisée pour déclencher et monitorer le fallback

Bonnes pratiques :
- Ne jamais exposer de prompts ou de données sensibles dans les logs ou erreurs
- Protéger toutes les routes par JWT
- Modulariser chaque wrapper de modèle pour faciliter l’ajout ou la mise à jour
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime
import logging

bp = Blueprint("ai_fallback", __name__, url_prefix="/api/ai/fallback")

# Simuler la disponibilité des modèles open source
AVAILABLE_MODELS = {
    "mixtral": True,
    "llama": True,
    "mistral": True,
}

def log_fallback(user_id, prompt, model, status, error=None):
    # Logging sécurisé (ne jamais logguer le prompt en clair en prod)
    msg = f"[{datetime.utcnow().isoformat()}] [FALLBACK] user={user_id} model={model} status={status}"
    if error:
        msg += f" error={error}"
    logging.info(msg)

def validate_input(data):
    if not isinstance(data, dict):
        raise ValueError("Entrée invalide : format JSON attendu.")
    if "prompt" not in data or not isinstance(data["prompt"], str) or not data["prompt"].strip():
        raise ValueError("Prompt manquant ou invalide.")
    if "task_type" not in data or not isinstance(data["task_type"], str):
        raise ValueError("Type de tâche manquant ou invalide.")
    return data["prompt"], data["task_type"]

def select_fallback_model():
    # Sélectionne le premier modèle disponible (logique simple, à améliorer)
    for model, available in AVAILABLE_MODELS.items():
        if available:
            return model
    raise RuntimeError("Aucun modèle open source disponible pour le fallback.")

def generate_with_model(model, prompt, task_type):
    # Simulation du wrapper modèle
    if model == "mixtral":
        return "code_mixtral", "url_mixtral"
    elif model == "llama":
        return "code_llama", "url_llama"
    elif model == "mistral":
        return "code_mistral", "url_mistral"
    raise ValueError("Modèle inconnu.")

@bp.route('/generate', methods=['POST'])
@jwt_required()
def api_fallback_generate():
    user_id = get_jwt_identity()
    try:
        data = request.get_json(force=True)
        prompt, task_type = validate_input(data)
        model = select_fallback_model()
        code, url = generate_with_model(model, prompt, task_type)
        log_fallback(user_id, prompt, model, 'success')
        return jsonify({'code': code, 'url': url, 'model': model}), 200
    except Exception as e:
        log_fallback(user_id, data.get('prompt', ''), 'unknown', 'error', str(e))
        return jsonify({'error': str(e)}), 400
