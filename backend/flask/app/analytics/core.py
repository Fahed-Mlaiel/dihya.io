"""
core.py — Analytics de base pour Dihya Coding (Flask)
Collecte, agrégation, anonymisation, RGPD, auditabilité.
"""
from flask import Blueprint, jsonify, request
import time

bp = Blueprint("analytics", __name__)

# Stockage en mémoire (à remplacer par une base ou un data lake en prod)
METRICS = {
    "requests": 0,
    "errors": 0,
    "latencies": [],
    "last_access": None
}

@bp.before_app_request
def before_request():
    METRICS["requests"] += 1
    METRICS["last_access"] = time.time()

@bp.route("/api/analytics/metrics", methods=["GET"])
def get_metrics():
    # Expose des métriques anonymisées, RGPD
    return jsonify({
        "requests": METRICS["requests"],
        "errors": METRICS["errors"],
        "avg_latency": sum(METRICS["latencies"])/len(METRICS["latencies"]) if METRICS["latencies"] else 0,
        "last_access": METRICS["last_access"]
    })
