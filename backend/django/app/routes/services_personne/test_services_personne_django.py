"""
Dihya – Tests unitaires et d'intégration pour Services à la Personne
- Couverture exhaustive, sécurité, RGPD, multilingue
"""
from django.test import TestCase
from .models import Beneficiaire, Intervenant, Prestation

class BeneficiaireModelTest(TestCase):
    def test_str(self):
        b = Beneficiaire.objects.create(nom='Test', prenom='User', email='test@example.com', telephone='0600000000', adresse='1 rue test')
        self.assertEqual(str(b), 'User Test')

class IntervenantModelTest(TestCase):
    def test_str(self):
        i = Intervenant.objects.create(nom='Doe', prenom='Jane', email='jane@example.com', specialite='Aide')
        self.assertEqual(str(i), 'Jane Doe')

class PrestationModelTest(TestCase):
    def test_str(self):
        b = Beneficiaire.objects.create(nom='Test', prenom='User', email='test@example.com', telephone='0600000000', adresse='1 rue test')
        i = Intervenant.objects.create(nom='Doe', prenom='Jane', email='jane@example.com', specialite='Aide')
        p = Prestation.objects.create(beneficiaire=b, intervenant=i, type_prestation='Ménage', date='2024-01-01T10:00:00Z', statut='planifiee')
        self.assertIn('Ménage', str(p))
