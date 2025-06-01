# Manufacturing – Integration Tests

## Overview
This directory contains advanced integration tests for all manufacturing project management routes, plugins, and modules in Dihya.

## Requirements
- 100% REST/GraphQL API coverage (CRUD, multitenancy, roles, security, i18n, GDPR, audit, plugins, fallback AI, etc.)
- Fixtures, mocks, multilingual data (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- GDPR compliance, audit, anonymization, exportability
- Integration with AI services (LLaMA, Mixtral, Mistral)
- Security (CORS, JWT, WAF, anti-DDOS, validation, structured logs)
- Example requests/responses for each endpoint
- CI/CD, Codespaces, Docker, K8s ready

## Structure
- `test_manufacturing_api.integration.test.js`: REST/GraphQL API tests
- `fixtures/`: multilingual, multi-role test data
- `mock_services/`: AI, plugin, security mocks

## Run
```bash
npm run test:integration -- manufacturing
```

## Multilingual
All assertions and data cover all supported languages.

## Contribution
See [CONTRIBUTING.md](../../../CONTRIBUTING.md)
