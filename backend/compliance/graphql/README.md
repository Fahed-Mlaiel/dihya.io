# README – Dihya Compliance GraphQL API

Ce dossier contient la documentation interactive OpenAPI/Swagger/GraphQL Playground pour l’API GraphQL conformité, audit, RGPD, plugins, multilingue, extensible.

- [openapi_graphql_compliance.yaml](./openapi_graphql_compliance.yaml)
- Compatible GraphQL Playground, Altair, Postman, Swagger UI (description), Redoc
- Authentification JWT, CORS, WAF, anti-DDOS, auditabilité, anonymisation, plugins, fallback IA
- Internationalisation dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)

## Exemple d’utilisation GraphQL Playground

```bash
# Lancer un serveur local de documentation interactive (nécessite graphql-playground ou altair)
npx graphql-playground ./openapi_graphql_compliance.yaml
```

- Documentation également intégrée dans les schémas GraphQL Python (voir exemples dans log_provenance.py, api_export_policies.py)

## 🌍 Exemples d’appels GraphQL multilingues

Voir [EXAMPLES_GRAPHQL_API.md](./EXAMPLES_GRAPHQL_API.md) pour des exemples concrets d’appels GraphQL (fr, en, ar, curl, mutations, queries, multilingue).
