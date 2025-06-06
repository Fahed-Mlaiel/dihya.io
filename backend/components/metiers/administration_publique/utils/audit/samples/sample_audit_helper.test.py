# Test du helper d’audit d’exemple (Python)
from .sample_audit_helper import sample_audit_log
def test_sample_audit_log(capsys):
    assert sample_audit_log('user123', 'LOGIN') is True
    captured = capsys.readouterr()
    assert '[AUDIT] Utilisateur: user123, Action: LOGIN' in captured.out
