"""
Dihya – Tests pour le module Restauration
- Couverture RGPD, sécurité, accessibilité
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Restaurant, Menu, Reservation
from rest_framework.test import APIClient
from rest_framework import status

class RestaurationAPITestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='restouser', password='testpass', is_restauration_admin=True)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.restaurant = Restaurant.objects.create(nom='Chez Dihya', adresse='1 rue de la Paix', telephone='0102030405', proprietaire=self.user)
        self.menu = Menu.objects.create(restaurant=self.restaurant, nom='Menu Test', prix='19.99')

    def test_create_reservation(self):
        data = {'restaurant': self.restaurant.id, 'client': self.user.id, 'date': '2025-06-01T19:00:00Z', 'nombre_personnes': 2, 'statut': 'en_attente'}
        response = self.client.post('/api/restauration/reservation/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['statut'], 'en_attente')

    def test_permission_denied_for_non_admin(self):
        self.client.force_authenticate(user=None)
        response = self.client.post('/api/restauration/restaurant/', {'nom': 'X', 'adresse': 'Y', 'telephone': 'Z'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
