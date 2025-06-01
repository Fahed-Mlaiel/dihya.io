# ressources_humaines

# Tests d'intégration Ressources Humaines

Ce dossier contient les tests d'intégration pour les modules RH (gestion des utilisateurs, rôles, permissions, anonymisation, export RGPD, etc.).

## Structure
- **Tests RESTful et GraphQL** pour RH.
- **Sécurité** : JWT, RBAC, CORS, audit, WAF, anti-DDOS.
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
Test d'intégration RH (création utilisateur, export RGPD)
"""
import pytest
from backend.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_user_admin():
    response = client.post("/api/rh/users", json={"email": "test@dihya.ai", "role": "user"}, headers={"Authorization": "Bearer <admin_token>"})
    assert response.status_code == 201
    assert response.json()["email"] == "test@dihya.ai"
```

## Bonnes pratiques
- Couverture maximale, mocks, fixtures, audit logs.
- Sécurité et conformité RGPD.
- Tests multilingues et multi-rôles.
