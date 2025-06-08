from .sample_advanced import sample_advanced

def test_auditor_role():
    assert sample_advanced['role'] == 'auditor'
