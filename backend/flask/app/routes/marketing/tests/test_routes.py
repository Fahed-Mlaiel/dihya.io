"""
Tests avancés pour le module Marketing (REST, GraphQL, sécurité, RGPD, accessibilité, SEO, multitenancy, plugins, audit)
"""
import pytest
from flask import url_for

def test_marketing_rest_crud(client, auth_headers):
    # Création
    resp = client.post(url_for('marketing.create'), json={
        'campagne': 'Promo Été', 'canal': 'Email', 'budget': 5000
    }, headers=auth_headers)
    assert resp.status_code == 201
    data = resp.get_json()
    assert data['campagne'] == 'Promo Été'

    # Lecture
    marketing_id = data['id']
    resp = client.get(url_for('marketing.get', marketing_id=marketing_id), headers=auth_headers)
    assert resp.status_code == 200

    # Mise à jour
    resp = client.put(url_for('marketing.update', marketing_id=marketing_id), json={'budget': 6000}, headers=auth_headers)
    assert resp.status_code == 200
    assert resp.get_json()['budget'] == 6000

    # Suppression
    resp = client.delete(url_for('marketing.delete', marketing_id=marketing_id), headers=auth_headers)
    assert resp.status_code == 204

def test_marketing_graphql(client, auth_headers):
    # Test d'une requête GraphQL (exemple)
    query = '{ marketings { id campagne canal budget } }'
    resp = client.post('/graphql', json={'query': query}, headers=auth_headers)
    assert resp.status_code == 200
    assert 'marketings' in resp.get_json()['data']

# Tests RGPD, accessibilité, SEO, plugins, audit, multitenancy, erreurs, edge cases, etc. à compléter
