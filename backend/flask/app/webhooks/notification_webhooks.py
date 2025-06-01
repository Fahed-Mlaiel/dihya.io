"""
Gestion des webhooks de notification pour Dihya Coding.

Ce module centralise la réception, la validation et le traitement sécurisé des notifications externes
(notifications push, SMS, emails transactionnels, etc.), en garantissant la traçabilité, la sécurité et la conformité RGPD.

Bonnes pratiques :
- Valider systématiquement la signature, l’origine et le contenu de chaque webhook reçu.
- Logger tous les événements pour audit et traçabilité.
- Protéger les endpoints contre les abus (rate limiting, validation stricte, authentification si possible).
- Ne jamais traiter ou exposer de données sensibles sans validation.
- Prévoir des tests unitaires pour chaque handler de webhook.

Exemple d’utilisation :
    from backend.flask.app.webhooks.notification_webhooks import notification_webhook_blueprint
    app.register_blueprint(notification_webhook_blueprint, url_prefix="/webhooks/notification")
"""

from flask import Blueprint, request, jsonify, abort
import logging
import hmac
import hashlib
import os

notification_webhook_blueprint = Blueprint("notification_webhook", __name__)

def verify_signature(payload: bytes, signature: str, secret: str) -> bool:
    """
    Vérifie la signature HMAC-SHA256 du webhook.

    Args:
        payload (bytes): Corps brut de la requête.
        signature (str): Signature reçue (header).
        secret (str): Secret partagé.

    Returns:
        bool: True si la signature est valide, False sinon.
    """
    computed = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(computed, signature)

@notification_webhook_blueprint.route("/", methods=["POST"])
def handle_notification_webhook():
    """
    Endpoint sécurisé pour recevoir les notifications externes.

    Sécurité :
    - Vérifie la signature HMAC.
    - Valide le contenu et l’origine.
    - Loggue l’événement pour audit.
    - Applique un rate limiting (à configurer via middleware).

    Returns:
        JSON: Statut du traitement.
    """
    secret = os.environ.get("NOTIFICATION_WEBHOOK_SECRET")
    if not secret:
        logging.error("[NOTIF_WEBHOOK] Secret de signature manquant.")
        abort(500, "Configuration manquante.")

    payload = request.get_data()
    signature = request.headers.get("X-Signature", "")

    if not verify_signature(payload, signature, secret):
        logging.warning("[NOTIF_WEBHOOK] Signature invalide.")
        abort(400, "Signature invalide.")

    try:
        data = request.get_json(force=True)
    except Exception as e:
        logging.warning(f"[NOTIF_WEBHOOK] JSON invalide : {e}")
        abort(400, "Payload JSON invalide.")

    event_type = data.get("event")
    notification_id = data.get("notification_id")
    user_id = data.get("user_id")

    if not event_type or not notification_id:
        logging.warning("[NOTIF_WEBHOOK] Champs obligatoires manquants.")
        abort(400, "Champs obligatoires manquants.")

    logging.info(f"[NOTIF_WEBHOOK] Event reçu : {event_type} pour notification_id={notification_id}, user_id={user_id}")

    # TODO: Ajouter la logique métier (mise à jour base, envoi notification interne, etc.)

    return jsonify({"status": "success"}), 200