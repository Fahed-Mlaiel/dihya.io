"""
index.test.py – Test d’intégration du point d’entrée metrics (Python)
Conformité, CI/CD, audit, synchronisation JS/Python
"""
from . import metrics

def test_index_metrics():
    assert hasattr(metrics, 'track_metric') or hasattr(metrics, 'metrics')
