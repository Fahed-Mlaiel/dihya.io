"""
index.test.py – Test d’intégration du point d’entrée i18n (Python)
"""
from . import i18n

def test_index_i18n():
    assert hasattr(i18n, 'translate') or hasattr(i18n, 'i18n')
