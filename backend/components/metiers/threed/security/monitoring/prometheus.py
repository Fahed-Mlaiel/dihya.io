# prometheus.py – Export des métriques sécurité

def export_metrics():
    # Exemple d’export Prometheus
    print("# HELP security_access_denied_total Nombre d'accès refusés")
    print("security_access_denied_total 0")
