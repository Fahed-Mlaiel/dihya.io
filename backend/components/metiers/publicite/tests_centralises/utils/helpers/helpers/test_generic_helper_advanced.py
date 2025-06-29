# test_generic_helper_advanced.py – Tests ultra avancés pour generic_helper.py (helpers/helpers)
from backend.components.metiers.publicite.utils.helpers.mocks.mock_helper import mock_validation_data
from backend.components.metiers.publicite.utils.helpers.helpers.generic_helper import capitalize_first

def test_mock_validation_data_helpers():
    mock = mock_validation_data()
    assert 'id' in mock
    assert 'user' in mock
    assert 'email' in mock
    assert 'consent' in mock
    assert 'timestamp' in mock

def test_mock_validation_data_helpers_auditabilite():
    mock = mock_validation_data()
    assert len(mock['timestamp']) > 10

def test_capitalize_first():
    assert capitalize_first('dihya') == 'Dihya'

def test_capitalize_first_empty():
    assert capitalize_first('') == ''
    assert capitalize_first(None) == ''

def test_capitalize_first_special():
    assert capitalize_first('élise') == 'Élise'

def test_capitalize_first_type():
    assert isinstance(capitalize_first('test'), str)
