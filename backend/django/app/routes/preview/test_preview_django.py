"""
Dihya – Tests pour le module Preview
- Couverture RGPD, sécurité, accessibilité
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Preview
from rest_framework.test import APIClient
from rest_framework import status

class PreviewAPITestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='previewuser', password='testpass', is_preview_admin=True)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_preview(self):
        data = {'titre': 'Aperçu Test', 'contenu': 'Contenu test', 'type': 'texte'}
        response = self.client.post('/api/preview/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['titre'], 'Aperçu Test')

    def test_permission_denied_for_non_admin(self):
        self.client.force_authenticate(user=None)
        response = self.client.post('/api/preview/', {'titre': 'X', 'contenu': 'X', 'type': 'texte'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
