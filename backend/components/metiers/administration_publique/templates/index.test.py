# index.test.py – Test d’intégration du point d’entrée Python pour templates Threed
import importlib
import pytest

entry = importlib.import_module('backend.components.metiers.threed.templates.index')

def test_helpers_exposes():
    assert hasattr(entry, 'render_template')
    assert hasattr(entry, 'is_valid_template')
    assert hasattr(entry, 'mock_template_context')

def test_validators_exposes():
    assert hasattr(entry, 'is_valid_template_file')
    assert hasattr(entry, 'validate_template_content')
