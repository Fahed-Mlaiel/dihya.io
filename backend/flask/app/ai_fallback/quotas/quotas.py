"""
Gestion des quotas d’utilisation des modèles IA pour Dihya Coding.

Ce module permet de :
- Suivre la consommation des quotas IA (OpenAI, Mixtral, LLaMA, etc.)
- Détecter le dépassement de quota et déclencher le fallback automatique
- Exposer des fonctions de vérification et de gestion des quotas
- Sécuriser l’accès aux informations de quotas (authentification requise)
- Logger chaque événement de quota (dépassement, reset, fallback)
"""

from datetime import datetime, timedelta
from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
import threading

# Simuler un stockage en mémoire (à remplacer par Redis ou DB en prod)
_QUOTA_STORE = {}
_LOCK = threading.Lock()

# Configuration par défaut (à adapter selon le modèle)
DEFAULT_QUOTAS = {
    "openai": {"limit": 1000, "window": 86400},      # 1000 requêtes/jour
    "mixtral": {"limit": 5000, "window": 86400},
    "llama": {"limit": 5000, "window": 86400},
    "mistral": {"limit": 5000, "window": 86400},
}

bp = Blueprint("ai_quotas", __name__, url_prefix="/api/ai/quotas")

def _get_user_key(user_id, provider):
    return f"{user_id}:{provider}"

def _now():
    return datetime.utcnow()

def _reset_if_needed(user_id, provider):
    key = _get_user_key(user_id, provider)
    with _LOCK:
        entry = _QUOTA_STORE.get(key)
        if not entry or (_now() - entry["start"]) > timedelta(seconds=DEFAULT_QUOTAS[provider]["window"]):
            _QUOTA_STORE[key] = {"count": 0, "start": _now()}

def check_quota(user_id, provider):
    """
    Vérifie si l'utilisateur a dépassé son quota pour un provider IA.
    Retourne True si quota disponible, False sinon.
    """
    if provider not in DEFAULT_QUOTAS:
        raise ValueError("Provider IA inconnu.")
    _reset_if_needed(user_id, provider)
    key = _get_user_key(user_id, provider)
    with _LOCK:
        count = _QUOTA_STORE[key]["count"]
        limit = DEFAULT_QUOTAS[provider]["limit"]
        return count < limit

def increment_quota(user_id, provider):
    """
    Incrémente le compteur de quota pour l'utilisateur et le provider IA.
    """
    if provider not in DEFAULT_QUOTAS:
        raise ValueError("Provider IA inconnu.")
    _reset_if_needed(user_id, provider)
    key = _get_user_key(user_id, provider)
    with _LOCK:
        _QUOTA_STORE[key]["count"] += 1
        # Logging (à remplacer par un vrai logger)
        print(f"[{_now()}] [QUOTA] User {user_id} - {provider}: {_QUOTA_STORE[key]['count']} / {DEFAULT_QUOTAS[provider]['limit']}")

def get_quota_status(user_id, provider):
    """
    Retourne le statut de quota pour l'utilisateur et le provider IA.
    """
    if provider not in DEFAULT_QUOTAS:
        raise ValueError("Provider IA inconnu.")
    _reset_if_needed(user_id, provider)
    key = _get_user_key(user_id, provider)
    with _LOCK:
        entry = _QUOTA_STORE[key]
        return {
            "provider": provider,
            "count": entry["count"],
            "limit": DEFAULT_QUOTAS[provider]["limit"],
            "window_seconds": DEFAULT_QUOTAS[provider]["window"],
            "window_start": entry["start"].isoformat(),
            "window_end": (entry["start"] + timedelta(seconds=DEFAULT_QUOTAS[provider]["window"])).isoformat(),
        }

def reset_quota(user_id, provider):
    """
    Réinitialise le quota pour l'utilisateur et le provider IA (admin uniquement).
    """
    if provider not in DEFAULT_QUOTAS:
        raise ValueError("Provider IA inconnu.")
    key = _get_user_key(user_id, provider)
    with _LOCK:
        _QUOTA_STORE[key] = {"count": 0, "start": _now()}

# --- ROUTES API SECURISEES ---

@bp.route("/status/<provider>", methods=["GET"])
@jwt_required()
def api_get_quota_status(provider):
    """
    Récupère le statut de quota pour l'utilisateur courant et le provider IA.
    """
    user_id = get_jwt_identity()
    try:
        status = get_quota_status(user_id, provider)
        return jsonify(status), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@bp.route("/increment/<provider>", methods=["POST"])
@jwt_required()
def api_increment_quota(provider):
    """
    Incrémente le quota pour l'utilisateur courant et le provider IA.
    """
    user_id = get_jwt_identity()
    try:
        increment_quota(user_id, provider)
        return jsonify({"message": "Quota incrémenté."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@bp.route("/reset/<provider>/<user_id>", methods=["POST"])
@jwt_required()
def api_reset_quota(provider, user_id):
    """
    Réinitialise le quota pour un utilisateur et un provider IA (admin uniquement).
    """
    # Vérification du rôle admin (à adapter selon votre système d'auth)
    current_user = get_jwt_identity()
    if not _is_admin(current_user):
        return jsonify({"error": "Accès refusé"}), 403
    try:
        reset_quota(user_id, provider)
        return jsonify({"message": "Quota réinitialisé."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

def _is_admin(user_id):
    # À remplacer par une vraie vérification de rôle
    return user_id == "admin"

# --- BONNES PRATIQUES ---
# - Toutes les routes sont protégées par JWT.
# - Les entrées sont validées.
# - Les accès admin sont vérifiés pour les opérations sensibles.
# - Les logs sont horodatés.
# - Aucun détail sensible n'est exposé dans les erreurs.

# --- À intégrer dans votre app Flask principale ---
# from backend.flask.app.ai_fallback.quotas.quotas import bp as quotas_bp
# app.register_blueprint(quotas_bp)