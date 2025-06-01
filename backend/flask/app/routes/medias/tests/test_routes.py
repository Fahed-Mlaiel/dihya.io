"""
Tests avancés pour le module Medias (REST, GraphQL, sécurité, RGPD, accessibilité, SEO, multitenancy, plugins, audit)
"""
import pytest
from flask import url_for
def test_medias_rest_crud(client, auth_headers):
    # Création
    resp = client.post(url_for('medias.create'), json={
        'titre': 'Vidéo Test', 'url': 'https://test.com/video', 'type': 'video'
    }, headers=auth_headers)
    assert resp.status_code == 201
    data = resp.get_json()
    assert data['titre'] == 'Vidéo Test'
    # Lecture
    medias_id = data['id']
    resp = client.get(url_for('medias.get', medias_id=medias_id), headers=auth_headers)
    assert resp.status_code == 200
    # Mise à jour
    resp = client.put(url_for('medias.update', medias_id=medias_id), json={'type': 'audio'}, headers=auth_headers)
    assert resp.status_code == 200
    assert resp.get_json()['type'] == 'audio'
    # Suppression
    resp = client.delete(url_for('medias.delete', medias_id=medias_id), headers=auth_headers)
    assert resp.status_code == 204
def test_medias_graphql(client, auth_headers):
    # Test d'une requête GraphQL (exemple)
    query = '{ medias { id titre url type } }'
    resp = client.post('/graphql', json={'query': query}, headers=auth_headers)
    assert resp.status_code == 200
    assert 'medias' in resp.get_json()['data']
# Tests RGPD, accessibilité, SEO, plugins, audit, multitenancy, erreurs, edge cases, etc. à compléter
