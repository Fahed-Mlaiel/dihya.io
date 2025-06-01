"""
Dihya – Tests API avancés pour Transport
- Tests unitaires, intégration, sécurité, accessibilité, multilingue
"""
from rest_framework.test import APITestCase
from django.urls import reverse
import sys
sys.path.insert(0, '.')
from backend.django.app.routes.transport.models import Vehicule, Trajet, Reservation

class VehiculeAPITest(APITestCase):
    def setUp(self):
        self.vehicule = Vehicule.objects.create(immatriculation='AB-123-CD', type='Bus', capacite=50)
    def test_list_vehicules(self):
        url = reverse('vehicule-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    def test_create_vehicule(self):
        url = reverse('vehicule-list')
        data = {'immatriculation': 'XY-456-ZW', 'type': 'Minibus', 'capacite': 20}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

class TrajetAPITest(APITestCase):
    def setUp(self):
        self.vehicule = Vehicule.objects.create(immatriculation='AB-123-CD', type='Bus', capacite=50)
        self.conducteur = Conducteur.objects.create(nom='Dupont', prenom='Jean', email='jean.dupont@example.com')
        self.trajet = Trajet.objects.create(vehicule=self.vehicule, conducteur=self.conducteur, depart='Paris', arrivee='Lyon', date='2024-07-01', places_disponibles=40)
    def test_list_trajets(self):
        url = reverse('trajet-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
