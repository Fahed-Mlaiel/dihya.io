import pytest
from .core_legacy import metier_legacy_core

def test_metier_legacy_core_ok():
    assert metier_legacy_core({'a': 1}) == {'a': 1, 'legacy': True}

def test_metier_legacy_core_fail():
    with pytest.raises(ValueError):
        metier_legacy_core(None)
