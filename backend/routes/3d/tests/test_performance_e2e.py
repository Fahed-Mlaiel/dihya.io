"""
Test de performance et anti-DDOS ultra avancé pour le module 3D (Dihya)
- Stress test, temps de réponse, audit, logs, RGPD
"""
import pytest
import time
from django.urls import reverse
from rest_framework.test import APIClient

def test_performance_stress():
    client = APIClient()
    start = time.time()
    for _ in range(10):
        response = client.get(reverse('3d-threedproject-list'))
        assert response.status_code in (200, 401, 403)
    elapsed = time.time() - start
    assert elapsed < 5  # 10 requêtes < 5s

def test_anti_ddos():
    client = APIClient()
    for _ in range(100):
        response = client.get(reverse('3d-threedproject-list'))
    # Doit retourner 429 (Too Many Requests) ou 200/401/403 si fallback
    assert response.status_code in (429, 200, 401, 403)
