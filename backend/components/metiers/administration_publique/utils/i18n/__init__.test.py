"""
__init__.test.py – Test d’import dynamique et d’intégration i18n (Python)
"""
from . import i18n
from . import core, helpers, fallback, samples

def test_import_i18n():
    assert hasattr(i18n, 'translate') or hasattr(i18n, 'i18n')

def test_import_i18n_all():
    assert hasattr(core, 'i18n')
    assert hasattr(helpers, 'i18n_helper')
    assert hasattr(fallback, 'fallback')
    assert hasattr(samples, 'sample_i18n')
