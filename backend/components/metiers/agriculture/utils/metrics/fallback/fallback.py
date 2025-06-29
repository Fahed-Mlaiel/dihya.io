# fallback.py
# Fallback metrics Python pour Agriculture – exemple clé en main
from datetime import datetime

fallback_metrics = []


def metrics_fallback(name, value):
    """
    Fallback minimal : stocke une métrique en mémoire si la persistance échoue
    """
    metric = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "name": name,
        "value": value,
    }
    fallback_metrics.append(metric)
    return metric
