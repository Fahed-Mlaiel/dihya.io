from .fixtures_advanced import fixtures_advanced

def test_superadmin_all_permissions():
    assert '*' in fixtures_advanced['superadmin']['permissions']
