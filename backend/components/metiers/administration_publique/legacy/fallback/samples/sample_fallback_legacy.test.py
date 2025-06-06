# sample_fallback_legacy.test.py – Test Python exemple fallback legacy
from .sample_fallback_legacy import sample_fallback_legacy

def test_sample_fallback_legacy_ok():
    assert sample_fallback_legacy({'a': 1}) == {'a': 1, 'fallback': True}
    assert sample_fallback_legacy(None) == {'fallback': True, 'empty': True}
