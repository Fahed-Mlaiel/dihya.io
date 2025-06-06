"""
__init__.test.py – Test d’import dynamique et d’intégration ai (Python)
"""
from . import ai_fallback

def test_import_ai():
    assert hasattr(ai_fallback, 'ai_fallback') or hasattr(ai_fallback, 'fallback_ai')

def test_import_init():
    import importlib
    mod = importlib.import_module('utils.ai.__init__')
    assert mod is not None
