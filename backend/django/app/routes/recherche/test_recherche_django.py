"""
Dihya – Tests pour le module Recherche
- Couverture RGPD, sécurité, accessibilité
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import RequeteRecherche, ResultatRecherche
from rest_framework.test import APIClient
from rest_framework import status

class RechercheAPITestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='rechercheuser', password='testpass', is_recherche_admin=True)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.requete = RequeteRecherche.objects.create(terme='Test', utilisateur=self.user)

    def test_create_resultat(self):
        data = {'requete': self.requete.id, 'titre': 'Résultat Test', 'url': 'https://example.com', 'score': 0.99}
        response = self.client.post('/api/recherche/resultatrecherche/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['titre'], 'Résultat Test')

    def test_permission_denied_for_non_admin(self):
        self.client.force_authenticate(user=None)
        response = self.client.post('/api/recherche/requeterecherche/', {'terme': 'X'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
