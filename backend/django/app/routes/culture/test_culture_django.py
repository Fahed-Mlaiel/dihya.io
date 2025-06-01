"""
Tests unitaires et intégration Culture (couverture maximale, multilingue)
"""
from django.test import TestCase
from .models import EvenementCulturel

class EvenementCulturelModelTest(TestCase):
    def test_creation_evenement(self):
        evt = EvenementCulturel.objects.create(
            titre='Festival Amazigh', description='Culture et musique', date='2025-07-01', lieu='Tizi Ouzou', organisateur='Yidir')
        self.assertEqual(evt.titre, 'Festival Amazigh')
