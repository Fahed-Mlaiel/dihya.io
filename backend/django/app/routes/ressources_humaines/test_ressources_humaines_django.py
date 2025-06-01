"""
Dihya – Tests pour le module Ressources Humaines
- Couverture RGPD, sécurité, accessibilité
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Employe, Poste, Candidature
from rest_framework.test import APIClient
from rest_framework import status

class RHAPITestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='rhuser', password='testpass', is_rh_admin=True)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.poste = Poste.objects.create(titre='Développeur', ouvert=True)
        self.employe = Employe.objects.create(nom='Doe', prenom='John', email='john.doe@example.com', poste='Développeur', date_embauche='2025-01-01', manager=self.user)

    def test_create_candidature(self):
        data = {'employe': self.employe.id, 'poste': self.poste.id, 'statut': 'en_attente'}
        response = self.client.post('/api/ressources_humaines/candidature/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['statut'], 'en_attente')

    def test_permission_denied_for_non_admin(self):
        self.client.force_authenticate(user=None)
        response = self.client.post('/api/ressources_humaines/employe/', {'nom': 'X', 'prenom': 'Y', 'email': 'x@y.com', 'poste': 'Test', 'date_embauche': '2025-01-01'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
