"""
Initialisation du module de gestion des métriques personnalisées pour Dihya Coding.

Ce package centralise la déclaration, la collecte et l’exposition des métriques applicatives (performance, usage, sécurité, etc.)
pour le monitoring, l’alerting et l’amélioration continue du backend.

Bonnes pratiques :
- Déclarer chaque type de métrique dans un fichier dédié (ex : performance_metrics.py, usage_metrics.py, security_metrics.py).
- Documenter chaque métrique (but, unité, fréquence de collecte).
- Protéger l’accès aux endpoints d’exposition des métriques (authentification, IP whitelist, etc.).
- Ne jamais exposer de données sensibles ou personnelles dans les métriques.
- Prévoir des tests unitaires pour chaque collecteur de métriques.
- Intégrer avec des outils de monitoring (Prometheus, Grafana, etc.) si besoin.

Exemple d’import :
    from backend.flask.app.metrics.performance_metrics import record_response_time
    from backend.flask.app.metrics.usage_metrics import increment_api_call_count
    from backend.flask.app.metrics.security_metrics import increment_failed_login
"""

# Import des principaux collecteurs pour exposition directe (décommentez selon vos besoins)
# from .performance_metrics import record_response_time, get_performance_metrics, performance_metrics_blueprint
# from .usage_metrics import increment_api_call_count, get_usage_metrics, usage_metrics_blueprint
# from .security_metrics import increment_failed_login, get_security_metrics, security_metrics_blueprint