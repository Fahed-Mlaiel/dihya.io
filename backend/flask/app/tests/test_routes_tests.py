"""
Tests d'intégration pour vérifier l'existence et la sécurité des routes principales de l'API Dihya Coding.
Couvre la présence, la méthode autorisée et la sécurité de base (méthodes interdites, 404, etc.).
"""

import pytest

@pytest.mark.parametrize("route,method,expected", [
    ("/", "get", 200),
    ("/api/health", "get", 200),
    ("/api/info", "get", 200),
    ("/api/ping", "get", 200),
    ("/api/echo", "post", 200),
    ("/robots.txt", "get", 200),
    ("/sitemap.xml", "get", 200),
])
def test_route_exists(client, route, method, expected):
    """Vérifie que chaque route principale existe et retourne le bon code HTTP."""
    http_method = getattr(client, method)
    if method == "post":
        response = http_method(route, json={"test": "ok"})
    else:
        response = http_method(route)
    assert response.status_code == expected

@pytest.mark.parametrize("route,method", [
    ("/", "post"),
    ("/api/health", "post"),
    ("/api/info", "post"),
    ("/api/ping", "post"),
    ("/robots.txt", "post"),
    ("/sitemap.xml", "post"),
])
def test_method_not_allowed(client, route, method):
    """Vérifie que les méthodes non autorisées retournent 405."""
    http_method = getattr(client, method)
    response = http_method(route)
    assert response.status_code in (405, 400)

def test_404(client):
    """Vérifie qu'une route inexistante retourne bien 404."""
    response = client.get("/route/inexistante")
    assert response.status_code == 404