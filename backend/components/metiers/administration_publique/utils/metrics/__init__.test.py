"""
__init__.test.py – Test d’import dynamique et d’intégration metrics (Python)
Conformité, CI/CD, audit, synchronisation JS/Python
"""
from . import metrics

def test_import_metrics():
    assert hasattr(metrics, 'track_metric') or hasattr(metrics, 'metrics')
