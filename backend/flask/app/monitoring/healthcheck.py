"""
Module de healthcheck pour Dihya Coding.

Ce module expose une route API permettant de vérifier la disponibilité et l'état de santé du backend.
Il peut être utilisé par les outils de monitoring, CI/CD, load balancers, etc.

Bonnes pratiques :
- Retourner un statut clair (200 OK si tout va bien)
- Ne jamais exposer d'informations sensibles dans la réponse
- Logger les checks échoués pour audit
- Prévoir l'extensibilité (vérification DB, cache, dépendances externes, etc.)
"""

from flask import Blueprint, jsonify
from datetime import datetime

bp = Blueprint("healthcheck", __name__, url_prefix="/api/health")

@bp.route("/", methods=["GET"])
def health_check():
    """
    Endpoint de healthcheck.
    Retourne 200 si le backend est opérationnel.
    """
    # Exemple d'extension : vérifier la DB, le cache, etc.
    status = {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    return jsonify(status), 200

# À intégrer dans votre app Flask principale :
# from backend.flask.app.monitoring.healthcheck import bp as healthcheck_bp
# app.register_blueprint(healthcheck_bp)