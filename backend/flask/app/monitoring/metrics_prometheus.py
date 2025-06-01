"""
Dihya – Exporteur Prometheus pour métriques backend Flask
Expose /metrics pour Prometheus (latence, requêtes, erreurs, RGPD)
"""
from flask import Blueprint, Response
import prometheus_client
from prometheus_client import Counter, Histogram, generate_latest

bp = Blueprint("metrics_prometheus", __name__)

REQUEST_COUNT = Counter('dihya_request_count', 'Nombre de requêtes', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('dihya_request_latency_seconds', 'Latence des requêtes', ['endpoint'])
ERROR_COUNT = Counter('dihya_error_count', 'Nombre d’erreurs', ['endpoint'])

@bp.route('/metrics')
def metrics():
    return Response(generate_latest(prometheus_client.REGISTRY), mimetype='text/plain')

# Exemple de hook à intégrer dans l’app Flask pour instrumenter les routes
# (à placer dans before_request/after_request)
