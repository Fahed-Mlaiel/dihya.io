# __api_restful_et_documentation_swagger/openapi

## Présentation
Ce module métier fournit une API RESTful complète et une documentation Swagger/OpenAPI pour tous les services métiers (Node, Flask, Django, plugins, etc.).

## Fonctionnalités principales
- Endpoints RESTful standardisés (CRUD, recherche, export, anonymisation)
- Documentation Swagger/OpenAPI générée automatiquement (`openapi.yaml`)
- Support GraphQL (optionnel)
- Sécurité avancée (OAuth2, JWT, scopes, CORS, rate limiting)
- Plugins d’API (versioning, hooks, audit, RGPD)
- Tests automatisés (unitaires, intégration, e2e, mocks)
- Génération de clients API (OpenAPI Generator, Postman)

## Exemples d’utilisation
- `/api/v1/metiers` (GET, POST, PUT, DELETE)
- `/api/v1/docs` (Swagger UI, Redoc)
- `/graphql` (optionnel)

## Conformité
- OpenAPI 3.1, REST best practices, RGPD, OAuth2

## Tests
- `npm test`, `pytest`, `jest`, `supertest`, `swagger-cli validate`, etc.

## Déploiement
- Docker/K8s ready, CI/CD, monitoring, auditabilité

## Contribution
Voir `CONTRIBUTING.md` et `API_SECURITY_GUIDE.md`.
