"""
__init__.test.py – Test d’import dynamique et d’intégration exporter (Python)
"""
from . import exporter
from . import core, helpers, fallback, samples

def test_import_exporter():
    assert hasattr(exporter, 'export_data') or hasattr(exporter, 'exporter')

def test_import_exporter_all():
    assert hasattr(core, 'exporter') or hasattr(core, 'export_data')
    assert hasattr(helpers, 'exporter_helper')
    assert hasattr(fallback, 'fallback')
    assert hasattr(samples, 'sample_export')
