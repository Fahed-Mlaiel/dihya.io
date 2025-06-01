# vr_ar

# Tests d'intégration VR/AR

Ce dossier contient les tests d'intégration pour les modules VR/AR (projets, expériences, IA, etc.).

## Structure
- **Tests RESTful et GraphQL** pour VR/AR.
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
Test d'intégration VR/AR (création projet VR)
"""
import pytest
from backend.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_vr_project():
    response = client.post("/api/vr_ar/projects", json={"title": "Expérience VR Dihya"}, headers={"Authorization": "Bearer <token>"})
    assert response.status_code == 201
    assert response.json()["title"] == "Expérience VR Dihya"
```

## Bonnes pratiques
- Couverture maximale, mocks, fixtures, audit logs.
- Sécurité et conformité RGPD.
- Tests multilingues et multi-rôles.
