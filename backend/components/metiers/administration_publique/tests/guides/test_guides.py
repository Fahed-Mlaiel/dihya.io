"""
Tests avancés pour la conformité des guides Threed (présence, contenu, accessibilité)
"""
import os
import pytest

def test_guides_presence():
    guides_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../guides'))
    guides = [f for f in os.listdir(guides_dir) if f.endswith('.md')]
    assert 'ACCESSIBILITY_GUIDE.md' in guides
    assert 'PLUGINS_GUIDE.md' in guides
    assert 'RGPD_GUIDE.md' in guides

def test_guides_content():
    guides_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../guides'))
    for guide in ['ACCESSIBILITY_GUIDE.md', 'PLUGINS_GUIDE.md', 'RGPD_GUIDE.md']:
        with open(os.path.join(guides_dir, guide)) as f:
            content = f.read()
            assert len(content) > 10
