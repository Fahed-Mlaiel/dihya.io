# helpers_monitoring.py
# Helpers avancés pour la supervision, alertes, dashboards

def send_alert(message):
    """Simule l'envoi d'une alerte"""
    print(f"[MONITORING ALERT] {message}")

def generate_dashboard(metrics):
    """Simule la génération d'un dashboard"""
    return f"Dashboard: {', '.join(metrics.keys())}"
