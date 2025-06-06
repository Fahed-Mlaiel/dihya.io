import importlib

def test_import_helpers_index():
    helpers = importlib.import_module('backend.components.metiers.threed.fixtures.helpers.index')
    assert helpers is not None

def test_import_validators_index():
    validators = importlib.import_module('backend.components.metiers.threed.fixtures.helpers.validators')
    assert validators is not None
