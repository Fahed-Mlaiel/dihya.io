"""
Tests centralisés pour les plugins threed (Python)
"""

from ...plugins import load_plugin, validate_plugin


def test_auth_plugin():
    plugin = load_plugin("auth")
    assert plugin is not None
    assert validate_plugin(plugin) is True


def test_invalid_plugin():
    invalid = {"name": "Fake", "hooks": []}
    assert validate_plugin(invalid) is False
