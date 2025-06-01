"""
Tests avancés pour le module Social (REST, GraphQL, sécurité, RGPD, accessibilité, SEO, multitenancy, plugins, audit)
"""
import pytest
from flask import url_for
def test_social_rest_crud(client, auth_headers):
    # Création
    resp = client.post(url_for('social.create'), json={
        'nom': 'Association', 'type': 'Caritatif', 'description': 'Aide sociale.'
    }, headers=auth_headers)
    assert resp.status_code == 201
    data = resp.get_json()
    assert data['nom'] == 'Association'
    # Lecture
    social_id = data['id']
    resp = client.get(url_for('social.get', social_id=social_id), headers=auth_headers)
    assert resp.status_code == 200
    # Mise à jour
    resp = client.put(url_for('social.update', social_id=social_id), json={'type': 'Soutien'}, headers=auth_headers)
    assert resp.status_code == 200
    assert resp.get_json()['type'] == 'Soutien'
    # Suppression
    resp = client.delete(url_for('social.delete', social_id=social_id), headers=auth_headers)
    assert resp.status_code == 204
def test_social_graphql(client, auth_headers):
    # Test d'une requête GraphQL (exemple)
    query = '{ socials { id nom type description } }'
    resp = client.post('/graphql', json={'query': query}, headers=auth_headers)
    assert resp.status_code == 200
    assert 'socials' in resp.get_json()['data']
# Tests RGPD, accessibilité, SEO, plugins, audit, multitenancy, erreurs, edge cases, etc. à compléter
