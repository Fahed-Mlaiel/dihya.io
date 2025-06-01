# transport

# Tests d'intégration Transport

Ce dossier contient les tests d'intégration pour les modules transport (trajets, réservations, véhicules, etc.).

## Structure
- **Tests RESTful et GraphQL** pour transport.
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
Test d'intégration transport (création trajet)
"""
import pytest
from backend.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_trip():
    response = client.post("/api/transport/trajets", json={"from": "A", "to": "B"}, headers={"Authorization": "Bearer <token>"})
    assert response.status_code == 201
    assert response.json()["from"] == "A"
```

## Bonnes pratiques
- Couverture maximale, mocks, fixtures, audit logs.
- Sécurité et conformité RGPD.
- Tests multilingues et multi-rôles.
