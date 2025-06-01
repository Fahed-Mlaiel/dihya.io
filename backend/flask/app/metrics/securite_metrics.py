"""
Collecte et exposition des métriques de sécurité pour Dihya Coding.

Ce module centralise la collecte, l’incrémentation et l’exposition des métriques de sécurité applicative
(tentatives d’accès refusées, alertes, erreurs critiques, etc.) pour le monitoring, l’alerting et la conformité.

Bonnes pratiques :
- Documenter chaque métrique (but, unité, fréquence de collecte).
- Ne jamais exposer de données sensibles ou personnelles.
- Protéger l’accès aux endpoints d’exposition des métriques (authentification, IP whitelist, etc.).
- Logger toute anomalie ou pic inhabituel pour audit.
- Prévoir des tests unitaires pour chaque collecteur de métriques.

Exemple d’utilisation :
    from backend.flask.app.metrics.security_metrics import increment_failed_login, get_security_metrics

    increment_failed_login("user_123")
    metrics = get_security_metrics()
"""

import threading
from typing import Dict
from flask import Blueprint, jsonify, request, abort
import os

# Stockage en mémoire (à remplacer par Redis ou DB pour la prod)
_security_metrics = {
    "failed_logins": 0,
    "access_denied": 0,
    "alerts": [],
}
_metrics_lock = threading.Lock()

def increment_failed_login(user_id: str = None):
    """
    Incrémente le compteur de tentatives de connexion échouées.

    Args:
        user_id (str): ID utilisateur (optionnel, anonymisé si besoin).
    """
    with _metrics_lock:
        _security_metrics["failed_logins"] += 1

def increment_access_denied(user_id: str = None):
    """
    Incrémente le compteur d’accès refusés.

    Args:
        user_id (str): ID utilisateur (optionnel, anonymisé si besoin).
    """
    with _metrics_lock:
        _security_metrics["access_denied"] += 1

def add_security_alert(alert: str):
    """
    Ajoute une alerte de sécurité (ex : tentative d’injection, attaque détectée).

    Args:
        alert (str): Description de l’alerte.
    """
    with _metrics_lock:
        _security_metrics["alerts"].append(alert)

def get_security_metrics() -> Dict:
    """
    Retourne un snapshot des métriques de sécurité (anonymisées).

    Returns:
        dict: Métriques de sécurité.
    """
    with _metrics_lock:
        return {
            "failed_logins": _security_metrics["failed_logins"],
            "access_denied": _security_metrics["access_denied"],
            "alerts": list(_security_metrics["alerts"])[-10:],  # Dernières 10 alertes
        }

# Blueprint Flask pour exposer les métriques (à sécuriser en prod)
security_metrics_blueprint = Blueprint("security_metrics", __name__)

@security_metrics_blueprint.route("/metrics/security", methods=["GET"])
def security_metrics_endpoint():
    """
    Endpoint sécurisé pour exposer les métriques de sécurité.

    Sécurité :
    - Protéger par authentification ou IP whitelist en production.
    - Ne jamais exposer d’identifiants ou de données personnelles.

    Returns:
        JSON: Métriques de sécurité.
    """
    api_key = request.headers.get("X-API-KEY")
    expected_key = os.environ.get("METRICS_API_KEY")
    if not expected_key or api_key != expected_key:
        abort(403, "Accès non autorisé aux métriques.")
    return jsonify(get_security_metrics())