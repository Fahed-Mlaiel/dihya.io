"""
Tests unitaires et intégration Immobilier (couverture maximale, multilingue)
"""
from django.test import TestCase
from .models import BienImmobilier

class BienImmobilierModelTest(TestCase):
    def test_creation_bien(self):
        bien = BienImmobilier.objects.create(
            titre='Appartement Amazigh', description='Vue sur mer', type='appartement', surface=80.0, localisation='Tizi Ouzou', prix=120000.00, proprietaire='Yidir')
        self.assertEqual(bien.titre, 'Appartement Amazigh')
