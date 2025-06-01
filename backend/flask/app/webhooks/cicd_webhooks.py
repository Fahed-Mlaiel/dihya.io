"""
Gestion des webhooks CI/CD pour Dihya Coding.

Ce module centralise la réception, la validation et le traitement sécurisé des notifications CI/CD
provenant de services externes (GitHub Actions, GitLab CI, etc.), en garantissant la traçabilité, la sécurité et la conformité RGPD.

Bonnes pratiques :
- Valider systématiquement la signature, l’origine et le contenu de chaque webhook reçu.
- Logger tous les événements pour audit et traçabilité.
- Protéger les endpoints contre les abus (rate limiting, validation stricte, authentification si possible).
- Ne jamais traiter ou exposer de données sensibles sans validation.
- Prévoir des tests unitaires pour chaque handler de webhook.

Exemple d’utilisation :
    from backend.flask.app.webhooks.cicd_webhooks import cicd_webhook_blueprint
    app.register_blueprint(cicd_webhook_blueprint, url_prefix="/webhooks/cicd")
"""

from flask import Blueprint, request, jsonify, abort
import logging
import hmac
import hashlib
import os

cicd_webhook_blueprint = Blueprint("cicd_webhook", __name__)

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

@cicd_webhook_blueprint.route("/", methods=["POST"])
def handle_cicd_webhook():
    """
    Endpoint sécurisé pour recevoir les notifications CI/CD.

    Sécurité :
    - Vérifie la signature HMAC.
    - Valide le contenu et l’origine.
    - Loggue l’événement pour audit.
    - Applique un rate limiting (à configurer via middleware).

    Returns:
        JSON: Statut du traitement.
    """
    secret = os.environ.get("CICD_WEBHOOK_SECRET")
    if not secret:
        logging.error("[CICD_WEBHOOK] Secret de signature manquant.")
        abort(500, "Configuration manquante.")

    payload = request.get_data()
    signature = request.headers.get("X-Signature", "")

    if not verify_signature(payload, signature, secret):
        logging.warning("[CICD_WEBHOOK] Signature invalide.")
        abort(400, "Signature invalide.")

    try:
        data = request.get_json(force=True)
    except Exception as e:
        logging.warning(f"[CICD_WEBHOOK] JSON invalide : {e}")
        abort(400, "Payload JSON invalide.")

    event_type = data.get("event")
    repo = data.get("repository")
    branch = data.get("branch")
    status = data.get("status")

    if not event_type or not repo or not branch or not status:
        logging.warning("[CICD_WEBHOOK] Champs obligatoires manquants.")
        abort(400, "Champs obligatoires manquants.")

    logging.info(f"[CICD_WEBHOOK] Event reçu : {event_type} sur {repo}@{branch} status={status}")

    # TODO: Ajouter la logique métier (déclenchement déploiement, notification, etc.)

    return jsonify({"status": "success"}), 200