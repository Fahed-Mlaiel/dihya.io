# fallback_plugins.test.py – Tests unitaires et edge cases Python
from .fallback_plugins import fallback_plugins

def test_fallback_plugins_structure():
    assert isinstance(fallback_plugins, dict)
    assert 'id' in fallback_plugins
    assert 'description' in fallback_plugins
