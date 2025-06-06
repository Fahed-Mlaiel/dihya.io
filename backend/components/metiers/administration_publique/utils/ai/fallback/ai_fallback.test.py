# ai_fallback.test.py – Test unitaire ultra avancé fallback IA (Python)
from .ai_fallback import ai_fallback

def test_ai_fallback_ok():
    res = ai_fallback('input-non-traite')
    assert res['status'] == 'FALLBACK'
    assert res['data'] == 'input-non-traite'
    assert res['audit'] is True

def test_ai_fallback_error():
    res = ai_fallback(None)
    assert res['status'] == 'ERROR'
