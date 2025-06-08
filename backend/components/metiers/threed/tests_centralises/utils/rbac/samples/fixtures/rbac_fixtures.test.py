from .rbac_fixtures import rbac_fixtures

def test_admin_has_delete():
    assert 'delete' in rbac_fixtures['admin']['permissions']
