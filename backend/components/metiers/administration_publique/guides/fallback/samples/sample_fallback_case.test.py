# sample_fallback_case.test.py – Tests unitaires et edge cases Python
from .sample_fallback_case import sample_fallback_case

def test_sample_fallback_case_structure():
    assert isinstance(sample_fallback_case, dict)
    assert 'id' in sample_fallback_case
    assert 'description' in sample_fallback_case
    assert 'status' in sample_fallback_case

def test_sample_fallback_case_status():
    assert sample_fallback_case['status'] in ['compliant', 'partial', 'non-compliant']
