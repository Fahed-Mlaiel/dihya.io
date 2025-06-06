# sample_helper_legacy.test.py – Test Python exemple helper legacy
from .sample_helper_legacy import sample_helper_legacy

def test_sample_helper_legacy_ok():
    assert sample_helper_legacy({'a': 1}) == {'a': 1, 'helper': True}
    assert sample_helper_legacy(None) == {'helper': True, 'empty': True}
