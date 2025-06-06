"""
Tests ultra avancés pour guide_accessibility.py (guides/core/accessibility/guides)
"""
from .guide_accessibility import get_accessibility_guide

def test_get_accessibility_guide():
    guide = get_accessibility_guide()
    assert isinstance(guide, dict)
    assert guide['title'] == 'Guide Accessibilité 3D'
    assert 'bestPractices' in guide
    assert 'integrationSteps' in guide
    assert 'Respecter les standards WCAG 2.1' in guide['bestPractices']
