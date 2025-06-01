"""
Tests avancés pour le module Medias
"""
from django.test import TestCase
from .models import MediaAsset
from django.contrib.auth import get_user_model

class MediaAssetTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='testuser')
        self.asset = MediaAsset.objects.create(name='Test', type='image', url='http://example.com/img.png', owner=self.user, language='fr')

    def test_create_asset(self):
        self.assertEqual(self.asset.name, 'Test')
        self.assertEqual(self.asset.owner, self.user)

    def test_delete_asset(self):
        aid = self.asset.id
        self.asset.delete()
        self.assertFalse(MediaAsset.objects.filter(id=aid).exists())
