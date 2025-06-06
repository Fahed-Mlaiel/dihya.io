"""
Tests ultra avancés pour guide_fixtures.py (guides/core/fixtures/guides)
"""
from .guide_fixtures import get_fixtures_guide

def test_get_fixtures_guide():
    guide = get_fixtures_guide()
    assert isinstance(guide, dict)
    assert guide['title'] == 'Guide Fixtures 3D'
    assert 'bestPractices' in guide
    assert 'integrationSteps' in guide
    assert 'Utiliser des fixtures typées et documentées' in guide['bestPractices']
