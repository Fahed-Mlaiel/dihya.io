# test_mock_helper_advanced.py – Tests ultra avancés pour mock_helper.py (helpers/mocks)
from backend.components.metiers.vr_ar.utils.helpers.mocks.mock_helper import mock_validation_data

def test_mock_validation_data_conforme():
    mock = mock_validation_data()
    assert 'id' in mock
    assert 'user' in mock
    assert 'email' in mock
    assert 'consent' in mock
    assert 'timestamp' in mock
    assert isinstance(mock['timestamp'], str)

def test_mock_validation_data_auditabilite():
    mock = mock_validation_data()
    assert len(mock['timestamp']) > 10

def test_mock_validation_data_accessibilite():
    mock = mock_validation_data()
    assert mock['user'] == 'mocked'
    assert '@' in mock['email']
