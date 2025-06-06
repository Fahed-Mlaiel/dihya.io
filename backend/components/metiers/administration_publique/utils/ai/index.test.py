"""
index.test.py – Test d’intégration du point d’entrée ai (Python)
"""
from . import ai_fallback

def test_index_ai():
    assert hasattr(ai_fallback, 'ai_fallback') or hasattr(ai_fallback, 'fallback_ai')
