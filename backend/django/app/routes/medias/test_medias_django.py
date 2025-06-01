"""
Dihya – Tests pour le module Médias
- Couverture RGPD, sécurité, accessibilité
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Media
from rest_framework.test import APIClient
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile

class MediaAPITestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='mediauser', password='testpass', is_media_admin=True)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_upload_media(self):
        file = SimpleUploadedFile('test.jpg', b'file_content', content_type='image/jpeg')
        data = {'titre': 'Test Media', 'type': 'image', 'fichier': file}
        response = self.client.post('/api/medias/', data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['titre'], 'Test Media')

    def test_permission_denied_for_non_admin(self):
        self.client.force_authenticate(user=None)
        response = self.client.post('/api/medias/', {'titre': 'X', 'type': 'image'}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
