# Test du helper d’export d’exemple (Python)
from .sample_exporter_helper import sample_export
def test_sample_export(capsys):
    assert sample_export({'id': 1, 'name': 'Test'}) is True
    captured = capsys.readouterr()
    assert '[EXPORT] Données exportées:' in captured.out
