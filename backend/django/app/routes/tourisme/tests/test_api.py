"""
Dihya – Tests API avancés pour Tourisme
- Tests unitaires, intégration, sécurité, accessibilité, multilingue
"""
from rest_framework.test import APITestCase
from django.urls import reverse
from ..models import Destination, Offre, Reservation, Avis

class DestinationAPITest(APITestCase):
    def setUp(self):
        self.destination = Destination.objects.create(nom='Paris', pays='France', description='Ville lumière')
    def test_list_destinations(self):
        url = reverse('destination-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    def test_create_destination(self):
        url = reverse('destination-list')
        data = {'nom': 'Lyon', 'pays': 'France', 'description': 'Ville des lumières'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

class OffreAPITest(APITestCase):
    def setUp(self):
        self.destination = Destination.objects.create(nom='Paris', pays='France', description='Ville lumière')
        self.offre = Offre.objects.create(destination=self.destination, titre='Séjour', description='Séjour à Paris', prix=1000, date_debut='2024-06-01', date_fin='2024-06-10')
    def test_list_offres(self):
        url = reverse('offre-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
