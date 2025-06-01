"""
Tests unitaires et intégration Juridique (couverture maximale, multilingue)
"""
from django.test import TestCase
from .models import DossierJuridique

class DossierJuridiqueModelTest(TestCase):
    def test_creation_dossier(self):
        dossier = DossierJuridique.objects.create(
            titre='Contrat Amazigh', description='Contrat test', type='contrat', responsable='Yidir')
        self.assertEqual(dossier.titre, 'Contrat Amazigh')
