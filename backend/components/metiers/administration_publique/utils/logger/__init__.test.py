"""
__init__.test.py – Test d’import dynamique et d’intégration logger (Python)
"""
from . import logger

def test_import_logger():
    assert hasattr(logger, 'log') or hasattr(logger, 'logger')
