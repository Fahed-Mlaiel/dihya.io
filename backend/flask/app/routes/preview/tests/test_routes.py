"""
Tests avancés pour le module Preview (REST, GraphQL, sécurité, RGPD, accessibilité, SEO, multitenancy, plugins, audit)
"""
import pytest
from flask import url_for
def test_preview_rest_crud(client, auth_headers):
    # Création
    resp = client.post(url_for('preview.create'), json={
        'nom': 'PreviewTest', 'url': 'https://test.com/preview', 'type': 'image'
    }, headers=auth_headers)
    assert resp.status_code == 201
    data = resp.get_json()
    assert data['nom'] == 'PreviewTest'
    # Lecture
    preview_id = data['id']
    resp = client.get(url_for('preview.get', preview_id=preview_id), headers=auth_headers)
    assert resp.status_code == 200
    # Mise à jour
    resp = client.put(url_for('preview.update', preview_id=preview_id), json={'type': 'video'}, headers=auth_headers)
    assert resp.status_code == 200
    assert resp.get_json()['type'] == 'video'
    # Suppression
    resp = client.delete(url_for('preview.delete', preview_id=preview_id), headers=auth_headers)
    assert resp.status_code == 204
def test_preview_graphql(client, auth_headers):
    # Test d'une requête GraphQL (exemple)
    query = '{ previews { id nom url type } }'
    resp = client.post('/graphql', json={'query': query}, headers=auth_headers)
    assert resp.status_code == 200
    assert 'previews' in resp.get_json()['data']
# Tests RGPD, accessibilité, SEO, plugins, audit, multitenancy, erreurs, edge cases, etc. à compléter
