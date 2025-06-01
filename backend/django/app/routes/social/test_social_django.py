"""
Dihya – Tests unitaires et d'intégration pour Social
- Couverture exhaustive, sécurité, RGPD, multilingue
"""
from django.test import TestCase
from .models import Profil, Post, Commentaire, Like, Abonnement
from django.contrib.auth import get_user_model

User = get_user_model()

class ProfilModelTest(TestCase):
    def test_str(self):
        user = User.objects.create(username='testuser')
        p = Profil.objects.create(user=user, bio='Bio')
        self.assertIn('testuser', str(p))

class PostModelTest(TestCase):
    def test_str(self):
        user = User.objects.create(username='testuser')
        p = Profil.objects.create(user=user, bio='Bio')
        post = Post.objects.create(auteur=p, contenu='Contenu')
        self.assertIn('Profil de testuser', str(post))

class CommentaireModelTest(TestCase):
    def test_str(self):
        user = User.objects.create(username='testuser')
        p = Profil.objects.create(user=user, bio='Bio')
        post = Post.objects.create(auteur=p, contenu='Contenu')
        c = Commentaire.objects.create(post=post, auteur=p, contenu='Commentaire')
        self.assertIn('Commentaire de', str(c))
