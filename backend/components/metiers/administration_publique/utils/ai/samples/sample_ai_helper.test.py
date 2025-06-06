# sample_ai_helper.test.py – Test unitaire ultra avancé sample helper IA (Python)
from .sample_ai_helper import sample_ai_helper

def test_sample_ai_helper_ok():
    res = sample_ai_helper('foo')
    assert res['status'] == 'SAMPLE'
    assert res['data'] == 'foo'
    assert res['audit'] is True

def test_sample_ai_helper_error():
    res = sample_ai_helper(None)
    assert res['status'] == 'ERROR'
