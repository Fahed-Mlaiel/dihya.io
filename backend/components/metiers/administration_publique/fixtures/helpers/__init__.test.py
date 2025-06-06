import importlib

def test_import_helpers_init():
    helpers = importlib.import_module('backend.components.metiers.threed.fixtures.helpers.helpers')
    assert helpers is not None

def test_import_validators_init():
    validators = importlib.import_module('backend.components.metiers.threed.fixtures.helpers.validators')
    assert validators is not None
