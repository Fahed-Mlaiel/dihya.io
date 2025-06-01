# recherche

# Tests d'intégration pour la recherche

Ce dossier contient les tests d'intégration pour les routes et services de recherche du backend Dihya.

## Structure
- **Tests RESTful et GraphQL** pour la recherche IA, VR, AR, etc.
- **Sécurité** : JWT, CORS, validation, audit, WAF, anti-DDOS.
- **Multilingue** : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.
- **Mock IA** : fallback LLaMA, Mixtral, Mistral.
- **Multitenancy** : admin, user, invité.
- **Auditabilité** : logs, anonymisation, export.

## Exécution
```bash
pytest --tb=short --maxfail=1
```

## Exemple de test (Python, pytest)
```python
"""
Test d'intégration pour la recherche IA (REST & GraphQL)
"""
import pytest
from backend.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_search_ia_jwt():
    response = client.post("/api/search/ia", json={"query": "test"}, headers={"Authorization": "Bearer <token>"})
    assert response.status_code == 200
    assert "results" in response.json()
```

## Bonnes pratiques
- Couverture maximale, mocks, fixtures, audit logs.
- Sécurité et conformité RGPD.
- Tests multilingues et multi-rôles.
