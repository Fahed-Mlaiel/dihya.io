"""
Tests avancés pour le module Science (REST, GraphQL, sécurité, RGPD, accessibilité, SEO, multitenancy, plugins, audit)
"""
import pytest
from flask import url_for
def test_science_rest_crud(client, auth_headers):
    # Création
    resp = client.post(url_for('science.create'), json={
        'domaine': 'Physique', 'sujet': 'Mécanique'
    }, headers=auth_headers)
    assert resp.status_code == 201
    data = resp.get_json()
    assert data['domaine'] == 'Physique'
    # Lecture
    science_id = data['id']
    resp = client.get(url_for('science.get', science_id=science_id), headers=auth_headers)
    assert resp.status_code == 200
    # Mise à jour
    resp = client.put(url_for('science.update', science_id=science_id), json={'sujet': 'Thermodynamique'}, headers=auth_headers)
    assert resp.status_code == 200
    assert resp.get_json()['sujet'] == 'Thermodynamique'
    # Suppression
    resp = client.delete(url_for('science.delete', science_id=science_id), headers=auth_headers)
    assert resp.status_code == 204
def test_science_graphql(client, auth_headers):
    # Test d'une requête GraphQL (exemple)
    query = '{ sciences { id domaine sujet } }'
    resp = client.post('/graphql', json={'query': query}, headers=auth_headers)
    assert resp.status_code == 200
    assert 'sciences' in resp.get_json()['data']
# Tests RGPD, accessibilité, SEO, plugins, audit, multitenancy, erreurs, edge cases, etc. à compléter
