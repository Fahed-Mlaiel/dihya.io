"""
Tests avancés pour le module Tourisme (REST, GraphQL, sécurité, RGPD, accessibilité, SEO, multitenancy, plugins, audit)
"""
import pytest
from flask import url_for
def test_tourisme_rest_crud(client, auth_headers):
    # Création
    resp = client.post(url_for('tourisme.create'), json={
        'nom': 'Visite guidée', 'type': 'Culturel', 'description': 'Tour de ville.'
    }, headers=auth_headers)
    assert resp.status_code == 201
    data = resp.get_json()
    assert data['nom'] == 'Visite guidée'
    # Lecture
    tourisme_id = data['id']
    resp = client.get(url_for('tourisme.get', tourisme_id=tourisme_id), headers=auth_headers)
    assert resp.status_code == 200
    # Mise à jour
    resp = client.put(url_for('tourisme.update', tourisme_id=tourisme_id), json={'type': 'Nature'}, headers=auth_headers)
    assert resp.status_code == 200
    assert resp.get_json()['type'] == 'Nature'
    # Suppression
    resp = client.delete(url_for('tourisme.delete', tourisme_id=tourisme_id), headers=auth_headers)
    assert resp.status_code == 204
def test_tourisme_graphql(client, auth_headers):
    # Test d'une requête GraphQL (exemple)
    query = '{ tourismes { id nom type description } }'
    resp = client.post('/graphql', json={'query': query}, headers=auth_headers)
    assert resp.status_code == 200
    assert 'tourismes' in resp.get_json()['data']
# Tests RGPD, accessibilité, SEO, plugins, audit, multitenancy, erreurs, edge cases, etc. à compléter
