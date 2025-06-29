import pytest
from sante.api.rgpd.rgpd import rgpd_sanitize

# Tests métier pour Santé

@pytest.mark.parametrize("cas_usage, attendu", [
    ("RGPD renforcé", True),
    ("Validation ordonnance obligatoire", True),
])
def test_cas_usage(cas_usage, attendu):
    # TODO: Implémenter la logique métier pour chaque cas d'usage
    assert attendu  # Remplacer par la vraie vérification

def test_anonymisation_rgpd():
    donnees = {"nom": "Bob", "email": "bob@exemple.com", "dossier": "secret"}
    donnees_rgpd = rgpd_sanitize(donnees)
    assert donnees_rgpd["nom"] == "***"
    assert donnees_rgpd["email"] == "***"
    assert donnees_rgpd["dossier"] == "secret"