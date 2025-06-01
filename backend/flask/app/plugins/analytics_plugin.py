"""
Plugin Analytics pour Dihya Coding.

Ce module fournit un plugin extensible pour la collecte et l’exposition d’analyses d’usage (visites, événements, conversions, etc.)
dans les projets générés par Dihya Coding, avec API REST sécurisée, gestion des rôles et validation.

Bonnes pratiques :
- Protéger toutes les routes par des vérifications de permissions (ACL).
- Valider et filtrer toutes les entrées utilisateur (événements, données).
- Logger les opérations critiques (collecte, suppression, export).
- Prévoir des tests unitaires pour chaque endpoint.
- Ne jamais exposer de données sensibles ou de secrets dans les contenus ou logs.

Exemple d’utilisation :
    from backend.flask.app.plugins.analytics_plugin import analytics_blueprint
    app.register_blueprint(analytics_blueprint, url_prefix="/api/analytics")
"""

from flask import Blueprint, request, jsonify, abort, g
from backend.flask.app.security.acl import require_permission
import logging
import time

analytics_blueprint = Blueprint("analytics", __name__)

# Simu base mémoire (remplacer par DB réelle)
_ANALYTICS_EVENTS = []

def validate_event(data):
    """Valide les champs d’un événement analytics."""
    event_type = data.get("event_type", "")
    timestamp = data.get("timestamp", 0)
    if not event_type or not isinstance(event_type, str) or len(event_type) > 100:
        return False, "Type d'événement invalide"
    if not isinstance(timestamp, (int, float)) or timestamp <= 0:
        return False, "Timestamp invalide"
    return True, ""

@analytics_blueprint.route("/event", methods=["POST"])
@require_permission("submit_project")
def collect_event():
    """
    Collecte un événement analytics.

    Sécurité :
    - Vérifie la permission 'submit_project'.
    - Valide les champs reçus.
    - Loggue l’opération pour audit.
    """
    data = request.get_json(force=True)
    valid, msg = validate_event(data)
    if not valid:
        abort(400, msg)
    event = {
        "event_type": data["event_type"],
        "timestamp": data["timestamp"],
        "user_id": getattr(g, "current_user", None).id if hasattr(g, "current_user") else "anonymous",
        "meta": data.get("meta", {})
    }
    _ANALYTICS_EVENTS.append(event)
    logging.info(f"[ANALYTICS] Event collecté : {event['event_type']} par {event['user_id']}")
    return jsonify({"status": "collected"}), 201

@analytics_blueprint.route("/events", methods=["GET"])
@require_permission("view_reports")
def list_events():
    """
    Liste les événements analytics collectés.

    Sécurité :
    - Vérifie la permission 'view_reports'.
    - Ne retourne jamais de données sensibles.
    """
    # Optionnel : filtrage par type ou période
    event_type = request.args.get("event_type")
    since = float(request.args.get("since", 0))
    filtered = [
        e for e in _ANALYTICS_EVENTS
        if (not event_type or e["event_type"] == event_type)
        and (since == 0 or e["timestamp"] >= since)
    ]
    return jsonify(filtered)

@analytics_blueprint.route("/event/<int:event_idx>", methods=["DELETE"])
@require_permission("delete_content")
def delete_event(event_idx):
    """
    Supprime un événement analytics par son index.

    Sécurité :
    - Vérifie la permission 'delete_content'.
    - Loggue l’opération pour audit.
    """
    if event_idx < 0 or event_idx >= len(_ANALYTICS_EVENTS):
        abort(404, "Événement introuvable")
    event = _ANALYTICS_EVENTS.pop(event_idx)
    logging.info(f"[ANALYTICS] Suppression event {event['event_type']} par {g.current_user.id if hasattr(g, 'current_user') else 'unknown'}")
    return jsonify({"status": "deleted", "event_type": event["event_type"]})