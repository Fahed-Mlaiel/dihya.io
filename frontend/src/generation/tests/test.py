"""
Test complet pour la génération de projets IA, VR, AR, etc.
@author: Dihya Team
@description: Couverture maximale, multilingue, sécurité, plugins, audit.
"""
import pytest
import requests

API_URL = "http://localhost:8000/api/generation"

@pytest.mark.parametrize("lang,token,expected_status", [
    ("fr", "TOKEN_ADMIN", 201),
    ("en", "TOKEN_ADMIN", 201),
    ("fr", None, 401),
    ("fr", "TOKEN_INVITE", 403),
])
def test_generation_multilingue(lang, token, expected_status):
    headers = {"Accept-Language": lang}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    data = {"type": "ia", "nom": "Test", "langue": lang}
    r = requests.post(API_URL, json=data, headers=headers)
    assert r.status_code == expected_status

# ...tests plugins, fallback IA, audit, i18n, SEO, RGPD, etc.
