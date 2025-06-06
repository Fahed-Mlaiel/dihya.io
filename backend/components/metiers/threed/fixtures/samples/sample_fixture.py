"""
Exemple de fixture utilitaire pour helpers/core (Python)
"""
import pytest

@pytest.fixture
def sample_helper_fixture():
    return {"name": "Sample Helper", "type": "helper", "status": "active"}
