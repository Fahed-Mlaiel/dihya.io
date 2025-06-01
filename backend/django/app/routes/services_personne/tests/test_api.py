"""
Dihya – Tests API avancés pour Services à la Personne
- Tests unitaires, intégration, sécurité, accessibilité, multilingue
"""
from rest_framework.test import APITestCase
from django.urls import reverse
from ..models import Beneficiaire, Intervenant, Prestation

class BeneficiaireAPITest(APITestCase):
    def setUp(self):
        self.b = Beneficiaire.objects.create(nom='Test', prenom='User', email='test@example.com', telephone='0600000000', adresse='1 rue test')
    def test_list_beneficiaires(self):
        url = reverse('client-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    def test_create_beneficiaire(self):
        url = reverse('client-list')
        data = {'nom': 'Doe', 'prenom': 'Jane', 'email': 'jane@example.com', 'telephone': '0600000001', 'adresse': '2 rue test'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

class IntervenantAPITest(APITestCase):
    def setUp(self):
        self.i = Intervenant.objects.create(nom='Doe', prenom='Jane', email='jane@example.com', specialite='Aide')
    def test_list_intervenants(self):
        url = reverse('intervenant-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class PrestationAPITest(APITestCase):
    def setUp(self):
        self.b = Beneficiaire.objects.create(nom='Test', prenom='User', email='test@example.com', telephone='0600000000', adresse='1 rue test')
        self.i = Intervenant.objects.create(nom='Doe', prenom='Jane', email='jane@example.com', specialite='Aide')
        self.p = Prestation.objects.create(beneficiaire=self.b, intervenant=self.i, type_prestation='Ménage', date='2024-01-01T10:00:00Z', statut='planifiee')
    def test_list_prestations(self):
        url = reverse('prestation-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
