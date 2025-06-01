# restauration

# Tests d'intégration Restauration

Ce dossier contient les tests d'intégration pour les modules de restauration (gestion restaurants, menus, commandes, allergies, etc.).

## Structure
- **Tests RESTful et GraphQL** pour restauration.
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
Test d'intégration restauration (création menu)
"""
import pytest
from backend.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_menu():
    response = client.post("/api/restauration/menus", json={"name": "Menu Vegan"}, headers={"Authorization": "Bearer <token>"})
    assert response.status_code == 201
    assert response.json()["name"] == "Menu Vegan"
```

## Bonnes pratiques
- Couverture maximale, mocks, fixtures, audit logs.
- Sécurité et conformité RGPD.
- Tests multilingues et multi-rôles.
