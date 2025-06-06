# Test du helper JS d’exemple (Python, clé en main)
from .sample_js_helper import sample_js_helper
def test_sample_js_helper(capsys):
    assert sample_js_helper('clé en main') is True
    captured = capsys.readouterr()
    assert '[JS SAMPLE] Exemple:' in captured.out
