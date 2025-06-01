"""
Tests avancés pour le module Recherche (REST, GraphQL, sécurité, RGPD, accessibilité, SEO, multitenancy, plugins, audit)
"""
import pytest
from flask import url_for
def test_recherche_rest_crud(client, auth_headers):
    # Création
    resp = client.post(url_for('recherche.create'), json={
        'sujet': 'IA', 'description': 'Recherche IA'
    }, headers=auth_headers)
    assert resp.status_code == 201
    data = resp.get_json()
    assert data['sujet'] == 'IA'
    # Lecture
    recherche_id = data['id']
    resp = client.get(url_for('recherche.get', recherche_id=recherche_id), headers=auth_headers)
    assert resp.status_code == 200
    # Mise à jour
    resp = client.put(url_for('recherche.update', recherche_id=recherche_id), json={'description': 'Recherche avancée'}, headers=auth_headers)
    assert resp.status_code == 200
    assert resp.get_json()['description'] == 'Recherche avancée'
    # Suppression
    resp = client.delete(url_for('recherche.delete', recherche_id=recherche_id), headers=auth_headers)
    assert resp.status_code == 204
def test_recherche_graphql(client, auth_headers):
    # Test d'une requête GraphQL (exemple)
    query = '{ recherches { id sujet description } }'
    resp = client.post('/graphql', json={'query': query}, headers=auth_headers)
    assert resp.status_code == 200
    assert 'recherches' in resp.get_json()['data']
# Tests RGPD, accessibilité, SEO, plugins, audit, multitenancy, erreurs, edge cases, etc. à compléter
