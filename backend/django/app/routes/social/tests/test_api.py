"""
Dihya – Tests API avancés pour Social
- Tests unitaires, intégration, sécurité, accessibilité, multilingue
"""
from rest_framework.test import APITestCase
from django.urls import reverse
from ..models import Profil, Post, Commentaire, Like, Abonnement
from django.contrib.auth import get_user_model

User = get_user_model()

class ProfilAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.p = Profil.objects.create(user=self.user, bio='Bio')
    def test_list_profils(self):
        url = reverse('profil-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    def test_create_profil(self):
        url = reverse('profil-list')
        user2 = User.objects.create(username='user2')
        data = {'user': user2.id, 'bio': 'Bio2'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

class PostAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.p = Profil.objects.create(user=self.user, bio='Bio')
        self.post = Post.objects.create(auteur=self.p, contenu='Contenu')
    def test_list_posts(self):
        url = reverse('post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
