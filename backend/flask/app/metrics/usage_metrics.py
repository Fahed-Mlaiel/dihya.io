"""
Collecte et exposition des métriques d’usage pour Dihya Coding.

Ce module centralise la collecte, l’incrémentation et l’exposition des métriques d’usage applicatif
(nombre d’appels API, utilisateurs actifs, endpoints utilisés, etc.) pour le monitoring, l’alerting et l’amélioration continue.

Bonnes pratiques :
- Documenter chaque métrique (but, unité, fréquence de collecte).
- Ne jamais exposer de données sensibles ou personnelles.
- Protéger l’accès aux endpoints d’exposition des métriques (authentification, IP whitelist, etc.).
- Logger les anomalies ou pics inhabituels pour audit.
- Prévoir des tests unitaires pour chaque collecteur de métriques.

Exemple d’utilisation :
    from backend.flask.app.metrics.usage_metrics import increment_api_call_count, get_usage_metrics

    increment_api_call_count("user_123")
    metrics = get_usage_metrics()
"""

import threading
from typing import Dict
from flask import Blueprint, jsonify, request, abort
import os

# Stockage en mémoire (à remplacer par Redis ou DB pour la prod)
_usage_metrics = {
    "api_calls": 0,
    "users": set(),
    "endpoints": {},
}
_metrics_lock = threading.Lock()

def increment_api_call_count(user_id: str, endpoint: str = None):
    """
    Incrémente le compteur d’appels API et enregistre l’utilisateur et l’endpoint.

    Args:
        user_id (str): ID utilisateur (anonymisé ou hashé si besoin).
        endpoint (str): Endpoint appelé (optionnel).
    """
    with _metrics_lock:
        _usage_metrics["api_calls"] += 1
        if user_id:
            _usage_metrics["users"].add(user_id)
        if endpoint:
            _usage_metrics["endpoints"].setdefault(endpoint, 0)
            _usage_metrics["endpoints"][endpoint] += 1

def get_usage_metrics() -> Dict:
    """
    Retourne un snapshot des métriques d’usage (anonymisées).

    Returns:
        dict: Métriques d’usage (nombre d’appels, utilisateurs uniques, endpoints).
    """
    with _metrics_lock:
        return {
            "api_calls": _usage_metrics["api_calls"],
            "unique_users": len(_usage_metrics["users"]),
            "endpoints": dict(_usage_metrics["endpoints"]),
        }

# Blueprint Flask pour exposer les métriques (à sécuriser en prod)
usage_metrics_blueprint = Blueprint("usage_metrics", __name__)

@usage_metrics_blueprint.route("/metrics/usage", methods=["GET"])
def usage_metrics_endpoint():
    """
    Endpoint sécurisé pour exposer les métriques d’usage.

    Sécurité :
    - Protéger par authentification ou IP whitelist en production.
    - Ne jamais exposer d’identifiants ou de données personnelles.

    Returns:
        JSON: Métriques d’usage.
    """
    # Exemple de protection simple par clé API (à renforcer en prod)
    api_key = request.headers.get("X-API-KEY")
    expected_key = os.environ.get("METRICS_API_KEY")
    if not expected_key or api_key != expected_key:
        abort(403, "Accès non autorisé aux métriques.")
    return jsonify(get_usage_metrics())