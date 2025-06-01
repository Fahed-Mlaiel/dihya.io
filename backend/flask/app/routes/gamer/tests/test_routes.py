"""
Tests avancés pour le module Gamer (REST, GraphQL, sécurité, RGPD, accessibilité, SEO, multitenancy, plugins, audit)
"""
import pytest
from flask import url_for

def test_gamer_rest_crud(client, auth_headers):
    # Création
    resp = client.post(url_for('gamer.create'), json={
        'pseudo': 'TestUser', 'email': 'test@example.com', 'score': 100
    }, headers=auth_headers)
    assert resp.status_code == 201
    data = resp.get_json()
    assert data['pseudo'] == 'TestUser'

    # Lecture
    gamer_id = data['id']
    resp = client.get(url_for('gamer.get', gamer_id=gamer_id), headers=auth_headers)
    assert resp.status_code == 200

    # Mise à jour
    resp = client.put(url_for('gamer.update', gamer_id=gamer_id), json={'score': 200}, headers=auth_headers)
    assert resp.status_code == 200
    assert resp.get_json()['score'] == 200

    # Suppression
    resp = client.delete(url_for('gamer.delete', gamer_id=gamer_id), headers=auth_headers)
    assert resp.status_code == 204

def test_gamer_graphql(client, auth_headers):
    # Test d'une requête GraphQL (exemple)
    query = '{ gamers { id pseudo email score } }'
    resp = client.post('/graphql', json={'query': query}, headers=auth_headers)
    assert resp.status_code == 200
    assert 'gamers' in resp.get_json()['data']

# Tests RGPD, accessibilité, SEO, plugins, audit, multitenancy, erreurs, edge cases, etc. à compléter
