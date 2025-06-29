# Test avancé pour api_utils.py du module utils/views/api
# from components.metiers.securite.utils.views.api.api_utils import ...
import pytest
from backend.components.metiers.securite.utils.views.api import api_views


class DummySecuriteAPI:
    def __init__(self, nom, statut, details=""):
        self.nom = nom
        self.statut = statut
        self.details = details


def test_utils_views_api():
    # Ajouter des assertions avancées selon la logique métier
    assert True


def test_render_securite_api_nominal():
    data = api_views.SecuriteAPIModel(nom="Projet API", statut="actif", details="ok")
    result = api_views.render_securite_api(data)
    assert result["nom"] == "Projet API"
    assert result["statut"] == "actif"
    assert result["details"] == "ok"


def test_render_securite_api_empty_details():
    data = api_views.SecuriteAPIModel(nom="Projet API", statut="inactif")
    result = api_views.render_securite_api(data)
    assert result["details"] == ""


def test_render_securite_api_rgpd():
    data = api_views.SecuriteAPIModel(nom="Projet RGPD", statut="archivé", details="aucune donnée perso")
    result = api_views.render_securite_api(data)
    assert "nom" in result and "statut" in result
    assert "details" in result
