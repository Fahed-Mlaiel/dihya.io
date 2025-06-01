"""
Module de metrics pour Dihya Coding.

Ce module expose des métriques de performance et d'usage pour le backend,
compatibles avec les outils de monitoring modernes (Prometheus, Grafana, etc.).
Permet de suivre la santé, la charge et l'utilisation de l'API.

Bonnes pratiques :
- Ne jamais exposer de données sensibles dans les métriques
- Prévoir l'extensibilité (ajout de nouvelles métriques facilement)
- Compatible Prometheus (format texte)
- Sécuriser l'accès à l'endpoint en production (IP whitelist, auth, etc.)
"""

from flask import Blueprint, Response, request
from datetime import datetime
import platform
import os
import psutil

bp = Blueprint("metrics", __name__, url_prefix="/api/metrics")

def collect_metrics():
    """
    Collecte des métriques système et applicatives.
    À étendre selon les besoins métier.
    """
    process = psutil.Process(os.getpid())
    metrics = [
        f'# HELP dihya_backend_up 1 si le backend répond',
        f'# TYPE dihya_backend_up gauge',
        f'dihya_backend_up 1',
        f'# HELP dihya_backend_requests_total Nombre total de requêtes traitées',
        f'# TYPE dihya_backend_requests_total counter',
        # À remplacer par un vrai compteur global si besoin
        f'dihya_backend_requests_total 1',
        f'# HELP dihya_backend_python_version Version de Python utilisée',
        f'# TYPE dihya_backend_python_version gauge',
        f'dihya_backend_python_version{{version="{platform.python_version()}"}} 1',
        f'# HELP dihya_backend_memory_usage_bytes Mémoire utilisée par le process (bytes)',
        f'# TYPE dihya_backend_memory_usage_bytes gauge',
        f'dihya_backend_memory_usage_bytes {process.memory_info().rss}',
        f'# HELP dihya_backend_cpu_usage_percent CPU utilisé par le process (%)',
        f'# TYPE dihya_backend_cpu_usage_percent gauge',
        f'dihya_backend_cpu_usage_percent {process.cpu_percent(interval=0.1)}',
        f'# HELP dihya_backend_timestamp_utc Timestamp de la collecte',
        f'# TYPE dihya_backend_timestamp_utc gauge',
        f'dihya_backend_timestamp_utc {int(datetime.utcnow().timestamp())}',
    ]
    return "\n".join(metrics) + "\n"

@bp.route("/", methods=["GET"])
def metrics():
    """
    Endpoint Prometheus pour exposer les métriques backend.
    À sécuriser en production (IP whitelist, auth, etc.).
    """
    # Exemple de restriction d'accès (à adapter)
    allowed_ips = ["127.0.0.1", "::1"]
    if request.remote_addr not in allowed_ips:
        return Response("Forbidden", status=403)
    metrics_data = collect_metrics()
    return Response(metrics_data, mimetype="text/plain")

# À intégrer dans votre app Flask principale :
# from backend.flask.app.monitoring.metrics import bp as metrics_bp
# app.register_blueprint(metrics_bp)