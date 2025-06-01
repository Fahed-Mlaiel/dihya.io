# README – Dihya Backend Plugins

Ce dossier contient les plugins backend de Dihya : extensions, modules métiers, intégrations, sécurité, tests, etc.

- Architecture plugin, conventions, sécurité, multilingue
- Exemples d’utilisation, scripts, tests, contribution

Voir [../README.md](../README.md), [../../PLUGINS_GUIDE.md](../../PLUGINS_GUIDE.md)

## 📖 Documentation interactive OpenAPI/Swagger

- La documentation interactive de l’API plugins backend (sécurité, RGPD, audit, multilingue, extensible) est générée automatiquement :
  - [openapi_plugins.yaml](./openapi_plugins.yaml)
  - Compatible Swagger UI, Redoc, Postman, GraphQL Playground
  - Authentification JWT, CORS, WAF, anti-DDOS, auditabilité, anonymisation, plugins, fallback IA
  - Internationalisation dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)

### Exemple d’utilisation Swagger UI

```bash
npx swagger-ui-watcher ./openapi_plugins.yaml
# ou
npx redoc-cli serve ./openapi_plugins.yaml
```

- Documentation également intégrée dans les routes FastAPI/GraphQL (voir exemples dans les plugins Python/JS)

## 🌍 Exemples d’appels API multilingues (REST)

### Liste des plugins (français)
```bash
curl -X GET https://api.dihya.com/api/plugins/list \
  -H "Authorization: Bearer <JWT>" \
  -H "Accept-Language: fr"
```

### Liste des plugins (anglais)
```bash
curl -X GET https://api.dihya.com/api/plugins/list \
  -H "Authorization: Bearer <JWT>" \
  -H "Accept-Language: en"
```

### Activation d’un plugin (arabe)
```bash
curl -X POST https://api.dihya.com/api/plugins/activate \
  -H "Authorization: Bearer <JWT>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "audit-pro",
    "lang": "ar"
  }'
```
