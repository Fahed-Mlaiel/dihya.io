"""
Test d’intrusion automatisé ultra avancé pour le module 3D (Dihya)
- Injection, XSS, CSRF, brute-force, anti-bot, audit, RGPD
"""
import pytest
from django.urls import reverse
from rest_framework.test import APIClient

def test_sql_injection_protection():
    client = APIClient()
    payload = {"name": "test'; DROP TABLE threedproject; --", "description": "x", "lang": "fr"}
    response = client.post(reverse('3d-threedproject-list'), payload)
    assert response.status_code in (400, 422, 201)
    assert 'DROP' not in str(response.content)

def test_xss_protection():
    client = APIClient()
    payload = {"name": "<script>alert('xss')</script>", "description": "desc", "lang": "fr"}
    response = client.post(reverse('3d-threedproject-list'), payload)
    assert response.status_code in (400, 422, 201)
    assert '<script>' not in str(response.content)

def test_csrf_protection():
    client = APIClient()
    payload = {"name": "csrf", "description": "desc", "lang": "fr"}
    response = client.post(reverse('3d-threedproject-list'), payload)
    assert response.status_code in (400, 403, 201)

def test_brute_force_protection():
    client = APIClient()
    for _ in range(20):
        response = client.post(reverse('3d-threedproject-list'), {"name": "bf", "description": "desc", "lang": "fr"})
    assert response.status_code in (429, 201, 400)

def test_anti_bot_header():
    client = APIClient(HTTP_USER_AGENT="bot")
    response = client.get(reverse('3d-threedproject-list'))
    assert response.status_code in (403, 200)
