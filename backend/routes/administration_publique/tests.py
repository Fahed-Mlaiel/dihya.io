"""
Tests avancés pour le module Administration Publique
"""
from django.test import TestCase
from .models import AdministrationPubliqueProject
from django.contrib.auth import get_user_model

class AdministrationPubliqueProjectTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='testuser')
        self.project = AdministrationPubliqueProject.objects.create(name='Test', owner=self.user, status='active', language='fr')

    def test_create_project(self):
        self.assertEqual(self.project.name, 'Test')
        self.assertEqual(self.project.owner, self.user)

    def test_delete_project(self):
        pid = self.project.id
        self.project.delete()
        self.assertFalse(AdministrationPubliqueProject.objects.filter(id=pid).exists())
