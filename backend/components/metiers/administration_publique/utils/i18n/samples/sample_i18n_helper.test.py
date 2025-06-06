# Test du helper i18n d’exemple (Python)
from .sample_i18n_helper import sample_i18n
def test_sample_i18n(capsys):
    assert sample_i18n('fr', 'Bonjour') is True
    captured = capsys.readouterr()
    assert '[I18N] [fr] Bonjour' in captured.out
