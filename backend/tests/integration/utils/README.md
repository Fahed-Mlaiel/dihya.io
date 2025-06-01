# utils

# Tests d'intégration Utils

Ce dossier contient les tests d'intégration pour les utilitaires backend (helpers, middlewares, outils de sécurité, etc.).

## Structure
- **Tests RESTful et GraphQL** pour utilitaires.
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
Test d'intégration utilitaire (middleware CORS)
"""
import pytest
from backend.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_cors_middleware():
    response = client.options("/api/utils/ping", headers={"Origin": "https://dihya.ai"})
    assert response.status_code == 200
    assert response.headers["access-control-allow-origin"] == "https://dihya.ai"
```

## Bonnes pratiques
- Couverture maximale, mocks, fixtures, audit logs.
- Sécurité et conformité RGPD.
- Tests multilingues et multi-rôles.
