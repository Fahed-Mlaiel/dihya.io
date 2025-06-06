"""
Test d'import du module accessibility (Python)
"""
import importlib

def test_import_accessibility():
    guides = importlib.import_module('.guides', __package__)
    samples = importlib.import_module('.samples', __package__)
    assert hasattr(guides, 'get_accessibility_guide') or hasattr(guides, 'getAccessibilityGuide')
    assert hasattr(samples, 'sample_accessibility_guide') or hasattr(samples, 'sample')
