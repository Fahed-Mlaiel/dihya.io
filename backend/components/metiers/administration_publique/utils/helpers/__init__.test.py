"""
__init__.test.py – Test d’import dynamique et d’intégration helpers (Python)
"""
from . import utils_helper
from . import core, helpers, fallback, samples

def test_import_helpers():
    assert hasattr(utils_helper, 'helper_function') or hasattr(utils_helper, 'utils_helper')

def test_import_helpers_all():
    assert hasattr(core, 'utils_helper')
    assert hasattr(helpers, 'generic_helper')
    assert hasattr(fallback, 'fallback')
    assert hasattr(samples, 'sample_helper')
