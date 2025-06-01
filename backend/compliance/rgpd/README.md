# RGPD – Dihya Compliance

Ce dossier regroupe les scripts, modules et documentations liés à la conformité RGPD : anonymisation, export, suppression, consentement, logs, auditabilité.

- Scripts d’anonymisation et d’export RGPD
- Documentation sur la gestion des droits utilisateurs
- Exemples d’API d’export/suppression
- Tests unitaires et d’intégration RGPD

## 📖 Documentation interactive OpenAPI/Swagger

- La documentation interactive de l’API RGPD (export, suppression, consentement, multilingue, plugins, audit, sécurité) est générée automatiquement :
  - [openapi_rgpd.yaml](./openapi_rgpd.yaml)
  - Compatible Swagger UI, Redoc, Postman, GraphQL Playground
  - Authentification JWT, CORS, WAF, anti-DDOS, auditabilité, anonymisation, plugins, fallback IA
  - Internationalisation dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)

### Exemple d’utilisation Swagger UI

```bash
npx swagger-ui-watcher ./openapi_rgpd.yaml
# ou
npx redoc-cli serve ./openapi_rgpd.yaml
```

- Documentation également intégrée dans les routes FastAPI/GraphQL (voir exemples dans export_rgpd.py)

## 📖 Documentation interactive GraphQL RGPD

- La documentation interactive de l’API GraphQL RGPD (export, suppression, consentement, multilingue, plugins, audit, sécurité) est générée automatiquement :
  - [openapi_graphql_rgpd.yaml](./openapi_graphql_rgpd.yaml)
  - Compatible GraphQL Playground, Altair, Postman, Swagger UI (description), Redoc
  - Authentification JWT, CORS, WAF, anti-DDOS, auditabilité, anonymisation, plugins, fallback IA
  - Internationalisation dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)

### Exemple d’utilisation GraphQL Playground

```bash
npx graphql-playground ./openapi_graphql_rgpd.yaml
```

- Documentation également intégrée dans les schémas GraphQL Python (voir exemples dans export_rgpd.py)

## 🌍 Exemples d’appels API multilingues (export, suppression, consentement)

Voir [EXAMPLES_API_RGPD.md](./EXAMPLES_API_RGPD.md) pour des exemples concrets d’appels API RGPD (fr, en, ar, ber, de, zh, ja, ko, nl, he, fa, hi, es, curl, multilingue).

## 🌍 Exemples d’appels GraphQL multilingues (export, suppression, consentement, erreurs)

Voir [EXAMPLES_GRAPHQL_RGPD.md](./EXAMPLES_GRAPHQL_RGPD.md) pour des exemples concrets d’appels GraphQL RGPD (fr, en, ar, ber, de, zh, ja, ko, nl, he, fa, hi, es, mutations, erreurs, multilingue).
