"""
Tests avancés pour le module Publicité (REST, GraphQL, sécurité, RGPD, accessibilité, SEO, multitenancy, plugins, audit)
"""
import pytest
from flask import url_for
def test_publicite_rest_crud(client, auth_headers):
    # Création
    resp = client.post(url_for('publicite.create'), json={
        'titre': 'Campagne Test', 'canal': 'TV', 'budget': 10000
    }, headers=auth_headers)
    assert resp.status_code == 201
    data = resp.get_json()
    assert data['titre'] == 'Campagne Test'
    # Lecture
    publicite_id = data['id']
    resp = client.get(url_for('publicite.get', publicite_id=publicite_id), headers=auth_headers)
    assert resp.status_code == 200
    # Mise à jour
    resp = client.put(url_for('publicite.update', publicite_id=publicite_id), json={'budget': 12000}, headers=auth_headers)
    assert resp.status_code == 200
    assert resp.get_json()['budget'] == 12000
    # Suppression
    resp = client.delete(url_for('publicite.delete', publicite_id=publicite_id), headers=auth_headers)
    assert resp.status_code == 204
def test_publicite_graphql(client, auth_headers):
    # Test d'une requête GraphQL (exemple)
    query = '{ publicites { id titre canal budget } }'
    resp = client.post('/graphql', json={'query': query}, headers=auth_headers)
    assert resp.status_code == 200
    assert 'publicites' in resp.get_json()['data']
# Tests RGPD, accessibilité, SEO, plugins, audit, multitenancy, erreurs, edge cases, etc. à compléter
