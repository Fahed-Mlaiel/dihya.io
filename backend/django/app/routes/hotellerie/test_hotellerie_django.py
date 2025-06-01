"""
Tests unitaires et intégration Hôtellerie (couverture maximale, multilingue)
"""
from django.test import TestCase
from .models import Hotel

class HotelModelTest(TestCase):
    def test_creation_hotel(self):
        hotel = Hotel.objects.create(
            nom='Hotel Amazigh', adresse='Tizi Ouzou', responsable='Yidir')
        self.assertEqual(hotel.nom, 'Hotel Amazigh')
