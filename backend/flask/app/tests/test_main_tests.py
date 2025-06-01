"""
Tests unitaires pour les routes publiques principales de l'API Dihya Coding.
Couvre : accueil, healthcheck, info, ping, echo, robots.txt, sitemap.xml.
"""

import pytest

def test_home(client):
    """Test de la route d'accueil '/'."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert "message" in data
    assert data["message"].startswith("Bienvenue")

def test_health(client):
    """Test du healthcheck '/api/health'."""
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "ok"

def test_info(client):
    """Test de la route info '/api/info'."""
    response = client.get("/api/info")
    assert response.status_code == 200
    data = response.get_json()
    assert data["project"] == "Dihya Coding"

def test_ping(client):
    """Test de la route ping '/api/ping'."""
    response = client.get("/api/ping")
    assert response.status_code == 200
    data = response.get_json()
    assert data["pong"] is True

def test_echo(client):
    """Test de la route echo '/api/echo'."""
    payload = {"test": "valeur"}
    response = client.post("/api/echo", json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert data["received"] == payload

def test_echo_no_data(client):
    """Test de la route echo '/api/echo' sans données."""
    response = client.post("/api/echo", json=None)
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data

def test_robots_txt(client):
    """Test de la route robots.txt pour le SEO."""
    response = client.get("/robots.txt")
    assert response.status_code == 200
    assert b"User-agent" in response.data

def test_sitemap_xml(client):
    """Test de la route sitemap.xml pour le SEO."""
    response = client.get("/sitemap.xml")
    assert response.status_code == 200
    assert b"<urlset" in response.data