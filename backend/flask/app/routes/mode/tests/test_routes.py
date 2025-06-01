"""
Tests avancés pour le module Mode (REST, GraphQL, sécurité, RGPD, accessibilité, SEO, multitenancy, plugins, audit)
"""
import pytest
from flask import url_for
def test_mode_rest_crud(client, auth_headers):
    # Création
    resp = client.post(url_for('mode.create'), json={
        'nom': 'Robe', 'style': 'Classique', 'saison': 'Été'
    }, headers=auth_headers)
    assert resp.status_code == 201
    data = resp.get_json()
    assert data['nom'] == 'Robe'
    # Lecture
    mode_id = data['id']
    resp = client.get(url_for('mode.get', mode_id=mode_id), headers=auth_headers)
    assert resp.status_code == 200
    # Mise à jour
    resp = client.put(url_for('mode.update', mode_id=mode_id), json={'style': 'Moderne'}, headers=auth_headers)
    assert resp.status_code == 200
    assert resp.get_json()['style'] == 'Moderne'
    # Suppression
    resp = client.delete(url_for('mode.delete', mode_id=mode_id), headers=auth_headers)
    assert resp.status_code == 204
def test_mode_graphql(client, auth_headers):
    # Test d'une requête GraphQL (exemple)
    query = '{ modes { id nom style saison } }'
    resp = client.post('/graphql', json={'query': query}, headers=auth_headers)
    assert resp.status_code == 200
    assert 'modes' in resp.get_json()['data']
# Tests RGPD, accessibilité, SEO, plugins, audit, multitenancy, erreurs, edge cases, etc. à compléter
