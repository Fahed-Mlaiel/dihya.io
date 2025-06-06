# Test du helper logger d’exemple (Python, clé en main)
from .sample_logger_helper import sample_logger_helper
def test_sample_logger_helper(capsys):
    assert sample_logger_helper('clé en main') is True
    captured = capsys.readouterr()
    assert '[LOGGER SAMPLE] Exemple:' in captured.out
