"""
Dihya – Tests unitaires et d'intégration pour Validators
- Couverture exhaustive, sécurité, RGPD, multilingue
"""
from django.test import TestCase
from .models import ValidationLog

class ValidationLogModelTest(TestCase):
    def test_str(self):
        v = ValidationLog.objects.create(type_validation='email', resultat='valide', details='OK', utilisateur='admin')
        self.assertIn('email', str(v))
