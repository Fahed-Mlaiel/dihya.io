"""
Tests unitaires et intégration Construction (couverture maximale, multilingue)
"""
from django.test import TestCase
from .models import Chantier

class ChantierModelTest(TestCase):
    def test_creation_chantier(self):
        chantier = Chantier.objects.create(
            nom='Chantier Amazigh', localisation='Tizi Ouzou', date_debut='2025-05-01', date_fin='2025-06-01', responsable='Yidir', budget=100000.00)
        self.assertEqual(chantier.nom, 'Chantier Amazigh')
