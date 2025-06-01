"""
Tests avancés pour le module Mobile
"""
from django.test import TestCase
from .models import MobileProject
from django.contrib.auth import get_user_model

class MobileProjectTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='testuser')
        self.project = MobileProject.objects.create(name='Test', owner=self.user, status='active', language='fr')

    def test_create_project(self):
        self.assertEqual(self.project.name, 'Test')
        self.assertEqual(self.project.owner, self.user)

    def test_delete_project(self):
        pid = self.project.id
        self.project.delete()
        self.assertFalse(MobileProject.objects.filter(id=pid).exists())
