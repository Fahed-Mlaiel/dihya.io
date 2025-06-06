"""
index.test.py – Test d’intégration du point d’entrée exporter (Python)
"""
from . import exporter

def test_index_exporter():
    assert hasattr(exporter, 'export_data') or hasattr(exporter, 'exporter')
