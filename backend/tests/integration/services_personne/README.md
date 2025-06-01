# services_personne

# Tests d'intégration Services à la personne

Ce dossier contient les tests d'intégration pour les modules services à la personne (aide, assistance, réservation, etc.).

## Structure
- **Tests RESTful et GraphQL** pour services à la personne.
- **Sécurité** : JWT, CORS, validation, audit, WAF, anti-DDOS.
- **Multilingue** : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.
- **Multitenancy** : admin, user, invité.
- **Auditabilité** : logs, anonymisation, export.

## Exécution
```bash
pytest --tb=short --maxfail=1
```

## Exemple de test
```python
"""
Test d'intégration service à la personne (création demande)
"""
import pytest
from backend.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_service_request():
    response = client.post("/api/services_personne/demandes", json={"type": "aide"}, headers={"Authorization": "Bearer <token>"})
    assert response.status_code == 201
    assert response.json()["type"] == "aide"
```

## Bonnes pratiques
- Couverture maximale, mocks, fixtures, audit logs.
- Sécurité et conformité RGPD.
- Tests multilingues et multi-rôles.
