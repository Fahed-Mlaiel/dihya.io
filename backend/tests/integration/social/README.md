# social

# Tests d'intégration Social

Ce dossier contient les tests d'intégration pour les modules social (réseaux, posts, commentaires, modération, etc.).

## Structure
- **Tests RESTful et GraphQL** pour social.
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
Test d'intégration social (création post)
"""
import pytest
from backend.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_post():
    response = client.post("/api/social/posts", json={"content": "Hello Dihya!"}, headers={"Authorization": "Bearer <token>"})
    assert response.status_code == 201
    assert response.json()["content"] == "Hello Dihya!"
```

## Bonnes pratiques
- Couverture maximale, mocks, fixtures, audit logs.
- Sécurité et conformité RGPD.
- Tests multilingues et multi-rôles.
