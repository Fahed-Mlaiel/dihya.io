# Ultra advanced RBAC fixture test (clé en main)
from .rbac_fixtures import rbac_fixtures

def test_compliance_officer_has_audit():
    assert 'audit' in rbac_fixtures['compliance_officer']['permissions']
