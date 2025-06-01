# Test d’accessibilité avancé pour le module voice
# Vérifie la conformité des endpoints et assets pour les utilisateurs en situation de handicap.

import pytest
from rest_framework.test import APIClient
from django.urls import reverse

def test_audiofile_accessibility_labels():
    client = APIClient()
    response = client.get(reverse('voice-audiofile-list'))
    assert 'Content-Language' in response
    assert response['Content-Language'] in ['fr', 'en', 'ar', 'amazigh']
    # Vérifie la présence de métadonnées d’accessibilité
    assert 'results' in response.data
    for audio in response.data['results']:
        assert 'language' in audio
        assert 'file' in audio
        assert 'id' in audio
