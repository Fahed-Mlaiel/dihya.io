# validators

# Tests d'intégration Validators

Ce dossier contient les tests d'intégration pour les validateurs (schemas, pydantic, custom, etc.).

## Structure
- **Tests RESTful et GraphQL** pour validateurs.
- **Sécurité** : JWT, CORS, validation, audit, WAF, anti-DDOS.
- **Multilingue** : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.
- **Auditabilité** : logs, anonymisation, export.

## Exécution
```bash
pytest --tb=short --maxfail=1
```

## Exemple de test
```python
"""
Test d'intégration validateur (schéma utilisateur)
"""
import pytest
from backend.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_user_schema():
    response = client.post("/api/validators/user", json={"email": "test@dihya.ai"})
    assert response.status_code == 200
    assert response.json()["valid"] is True
```

## Bonnes pratiques
- Couverture maximale, mocks, fixtures, audit logs.
- Sécurité et conformité RGPD.
- Tests multilingues et multi-rôles.
