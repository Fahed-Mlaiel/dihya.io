from django.test import TestCase
from .models import ConstructionProject, ConstructionAsset
from django.contrib.auth import get_user_model
class ConstructionProjectTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='testuser')
        self.project = ConstructionProject.objects.create(name='Test', owner=self.user, status='active', language='fr')
    def test_create_project(self):
        self.assertEqual(self.project.name, 'Test')
        self.assertEqual(self.project.owner, self.user)
    def test_delete_project(self):
        pid = self.project.id
        self.project.delete()
        self.assertFalse(ConstructionProject.objects.filter(id=pid).exists())
class ConstructionAssetTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='testuser')
        self.asset = ConstructionAsset.objects.create(name='Asset', type='machine', url='http://example.com/asset', owner=self.user, language='fr')
    def test_create_asset(self):
        self.assertEqual(self.asset.name, 'Asset')
        self.assertEqual(self.asset.owner, self.user)
    def test_delete_asset(self):
        aid = self.asset.id
        self.asset.delete()
        self.assertFalse(ConstructionAsset.objects.filter(id=aid).exists())
