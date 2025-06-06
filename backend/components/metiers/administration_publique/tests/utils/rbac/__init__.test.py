# __init__.test.py – Test d'import global du module rbac (Python)
from . import *

def test_import_rbac_utils():
    assert callable(has_permission)
    assert callable(get_user_permissions)
    assert isinstance(ROLES, list)
    assert isinstance(PERMISSIONS, dict)
