"""
Tests avancés pour le module Services Personne (REST, GraphQL, sécurité, RGPD, accessibilité, SEO, multitenancy, plugins, audit)
"""
import pytest
from flask import url_for
def test_services_personne_rest_crud(client, auth_headers):
    # Création
    resp = client.post(url_for('services_personne.create'), json={
        'nom': 'Aide à domicile', 'type': 'Ménage', 'description': 'Service de ménage.'
    }, headers=auth_headers)
    assert resp.status_code == 201
    data = resp.get_json()
    assert data['nom'] == 'Aide à domicile'
    # Lecture
    sp_id = data['id']
    resp = client.get(url_for('services_personne.get', sp_id=sp_id), headers=auth_headers)
    assert resp.status_code == 200
    # Mise à jour
    resp = client.put(url_for('services_personne.update', sp_id=sp_id), json={'type': 'Garde d\'enfants'}, headers=auth_headers)
    assert resp.status_code == 200
    assert resp.get_json()['type'] == "Garde d'enfants"
    # Suppression
    resp = client.delete(url_for('services_personne.delete', sp_id=sp_id), headers=auth_headers)
    assert resp.status_code == 204
def test_services_personne_graphql(client, auth_headers):
    # Test d'une requête GraphQL (exemple)
    query = '{ servicesPersonne { id nom type description } }'
    resp = client.post('/graphql', json={'query': query}, headers=auth_headers)
    assert resp.status_code == 200
    assert 'servicesPersonne' in resp.get_json()['data']
# Tests RGPD, accessibilité, SEO, plugins, audit, multitenancy, erreurs, edge cases, etc. à compléter
