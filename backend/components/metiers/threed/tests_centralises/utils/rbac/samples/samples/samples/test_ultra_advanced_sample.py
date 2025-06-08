# Ultra advanced RBAC sample test (clé en main)
from .sample_advanced import sample_advanced

def test_backup_admin_role():
    assert sample_advanced['role'] == 'backup_admin'
