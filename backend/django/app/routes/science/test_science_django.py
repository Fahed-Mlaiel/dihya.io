"""
Dihya – Tests pour le module Science
- Couverture RGPD, sécurité, accessibilité
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import ProjetScientifique, Publication, Chercheur
from rest_framework.test import APIClient
from rest_framework import status

class ScienceAPITestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='scienceuser', password='testpass', is_science_admin=True)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.projet = ProjetScientifique.objects.create(titre='Projet Test', description='Desc', date_debut='2025-01-01', date_fin='2025-12-31', responsable=self.user)

    def test_create_publication(self):
        data = {'projet': self.projet.id, 'titre': 'Publication Test', 'date_publication': '2025-06-01'}
        response = self.client.post('/api/science/publication/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['titre'], 'Publication Test')

    def test_permission_denied_for_non_admin(self):
        self.client.force_authenticate(user=None)
        response = self.client.post('/api/science/projetscientifique/', {'titre': 'X', 'description': 'Y', 'date_debut': '2025-01-01', 'date_fin': '2025-12-31'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
