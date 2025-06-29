import pytest
from sante.api.controllers.sante_controller import SanteController
from sante.api.rgpd.rgpd import rgpd_sanitize

def test_validation_ordonnance():
    ordonnance = {"patient": "Alice", "medicament": "Doliprane", "valide": True}
    result = SanteController.valider_ordonnance(ordonnance)
    assert result is True

def test_rgpd_renforce():
    donnees = {"nom": "Alice", "email": "alice@exemple.com", "dossier": "secret"}
    donnees_rgpd = rgpd_sanitize(donnees)
    assert donnees_rgpd["nom"] == "***"
    assert donnees_rgpd["email"] == "***"