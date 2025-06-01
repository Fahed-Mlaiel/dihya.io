# seo

# Tests d'intégration SEO

Ce dossier contient les tests d'intégration pour les modules SEO (robots.txt, sitemap, logs structurés, etc.).

## Structure
- **Tests RESTful et GraphQL** pour SEO.
- **Sécurité** : JWT, CORS, validation, audit, WAF, anti-DDOS.
- **Multilingue** : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.
- **SEO** : robots.txt, sitemap dynamique, logs structurés.
- **Auditabilité** : logs, anonymisation, export.

## Exécution
```bash
pytest --tb=short --maxfail=1
```

## Exemple de test
```python
"""
Test d'intégration SEO (sitemap)
"""
import pytest
from backend.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_sitemap():
    response = client.get("/api/seo/sitemap.xml")
    assert response.status_code == 200
    assert "<urlset" in response.text
```

## Bonnes pratiques
- Couverture maximale, mocks, fixtures, audit logs.
- Sécurité et conformité RGPD.
- Tests multilingues et multi-rôles.
