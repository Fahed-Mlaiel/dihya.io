# Provenance & Traçabilité du Code – Dihya Compliance

Ce dossier centralise la gestion de la provenance, la traçabilité, l’auditabilité et l’export des logs de génération pour la plateforme Dihya Coding.

## 📚 Contenu du dossier
- **log_provenance.py** : Module de gestion des logs de provenance (génération, export, audit, plugins, i18n, REST/GraphQL)
- **test_log_provenance.py** : Tests unitaires, intégration, e2e, audit, RGPD, multilingue
- **README.md** : Présentation, bonnes pratiques, exemples, multilingue

## 🛡️ Sécurité & conformité
- Sécurité maximale : CORS, JWT, validation stricte, audit, WAF, anti-DDOS, anonymisation RGPD
- Multitenancy, gestion des rôles (admin, user, invité)
- Internationalisation dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
- Extensible via plugins (ajout API/CLI)
- Auditabilité : logs structurés, export, anonymisation, accès exportable
- Conformité RGPD, portabilité, droit à l’oubli

## 🔗 Liens utiles
- [Guide RGPD](../../../LEGAL_COMPLIANCE_GUIDE.md)
- [Guide audit](../../../AUDIT_LOGGING_GUIDE.md)
- [API OpenAPI](../../../openapi.yaml)
- [README global](../../../README.md)

## 📖 Documentation interactive OpenAPI/Swagger

- La documentation interactive de l’API de provenance/auditabilité conforme RGPD, sécurité, plugins, multilingue est générée automatiquement :
  - [openapi_log_provenance.yaml](./openapi_log_provenance.yaml)
  - Compatible Swagger UI, Redoc, Postman, GraphQL Playground
  - Authentification JWT, CORS, WAF, anti-DDOS, auditabilité, anonymisation, plugins, fallback IA
  - Internationalisation dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)

### Exemple d’utilisation Swagger UI

```bash
# Lancer un serveur local de documentation interactive (nécessite swagger-ui ou redoc-cli)
npx swagger-ui-watcher ./openapi_log_provenance.yaml
# ou
npx redoc-cli serve ./openapi_log_provenance.yaml
```

- Documentation également intégrée dans les routes FastAPI/GraphQL (voir exemples dans log_provenance.py)

## 🧑‍💻 Bonnes pratiques
- Documenter chaque modification (audit, logs, reviewers)
- Traduire chaque message dans toutes les langues supportées
- Tester chaque fonction (unit, intégration, e2e)
- Utiliser les plugins pour anonymisation, conformité, extension
- Ne jamais stocker de données sensibles sans consentement explicite

## 📝 Exemples d’utilisation

### Exemple d’enregistrement de provenance (Python)
```python
from log_provenance import ProvenanceLogger, ProvenanceEvent
logger = ProvenanceLogger()
event = ProvenanceEvent(
    user_id="u1", action="generate_project", details={"stack": "AI+VR"}, lang="fr"
)
logger.log_event(event)
```

### Exemple d’export (API REST)
```http
POST /api/provenance/export
Authorization: Bearer <JWT>
Content-Type: application/json
{
  "tenant_id": "t1", "format": "json", "lang": "en"
}
```

## 🌍 Exemples d’appels API multilingues (REST)

### Provenance (français)
```bash
curl -X POST https://api.dihya.com/api/compliance/provenance/log \
  -H "Authorization: Bearer <JWT>" \
  -H "Content-Type: application/json" \
  -d '{
    "tenant_id": "t1",
    "user_id": "u1",
    "role": "admin",
    "event": "export",
    "details": {"ip": "1.2.3.4"},
    "lang": "fr"
  }'
```

### Provenance (anglais)
```bash
curl -X POST https://api.dihya.com/api/compliance/provenance/log \
  -H "Authorization: Bearer <JWT>" \
  -H "Content-Type: application/json" \
  -d '{
    "tenant_id": "t1",
    "user_id": "u1",
    "role": "admin",
    "event": "export",
    "details": {"ip": "1.2.3.4"},
    "lang": "en"
  }'
```

### Provenance (arabe)
```bash
curl -X POST https://api.dihya.com/api/compliance/provenance/log \
  -H "Authorization: Bearer <JWT>" \
  -H "Content-Type: application/json" \
  -d '{
    "tenant_id": "t1",
    "user_id": "u1",
    "role": "admin",
    "event": "export",
    "details": {"ip": "1.2.3.4"},
    "lang": "ar"
  }'
```

---

> **Dihya Coding : traçabilité, sécurité, conformité, auditabilité, extensibilité, souveraineté, multilingue.**
