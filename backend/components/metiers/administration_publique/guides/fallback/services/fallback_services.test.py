# fallback_services.test.py – Tests unitaires et edge cases Python
from .fallback_services import fallback_services

def test_fallback_services_structure():
    assert isinstance(fallback_services, dict)
    assert 'id' in fallback_services
    assert 'description' in fallback_services
