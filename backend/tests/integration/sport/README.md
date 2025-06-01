# sport

# Tests d'intégration Sport

Ce dossier contient les tests d'intégration pour les modules sport (clubs, événements, réservations, etc.).

## Structure
- **Tests RESTful et GraphQL** pour sport.
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
Test d'intégration sport (création club)
"""
import pytest
from backend.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_club():
    response = client.post("/api/sport/clubs", json={"name": "Dihya FC"}, headers={"Authorization": "Bearer <token>"})
    assert response.status_code == 201
    assert response.json()["name"] == "Dihya FC"
```

## Bonnes pratiques
- Couverture maximale, mocks, fixtures, audit logs.
- Sécurité et conformité RGPD.
- Tests multilingues et multi-rôles.
