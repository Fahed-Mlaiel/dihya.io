# voice

# Tests d'intégration Voice

Ce dossier contient les tests d'intégration pour les modules voice (synthèse, reconnaissance, IA, etc.).

## Structure
- **Tests RESTful et GraphQL** pour voice.
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
Test d'intégration voice (synthèse vocale)
"""
import pytest
from backend.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_voice_synthesis():
    response = client.post("/api/voice/synthesize", json={"text": "Bonjour Dihya"}, headers={"Authorization": "Bearer <token>"})
    assert response.status_code == 200
    assert "audio" in response.json()
```

## Bonnes pratiques
- Couverture maximale, mocks, fixtures, audit logs.
- Sécurité et conformité RGPD.
- Tests multilingues et multi-rôles.
