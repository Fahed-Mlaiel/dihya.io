"""
index.test.py – Test d’intégration du point d’entrée logger (Python)
"""
from . import logger

def test_index_logger():
    assert hasattr(logger, 'log') or hasattr(logger, 'logger')
