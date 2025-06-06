"""
metrics.py – Collecte et reporting des métriques environnementales (Python)
"""
from collections import defaultdict

_metrics = defaultdict(list)

def record_metric(name, value):
    _metrics[name].append(value)

def get_average_metric(name):
    arr = _metrics[name]
    if not arr:
        return None
    return sum(arr) / len(arr)

def get_all_metrics():
    return dict(_metrics)
