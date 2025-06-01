"""
Gestion des webhooks de paiement pour Dihya Coding.

Ce module centralise la réception, la validation et le traitement sécurisé des notifications de paiement
provenant de prestataires externes (Stripe, PayPal, etc.), en garantissant la traçabilité, la sécurité et la conformité RGPD.

Bonnes pratiques :
- Valider systématiquement la signature, l’origine et le contenu de chaque webhook reçu.
- Logger tous les événements pour audit et traçabilité.
- Protéger les endpoints contre les abus (rate limiting, validation stricte, authentification si possible).
- Ne jamais traiter ou exposer de données sensibles sans validation.
- Prévoir des tests unitaires pour chaque handler de webhook.

Exemple d’utilisation :
    from backend.flask.app.webhooks.payment_webhooks import payment_webhook_blueprint
    app.register_blueprint(payment_webhook_blueprint, url_prefix="/webhooks/payment")
"""

from flask import Blueprint, request, jsonify, abort, current_app
import logging
import hmac
import hashlib
import os

payment_webhook_blueprint = Blueprint("payment_webhook", __name__)

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

@payment_webhook_blueprint.route("/", methods=["POST"])
def handle_payment_webhook():
    """
    Endpoint sécurisé pour recevoir les notifications de paiement.

    Sécurité :
    - Vérifie la signature HMAC (exemple Stripe/PayPal).
    - Valide le contenu et l’origine.
    - Loggue l’événement pour audit.
    - Applique un rate limiting (à configurer via middleware).

    Returns:
        JSON: Statut du traitement.
    """
    # Récupération du secret de signature (à stocker en variable d’environnement)
    secret = os.environ.get("PAYMENT_WEBHOOK_SECRET")
    if not secret:
        logging.error("[PAYMENT_WEBHOOK] Secret de signature manquant.")
        abort(500, "Configuration manquante.")

    # Lecture du payload brut et de la signature
    payload = request.get_data()
    signature = request.headers.get("X-Signature", "")

    # Vérification de la signature
    if not verify_signature(payload, signature, secret):
        logging.warning("[PAYMENT_WEBHOOK] Signature invalide.")
        abort(400, "Signature invalide.")

    # Validation du contenu JSON
    try:
        data = request.get_json(force=True)
    except Exception as e:
        logging.warning(f"[PAYMENT_WEBHOOK] JSON invalide : {e}")
        abort(400, "Payload JSON invalide.")

    # Exemple de traitement (à adapter selon le provider)
    event_type = data.get("event")
    payment_id = data.get("payment_id")
    user_id = data.get("user_id")

    if not event_type or not payment_id:
        logging.warning("[PAYMENT_WEBHOOK] Champs obligatoires manquants.")
        abort(400, "Champs obligatoires manquants.")

    # Log de l’événement pour audit
    logging.info(f"[PAYMENT_WEBHOOK] Event reçu : {event_type} pour payment_id={payment_id}, user_id={user_id}")

    # TODO: Ajouter la logique métier (mise à jour base, envoi notification, etc.)

    return jsonify({"status": "success"}), 200