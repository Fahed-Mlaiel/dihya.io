import importlib

def test_is_valid_3d_model():
    validators = importlib.import_module('backend.components.metiers.threed.fixtures.helpers.validators')
    assert validators.is_valid_3d_model({'id': 'x', 'vertices': []})
    assert not validators.is_valid_3d_model({'id': 1, 'vertices': None})

def test_is_valid_user():
    validators = importlib.import_module('backend.components.metiers.threed.fixtures.helpers.validators')
    assert validators.is_valid_user({'id': 'u', 'role': 'admin'})
    assert not validators.is_valid_user({'id': 1, 'role': None})

def test_is_fixture_accessible():
    validators = importlib.import_module('backend.components.metiers.threed.fixtures.helpers.validators')
    assert validators.is_fixture_accessible({'description': 'ok'})
    assert not validators.is_fixture_accessible({'description': 123})
