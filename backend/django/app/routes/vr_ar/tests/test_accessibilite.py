# Test d’accessibilité avancé pour le module vr_ar
# Vérifie la conformité des endpoints pour les utilisateurs en situation de handicap.

import pytest
from rest_framework.test import APIClient
from django.urls import reverse

def test_scene_accessibility_labels():
    client = APIClient()
    response = client.get(reverse('vr_ar-scene-list'))
    assert 'Content-Language' in response
    assert response['Content-Language'] in ['fr', 'en', 'ar', 'amazigh']
    # Vérifie la présence de métadonnées d’accessibilité
    assert 'results' in response.data
    for scene in response.data['results']:
        assert 'lang' in scene
        assert 'title' in scene
        assert 'id' in scene
