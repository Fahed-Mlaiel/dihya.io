# __api_restful_and_swagger_openapi_documentation

## Overview
This business module provides a complete RESTful API and Swagger/OpenAPI documentation for all business services (Node, Flask, Django, plugins, etc.).

## Main features
- Standardized RESTful endpoints (CRUD, search, export, anonymization)
- Automatically generated Swagger/OpenAPI documentation (`openapi.yaml`)
- GraphQL support (optional)
- Advanced security (OAuth2, JWT, scopes, CORS, rate limiting)
- API plugins (versioning, hooks, audit, GDPR)
- Automated tests (unit, integration, e2e, mocks)
- API client generation (OpenAPI Generator, Postman)

## Usage examples
- `/api/v1/metiers` (GET, POST, PUT, DELETE)
- `/api/v1/docs` (Swagger UI, Redoc)
- `/graphql` (optional)

## Compliance
- OpenAPI 3.1, REST best practices, GDPR, OAuth2

## Tests
- `npm test`, `pytest`, `jest`, `supertest`, `swagger-cli validate`, etc.

## Deployment
- Docker/K8s ready, CI/CD, monitoring, auditability

## Contribution
See `CONTRIBUTING.md` and `API_SECURITY_GUIDE.md`.
