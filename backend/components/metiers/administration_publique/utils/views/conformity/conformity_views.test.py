"""
conformity_views.test.py – Tests unitaires conformité views threed (Python)
"""
from .conformity_views import check_rgpd, check_accessibility

def test_check_rgpd():
    assert check_rgpd({"nom": "Test"}) == (True, "Conforme RGPD")
    assert check_rgpd({"password": "123"})[0] is False

def test_check_accessibility():
    class View: lang = 'fr'
    assert check_accessibility(View()) == (True, "Accessible")
    class NoLang: pass
    assert check_accessibility(NoLang())[0] is False
