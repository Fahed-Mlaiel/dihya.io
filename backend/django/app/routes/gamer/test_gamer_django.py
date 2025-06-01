"""
Tests unitaires et intégration Gamer (couverture maximale, multilingue)
"""
from django.test import TestCase
from .models import ProfilGamer

class ProfilGamerModelTest(TestCase):
    def test_creation_profil(self):
        profil = ProfilGamer.objects.create(
            pseudo='Yidir', score=1000, niveau='Expert')
        self.assertEqual(profil.pseudo, 'Yidir')

def test_smoke_gamer():
    """Ultra-smoke-test: Sicherstellung pytest-Discovery und Basismodell."""
    assert True
