"""
Tests avancés pour le module Hotellerie (REST, GraphQL, sécurité, RGPD, accessibilité, SEO, multitenancy, plugins, audit)
"""
import pytest
from flask import url_for

def test_hotellerie_rest_crud(client, auth_headers):
    # Création
    resp = client.post(url_for('hotellerie.create'), json={
        'nom': 'HotelTest', 'adresse': '1 rue test', 'etoiles': 4
    }, headers=auth_headers)
    assert resp.status_code == 201
    data = resp.get_json()
    assert data['nom'] == 'HotelTest'

    # Lecture
    hotel_id = data['id']
    resp = client.get(url_for('hotellerie.get', hotel_id=hotel_id), headers=auth_headers)
    assert resp.status_code == 200

    # Mise à jour
    resp = client.put(url_for('hotellerie.update', hotel_id=hotel_id), json={'etoiles': 5}, headers=auth_headers)
    assert resp.status_code == 200
    assert resp.get_json()['etoiles'] == 5

    # Suppression
    resp = client.delete(url_for('hotellerie.delete', hotel_id=hotel_id), headers=auth_headers)
    assert resp.status_code == 204

def test_hotellerie_graphql(client, auth_headers):
    # Test d'une requête GraphQL (exemple)
    query = '{ hotelleries { id nom adresse etoiles } }'
    resp = client.post('/graphql', json={'query': query}, headers=auth_headers)
    assert resp.status_code == 200
    assert 'hotelleries' in resp.get_json()['data']

# Tests RGPD, accessibilité, SEO, plugins, audit, multitenancy, erreurs, edge cases, etc. à compléter
