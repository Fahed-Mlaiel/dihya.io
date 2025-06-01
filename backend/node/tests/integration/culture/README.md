# culture

# Integration Tests – Culture Module

## Purpose
This directory contains advanced integration tests for all routes, plugins, and modules related to cultural project management (museums, heritage, events, etc.) in the Dihya platform.

## Requirements
- Full coverage of REST and GraphQL APIs (CRUD, multitenancy, roles, security, i18n, GDPR, audit, plugins, fallback AI, etc.)
- Use of fixtures, mocks, and multilingual data (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- GDPR compliance, auditability, anonymization, exportability
- Integration with AI services (LLaMA, Mixtral, Mistral)
- Security tests (CORS, JWT, WAF, anti-DDOS, validation, structured logs)
- Example requests and responses for each endpoint
- Ready for CI/CD, Codespaces, Docker, K8s

## Structure
- `test_culture_api.integration.test.js`: REST/GraphQL API tests
- `fixtures/`: multilingual, multi-role test data
- `mock_services/`: AI, plugin, security mocks

## Run
```bash
npm run test:integration -- culture
```

## Multilingual
All assertions and data cover Dihya's supported languages.

## Contribution
See [CONTRIBUTING.md](../../../CONTRIBUTING.md)
