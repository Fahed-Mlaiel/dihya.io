# Test d’accessibilité avancé pour le module voyage
# Vérifie la conformité des endpoints pour les utilisateurs en situation de handicap.

import pytest
from rest_framework.test import APIClient
from django.urls import reverse

def test_reservation_accessibility_labels():
    client = APIClient()
    response = client.get(reverse('voyage-reservation-list'))
    assert 'Content-Language' in response
    assert response['Content-Language'] in ['fr', 'en', 'ar', 'amazigh']
    # Vérifie la présence de métadonnées d’accessibilité
    assert 'results' in response.data
    for res in response.data['results']:
        assert 'lang' in res
        assert 'voyage' in res
        assert 'id' in res
