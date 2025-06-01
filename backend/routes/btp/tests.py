from django.test import TestCase
from .models import BtpProject, BtpAsset
from django.contrib.auth import get_user_model
class BtpProjectTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='testuser')
        self.project = BtpProject.objects.create(name='Test', owner=self.user, status='active', language='fr')
    def test_create_project(self):
        self.assertEqual(self.project.name, 'Test')
        self.assertEqual(self.project.owner, self.user)
    def test_delete_project(self):
        pid = self.project.id
        self.project.delete()
        self.assertFalse(BtpProject.objects.filter(id=pid).exists())
class BtpAssetTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='testuser')
        self.asset = BtpAsset.objects.create(name='Asset', type='machine', url='http://example.com/asset', owner=self.user, language='fr')
    def test_create_asset(self):
        self.assertEqual(self.asset.name, 'Asset')
        self.assertEqual(self.asset.owner, self.user)
    def test_delete_asset(self):
        aid = self.asset.id
        self.asset.delete()
        self.assertFalse(BtpAsset.objects.filter(id=aid).exists())
