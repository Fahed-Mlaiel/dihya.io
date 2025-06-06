import importlib

def test_import_helpers_py():
    helpers = importlib.import_module('backend.components.metiers.threed.fixtures.helpers.helpers')
    assert helpers.get_model_by_id
    assert helpers.anonymize_fixture
    assert helpers.audit_fixture

def test_import_validators_py():
    validators = importlib.import_module('backend.components.metiers.threed.fixtures.helpers.validators')
    assert validators.is_valid_3d_model
    assert validators.is_valid_user
    assert validators.is_fixture_accessible
