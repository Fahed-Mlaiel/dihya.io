# Test Banque & Finance
def test_banque_finance():
    assert 'banque' in 'banque_finance'

def test_banque_finance_multilingue():
    from ..banque_finance import BanqueFinance
    from ..views import afficher_solde
    compte = BanqueFinance('FR12345678', 1000)
    assert 'Solde du compte' in afficher_solde(compte, 'fr')
    assert 'Account balance' in afficher_solde(compte, 'en')
    assert 'رصيد الحساب' in afficher_solde(compte, 'ar')

def test_banque_finance_rgpd():
    from ..banque_finance import BanqueFinance
    compte = BanqueFinance('FR12345678', 1000, owner='Alice', tenant='banque')
    export = compte.export_rgpd()
    assert export['owner'] == 'anonymisé'

def test_banque_finance_plugin():
    from ..plugins import accessibility_plugin
    banque = {'compte': 'FR12345678', 'solde': 1000, 'devise': 'EUR'}
    assert accessibility_plugin(banque) is True

def test_banque_finance_edge_case():
    from ..banque_finance import BanqueFinance
    compte = BanqueFinance('FR12345678', 0)
    try:
        compte.retrait(100)
        assert False, 'Doit lever une exception sur solde insuffisant'
    except ValueError:
        assert True
