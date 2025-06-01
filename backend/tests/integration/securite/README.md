# securite

# Tests d'intégration Sécurité

Ce dossier contient les tests d'intégration pour les modules sécurité (audit, WAF, anti-DDOS, gestion des accès, etc.).

## Structure
- **Tests RESTful et GraphQL** pour sécurité.
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
Test d'intégration sécurité (audit log)
"""
import pytest
from backend.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_audit_log():
    response = client.get("/api/security/audit", headers={"Authorization": "Bearer <admin_token>"})
    assert response.status_code == 200
    assert "logs" in response.json()
```

## Bonnes pratiques
- Couverture maximale, mocks, fixtures, audit logs.
- Sécurité et conformité RGPD.
- Tests multilingues et multi-rôles.
