# science

# Tests d'intégration Science

Ce dossier contient les tests d'intégration pour les modules science (projets, publications, IA, VR, AR, etc.).

## Structure
- **Tests RESTful et GraphQL** pour science.
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
Test d'intégration science (création projet)
"""
import pytest
from backend.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_science_project():
    response = client.post("/api/science/projects", json={"title": "Projet IA"}, headers={"Authorization": "Bearer <token>"})
    assert response.status_code == 201
    assert response.json()["title"] == "Projet IA"
```

## Bonnes pratiques
- Couverture maximale, mocks, fixtures, audit logs.
- Sécurité et conformité RGPD.
- Tests multilingues et multi-rôles.
