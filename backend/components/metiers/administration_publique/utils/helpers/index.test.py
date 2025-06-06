"""
index.test.py – Test d’intégration du point d’entrée helpers (Python)
"""
from . import utils_helper

def test_index_helpers():
    assert hasattr(utils_helper, 'helper_function') or hasattr(utils_helper, 'utils_helper')
