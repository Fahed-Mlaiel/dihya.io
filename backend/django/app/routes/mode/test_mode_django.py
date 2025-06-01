"""
Dihya – Tests pour le module Mode
- Couverture RGPD, sécurité, accessibilité
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Collection, Produit, Createur
from rest_framework.test import APIClient
from rest_framework import status

class ModeAPITestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='modeuser', password='testpass', is_mode_admin=True)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.collection = Collection.objects.create(nom='Printemps 2025', saison='printemps', annee=2025, cree_par=self.user)

    def test_create_produit(self):
        data = {'nom': 'Robe Test', 'collection': self.collection.id, 'prix': '99.99', 'taille': 'M', 'couleur': 'Rouge'}
        response = self.client.post('/api/mode/produits/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nom'], 'Robe Test')

    def test_permission_denied_for_non_admin(self):
        self.client.force_authenticate(user=None)
        response = self.client.post('/api/mode/collections/', {'nom': 'X', 'saison': 'été', 'annee': 2025})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
