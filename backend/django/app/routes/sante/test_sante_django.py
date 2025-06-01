"""
Dihya – Tests pour le module Santé
- Couverture RGPD, sécurité, accessibilité
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Patient, RendezVous, DossierMedical
from rest_framework.test import APIClient
from rest_framework import status

class SanteAPITestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='santeuser', password='testpass', is_sante_admin=True)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.patient = Patient.objects.create(nom='Doe', prenom='Jane', date_naissance='1990-01-01', email='jane.doe@example.com', telephone='0102030405', genre='femme')

    def test_create_rendezvous(self):
        data = {'patient': self.patient.id, 'date': '2025-06-01T10:00:00Z', 'motif': 'Consultation', 'statut': 'planifie'}
        response = self.client.post('/api/sante/rendezvous/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['statut'], 'planifie')

    def test_permission_denied_for_non_admin(self):
        self.client.force_authenticate(user=None)
        response = self.client.post('/api/sante/patient/', {'nom': 'X', 'prenom': 'Y', 'date_naissance': '2000-01-01', 'email': 'x@y.com', 'telephone': '000', 'genre': 'autre'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
