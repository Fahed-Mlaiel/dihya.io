"""
Collecte et exposition des métriques de performance pour Dihya Coding.

Ce module centralise la collecte, l’agrégation et l’exposition des métriques de performance applicative
(temps de réponse, latence, taux d’erreur, etc.) pour le monitoring, l’alerting et l’amélioration continue.

Bonnes pratiques :
- Documenter chaque métrique (but, unité, fréquence de collecte).
- Ne jamais exposer de données sensibles ou personnelles.
- Protéger l’accès aux endpoints d’exposition des métriques (authentification, IP whitelist, etc.).
- Logger toute anomalie ou pic inhabituel pour audit.
- Prévoir des tests unitaires pour chaque collecteur de métriques.

Exemple d’utilisation :
    from backend.flask.app.metrics.performance_metrics import record_response_time, get_performance_metrics

    record_response_time("/api/generate", 120)
    metrics = get_performance_metrics()
"""

import threading
from typing import Dict
from flask import Blueprint, jsonify, request, abort
import os
import time

# Stockage en mémoire (à remplacer par Redis ou DB pour la prod)
_performance_metrics = {
    "response_times": {},  # endpoint: [durées en ms]
    "error_rates": {},     # endpoint: nombre d'erreurs
    "total_requests": {},  # endpoint: nombre total de requêtes
}
_metrics_lock = threading.Lock()

def record_response_time(endpoint: str, duration_ms: float, error: bool = False):
    """
    Enregistre le temps de réponse d’un endpoint.

    Args:
        endpoint (str): Nom ou chemin de l’endpoint.
        duration_ms (float): Durée en millisecondes.
        error (bool): Indique si la requête a échoué.
    """
    with _metrics_lock:
        _performance_metrics["response_times"].setdefault(endpoint, []).append(duration_ms)
        _performance_metrics["total_requests"].setdefault(endpoint, 0)
        _performance_metrics["total_requests"][endpoint] += 1
        if error:
            _performance_metrics["error_rates"].setdefault(endpoint, 0)
            _performance_metrics["error_rates"][endpoint] += 1

def get_performance_metrics() -> Dict:
    """
    Retourne un snapshot des métriques de performance (anonymisées).

    Returns:
        dict: Métriques de performance (moyenne, max, taux d’erreur par endpoint).
    """
    with _metrics_lock:
        metrics = {}
        for endpoint, times in _performance_metrics["response_times"].items():
            total = _performance_metrics["total_requests"].get(endpoint, 1)
            errors = _performance_metrics["error_rates"].get(endpoint, 0)
            avg = sum(times) / len(times) if times else 0
            metrics[endpoint] = {
                "avg_response_time_ms": round(avg, 2),
                "max_response_time_ms": max(times) if times else 0,
                "min_response_time_ms": min(times) if times else 0,
                "total_requests": total,
                "error_rate": round(errors / total, 4) if total else 0,
            }
        return metrics

# Blueprint Flask pour exposer les métriques (à sécuriser en prod)
performance_metrics_blueprint = Blueprint("performance_metrics", __name__)

@performance_metrics_blueprint.route("/metrics/performance", methods=["GET"])
def performance_metrics_endpoint():
    """
    Endpoint sécurisé pour exposer les métriques de performance.

    Sécurité :
    - Protéger par authentification ou IP whitelist en production.
    - Ne jamais exposer d’identifiants ou de données personnelles.

    Returns:
        JSON: Métriques de performance.
    """
    api_key = request.headers.get("X-API-KEY")
    expected_key = os.environ.get("METRICS_API_KEY")
    if not expected_key or api_key != expected_key:
        abort(403, "Accès non autorisé aux métriques.")
    return jsonify(get_performance_metrics())