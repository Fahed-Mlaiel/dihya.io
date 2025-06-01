# voyage

# Tests d'intégration Voyage

Ce dossier contient les tests d'intégration pour les modules voyage (réservations, itinéraires, guides, etc.).

## Structure
- **Tests RESTful et GraphQL** pour voyage.
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
Test d'intégration voyage (création réservation)
"""
import pytest
from backend.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_reservation():
    response = client.post("/api/voyage/reservations", json={"destination": "Tizi Ouzou"}, headers={"Authorization": "Bearer <token>"})
    assert response.status_code == 201
    assert response.json()["destination"] == "Tizi Ouzou"
```

## Bonnes pratiques
- Couverture maximale, mocks, fixtures, audit logs.
- Sécurité et conformité RGPD.
- Tests multilingues et multi-rôles.
