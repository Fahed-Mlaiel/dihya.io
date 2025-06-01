"""
Tests avancés pour le module Loisirs (REST, GraphQL, sécurité, RGPD, accessibilité, SEO, multitenancy, plugins, audit)
"""
import pytest
from flask import url_for

def test_loisirs_rest_crud(client, auth_headers):
    # Création
    resp = client.post(url_for('loisirs.create'), json={
        'nom': 'Randonnée', 'type': 'Sport', 'description': 'En montagne.'
    }, headers=auth_headers)
    assert resp.status_code == 201
    data = resp.get_json()
    assert data['nom'] == 'Randonnée'

    # Lecture
    loisirs_id = data['id']
    resp = client.get(url_for('loisirs.get', loisirs_id=loisirs_id), headers=auth_headers)
    assert resp.status_code == 200

    # Mise à jour
    resp = client.put(url_for('loisirs.update', loisirs_id=loisirs_id), json={'type': 'Nature'}, headers=auth_headers)
    assert resp.status_code == 200
    assert resp.get_json()['type'] == 'Nature'

    # Suppression
    resp = client.delete(url_for('loisirs.delete', loisirs_id=loisirs_id), headers=auth_headers)
    assert resp.status_code == 204

def test_loisirs_graphql(client, auth_headers):
    # Test d'une requête GraphQL (exemple)
    query = '{ loisirs { id nom type description } }'
    resp = client.post('/graphql', json={'query': query}, headers=auth_headers)
    assert resp.status_code == 200
    assert 'loisirs' in resp.get_json()['data']

# Tests RGPD, accessibilité, SEO, plugins, audit, multitenancy, erreurs, edge cases, etc. à compléter
