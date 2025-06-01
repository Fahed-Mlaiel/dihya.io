"""
Tests avancés pour le module Mode (Fashion)
"""
from django.test import TestCase
from .models import ModeProject
from django.contrib.auth import get_user_model

class ModeProjectTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='testuser')
        self.project = ModeProject.objects.create(name='Test', owner=self.user, status='active', language='fr')

    def test_create_project(self):
        self.assertEqual(self.project.name, 'Test')
        self.assertEqual(self.project.owner, self.user)

    def test_delete_project(self):
        pid = self.project.id
        self.project.delete()
        self.assertFalse(ModeProject.objects.filter(id=pid).exists())
