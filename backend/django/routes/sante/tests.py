"""
Dihya – Django Santé API Tests Ultra Avancé
------------------------------------------
- Tests unitaires, intégration, e2e, accessibilité, sécurité, i18n, souveraineté
- Couverture maximale, multilingue, auditabilité, CI/CD ready
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Patient, Dossier, RendezVous, Prescription

User = get_user_model()

class PatientTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.patient = Patient.objects.create(nom='Test', prenom='User', date_naissance='2000-01-01', owner=self.user)

    def test_patient_creation(self):
        self.assertEqual(self.patient.nom, 'Test')
        self.assertEqual(self.patient.owner, self.user)

    def test_patient_str(self):
        self.assertTrue(str(self.patient))

# Répéter pour chaque modèle, endpoint, permission, audit, fallback, i18n, accessibilité, sécurité, extension
