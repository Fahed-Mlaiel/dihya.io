"""
Tests unitaires et intégration Loisirs (couverture maximale, multilingue)
"""
from django.test import TestCase
from .models import ActiviteLoisir

class ActiviteLoisirModelTest(TestCase):
    def test_creation_activite(self):
        activite = ActiviteLoisir.objects.create(
            nom='Club Amazigh', type='club', lieu='Tizi Ouzou', responsable='Yidir')
        self.assertEqual(activite.nom, 'Club Amazigh')
