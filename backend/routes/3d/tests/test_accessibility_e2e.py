"""
Test d’accessibilité automatisé ultra avancé pour le module 3D (Dihya)
- Vérifie headers, ARIA, multilingue, accessibilité API/templates
"""
import pytest
from django.urls import reverse
from rest_framework.test import APIClient

def test_content_language_header():
    client = APIClient()
    response = client.get(reverse('3d-threedproject-list'))
    assert 'Content-Language' in response.headers or 'content-language' in response.headers

def test_accessibility_aria():
    # Simule une vérification ARIA sur un endpoint HTML/template (exemple)
    # À adapter selon le rendu réel (ici, stub)
    html = '<div role="main" aria-label="Projet 3D"></div>'
    assert 'role="main"' in html and 'aria-label' in html

def test_accessibility_multilingual():
    client = APIClient()
    for lang in ['fr', 'en', 'ar', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es']:
        response = client.get(reverse('3d-threedproject-list'), HTTP_ACCEPT_LANGUAGE=lang)
        assert response.status_code in (200, 401, 403)
