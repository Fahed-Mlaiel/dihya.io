# Test avancé pour conformity_utils.py du module utils/views/conformity
# from components.metiers.administration_publique.utils.views.conformity.conformity_utils
# import ...


from backend.components.metiers.administration_publique.utils.views.conformity import conformity_views


def test_utils_views_conformity():
    # Ajouter des assertions avancées selon la logique métier
    assert True


def test_check_rgpd_nominal():
    data = {"nom": "ok", "statut": "actif"}
    result, msg = conformity_views.check_rgpd(data)
    assert result is True
    assert "Conforme" in msg


def test_check_rgpd_forbidden():
    data = {"password": "123", "ssn": "000-00-0000"}
    result, msg = conformity_views.check_rgpd(data)
    assert result is False
    assert "Champs interdits" in msg


def test_check_accessibility_nominal():
    class DummyView:
        lang = "fr"

    result, msg = conformity_views.check_accessibility(DummyView())
    assert result is True
    assert "Accessible" in msg


def test_check_accessibility_missing_lang():
    class DummyView:
        pass

    result, msg = conformity_views.check_accessibility(DummyView())
    assert result is False
    assert "Langue non spécifiée" in msg
