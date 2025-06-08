# Ultra advanced RBAC mock test (clé en main)
from .rbac_mocks import rbac_mocks

def test_test_user_has_test_permission():
    assert 'test' in rbac_mocks['test_user']['permissions']
