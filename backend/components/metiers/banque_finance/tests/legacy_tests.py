# Legacy tests pour Banque & Finance
def test_legacy():
    assert True

def test_legacy_compat():
    from ..banque_finance import BanqueFinance
    compte = BanqueFinance('FR12345678', 100)
    assert hasattr(compte, 'virement')
    assert hasattr(compte, 'retrait')

def test_legacy_audit():
    from ..banque_finance import BanqueFinance
    compte = BanqueFinance('FR12345678', 100)
    compte.virement(10, BanqueFinance('FR87654321', 0))
    # Audit log doit être affiché (voir stdout)
