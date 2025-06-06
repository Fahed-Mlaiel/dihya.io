# Test du helper d’exemple (Python)
from .sample_helper import sample_helper
def test_sample_helper(capsys):
    assert sample_helper('exemple') is True
    captured = capsys.readouterr()
    assert '[HELPER] Exemple:' in captured.out
