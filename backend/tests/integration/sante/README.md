# sante

# Tests d'intégration Santé

Ce dossier contient les tests d'intégration pour les modules santé (dossiers, rendez-vous, anonymisation, export RGPD, etc.).

## Structure
- **Tests RESTful et GraphQL** pour santé.
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
Test d'intégration santé (création dossier patient)
"""
import pytest
from backend.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_patient():
    response = client.post("/api/sante/patients", json={"nom": "Aït", "prenom": "Dihya"}, headers={"Authorization": "Bearer <token>"})
    assert response.status_code == 201
    assert response.json()["nom"] == "Aït"
```

## Bonnes pratiques
- Couverture maximale, mocks, fixtures, audit logs.
- Sécurité et conformité RGPD.
- Tests multilingues et multi-rôles.
