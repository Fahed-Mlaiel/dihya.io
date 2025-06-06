"""
Tests ultra avancés pour guide_plugins.py (guides/core/plugins)
"""
from .guide_plugins import get_plugins_guide

def test_get_plugins_guide():
    guide = get_plugins_guide()
    assert isinstance(guide, dict)
    assert guide['title'] == 'Guide Plugins 3D'
    assert 'bestPractices' in guide
    assert 'integrationSteps' in guide
    assert 'Utiliser des plugins typés et documentés' in guide['bestPractices']
