import pytest
from backend.components.metiers.threed.api.rgpd.rgpd import rgpd_sanitize

def test_rgpd_sanitize():
    entity = {'id': 1, 'name': 'Test'}
    result = rgpd_sanitize(entity)
    assert result == entity
