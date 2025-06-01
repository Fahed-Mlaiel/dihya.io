"""
Service de gestion des notifications internes pour Dihya Coding.

Ce module fournit les fonctions métier pour :
- Créer, lister, marquer comme lues et supprimer les notifications utilisateur
- Sécuriser l'accès (JWT requis)
- Valider les entrées/sorties
- Logger les actions importantes (création, lecture, suppression)
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime
from .models import Notification, add_notification, get_user_notifications, mark_notification_read, clear_user_notifications

bp = Blueprint("notifications", __name__, url_prefix="/api/notifications")

def log_action(user_id, action, notif_type=None):
    # Logging simple (à remplacer par un vrai logger en prod)
    print(f"[{datetime.utcnow().isoformat()}] [NOTIF] user={user_id} action={action} type={notif_type}")

@bp.route("/", methods=["GET"])
@jwt_required()
def list_notifications():
    """
    Liste les notifications de l'utilisateur courant.
    """
    user_id = get_jwt_identity()
    notifs = get_user_notifications(user_id)
    return jsonify([n.to_dict() for n in notifs]), 200

@bp.route("/", methods=["POST"])
@jwt_required()
def create_notification():
    """
    Crée une notification pour l'utilisateur courant.
    Entrée : { "notif_type": "...", "content": "...", "action_url": "..." }
    """
    user_id = get_jwt_identity()
    data = request.get_json(force=True)
    notif_data = {
        "user_id": user_id,
        "notif_type": data.get("notif_type"),
        "content": data.get("content"),
        "action_url": data.get("action_url")
    }
    try:
        Notification.validate(notif_data)
        notif = Notification(**notif_data)
        add_notification(notif)
        log_action(user_id, "create", notif.notif_type)
        return jsonify(notif.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@bp.route("/read/<int:idx>", methods=["POST"])
@jwt_required()
def mark_read(idx):
    """
    Marque une notification comme lue (par index dans la liste utilisateur).
    """
    user_id = get_jwt_identity()
    notifs = get_user_notifications(user_id)
    if idx < 0 or idx >= len(notifs):
        return jsonify({"error": "Notification introuvable"}), 404
    mark_notification_read(notifs[idx])
    log_action(user_id, "read", notifs[idx].notif_type)
    return jsonify({"message": "Notification marquée comme lue"}), 200

@bp.route("/clear", methods=["POST"])
@jwt_required()
def clear_all():
    """
    Supprime toutes les notifications de l'utilisateur courant.
    """
    user_id = get_jwt_identity()
    clear_user_notifications(user_id)
    log_action(user_id, "clear")
    return jsonify({"message": "Notifications supprimées"}), 200

# À intégrer dans votre app Flask principale :
# from backend.flask.app.notifications.service import bp as notifications_bp
# app.register_blueprint(notifications_bp)