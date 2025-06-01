# Exemples API – Dihya Compliance

Ce document présente des exemples d’utilisation avancée de la politique d’export API, de la gestion RGPD, de l’audit, de l’extensibilité par plugins et de la multilingue.

---

## 1. Exemple d’appel API REST (FastAPI)

```python
from fastapi import APIRouter, Depends, Request
from .api_export_policies import ExportRequest, APIExportPolicy

router = APIRouter()

@router.post("/export", response_model=APIExportPolicy.ExportResponse, tags=["Export"], summary="Export de données conforme RGPD")
async def export_data(req: ExportRequest, request: Request):
    # Authentification, validation JWT, CORS, etc. gérés par FastAPI/middleware
    # Données à exporter récupérées selon le tenant, les filtres, etc.
    data = [{"id": 1, "email": "user@dihya.com", "ip": "1.2.3.4", "ssn": "123-45-6789"}]
    return APIExportPolicy.export(req, data)
```

## 2. Exemple d’appel API GraphQL (Strawberry)

```python
import strawberry
from .api_export_policies import ExportRequest, APIExportPolicy

@strawberry.type
class Mutation:
    @strawberry.mutation
    def export_data(self, input: ExportRequest) -> APIExportPolicy.ExportResponse:
        data = [{"id": 1, "email": "user@dihya.com", "ip": "1.2.3.4", "ssn": "123-45-6789"}]
        return APIExportPolicy.export(input, data)
```

## 3. Exemple d’extension par plugin RGPD

```python
from .api_export_policies import ExportPlugin, APIExportPolicy

class CustomAnonymizerPlugin(ExportPlugin):
    def process(self, data, req):
        for row in data:
            row.pop("phone", None)
        return data

APIExportPolicy.register_plugin(CustomAnonymizerPlugin())
```

## 4. Exemple d’audit log structuré

```python
from .api_export_policies import AuditLog, log_audit

audit = AuditLog(
    audit_id="exp-1234",
    timestamp="2025-05-23T12:00:00Z",
    tenant_id="t1",
    user_id="u1",
    action="export",
    status="success",
    details={"format": "json", "count": 1}
)
log_audit(audit)
```

## 5. Exemple de test unitaire (Pytest)

```python
def test_export_policy():
    from .api_export_policies import ExportRequest, APIExportPolicy, Role, ExportFormat
    req = ExportRequest(tenant_id="t1", user_id="u1", role=Role.admin, format=ExportFormat.json)
    data = [{"id": 1, "email": "user@dihya.com", "ip": "1.2.3.4", "ssn": "123-45-6789"}]
    resp = APIExportPolicy.export(req, data)
    assert resp.status == "success"
    assert resp.export_url is not None
```

## 6. Exemple multilingue (message d’erreur)

```python
from .api_export_policies import get_i18n_message
assert get_i18n_message("export_not_allowed", "ar") == "التصدير غير مسموح."
```

## 🌍 Exemples d’appels API multilingues (REST)

### Export (français)
```bash
curl -X POST https://api.dihya.com/api/compliance/policies/export \
  -H "Authorization: Bearer <JWT>" \
  -H "Content-Type: application/json" \
  -d '{
    "tenant_id": "t1",
    "user_id": "u1",
    "role": "admin",
    "format": "json",
    "lang": "fr"
  }'
```

### Export (anglais)
```bash
curl -X POST https://api.dihya.com/api/compliance/policies/export \
  -H "Authorization: Bearer <JWT>" \
  -H "Content-Type: application/json" \
  -d '{
    "tenant_id": "t1",
    "user_id": "u1",
    "role": "admin",
    "format": "json",
    "lang": "en"
  }'
```

### Export (arabe)
```bash
curl -X POST https://api.dihya.com/api/compliance/policies/export \
  -H "Authorization: Bearer <JWT>" \
  -H "Content-Type: application/json" \
  -d '{
    "tenant_id": "t1",
    "user_id": "u1",
    "role": "admin",
    "format": "json",
    "lang": "ar"
  }'
```

---

> **Dihya Coding : API conforme, extensible, multilingue, auditable, prête pour la production et la contribution.**
