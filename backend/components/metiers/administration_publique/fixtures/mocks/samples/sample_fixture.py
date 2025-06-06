"""
Exemple de fixture pour le module Threed (3D)
"""
import pytest

@pytest.fixture
def sample_3d_fixture():
    return {"name": "Sample 3D", "type": "model", "status": "active"}
