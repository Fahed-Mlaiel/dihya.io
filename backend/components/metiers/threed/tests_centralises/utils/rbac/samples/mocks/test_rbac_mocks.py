from .rbac_mocks import rbac_mocks

def test_guest_has_no_permissions():
    assert rbac_mocks['guest']['permissions'] == []
