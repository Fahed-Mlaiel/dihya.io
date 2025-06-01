"""
Tests avancés pour le module Sport (REST, GraphQL, sécurité, RGPD, accessibilité, SEO, multitenancy, plugins, audit)
"""
import pytest
from flask import url_for
def test_sport_rest_crud(client, auth_headers):
    # Création
    resp = client.post(url_for('sport.create'), json={
        'nom': 'Football', 'type': 'Collectif', 'description': 'Sport d\'équipe.'
    }, headers=auth_headers)
    assert resp.status_code == 201
    data = resp.get_json()
    assert data['nom'] == 'Football'
    # Lecture
    sport_id = data['id']
    resp = client.get(url_for('sport.get', sport_id=sport_id), headers=auth_headers)
    assert resp.status_code == 200
    # Mise à jour
    resp = client.put(url_for('sport.update', sport_id=sport_id), json={'type': 'Individuel'}, headers=auth_headers)
    assert resp.status_code == 200
    assert resp.get_json()['type'] == 'Individuel'
    # Suppression
    resp = client.delete(url_for('sport.delete', sport_id=sport_id), headers=auth_headers)
    assert resp.status_code == 204
def test_sport_graphql(client, auth_headers):
    # Test d'une requête GraphQL (exemple)
    query = '{ sports { id nom type description } }'
    resp = client.post('/graphql', json={'query': query}, headers=auth_headers)
    assert resp.status_code == 200
    assert 'sports' in resp.get_json()['data']
# Tests RGPD, accessibilité, SEO, plugins, audit, multitenancy, erreurs, edge cases, etc. à compléter
