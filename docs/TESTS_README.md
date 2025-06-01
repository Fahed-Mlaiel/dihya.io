# Dihya Coding – Tests Guide

## Introduction
This document explains the test strategy, coverage, and best practices for Dihya Coding. All code must be fully tested (unit, integration, e2e) with structured fixtures, mocks, and audit logs. Tests are multilingual and cover all roles (admin, user, guest).

## Test Types
- **Unit tests**: Functions, models, plugins
- **Integration tests**: API, DB, plugins, i18n, security
- **E2E tests**: Full user flows (web, mobile, API)
- **Security tests**: JWT, CORS, WAF, anti-DDOS, RBAC
- **Accessibility tests**: WCAG 2.2, ARIA

## Running Tests
```bash
make test
```
- Or run specific suites: `pytest`, `jest`, `make test-e2e`

## Coverage
- Minimum 95% required
- Coverage reports: `coverage/`, `jest-coverage/`

## Fixtures & Mocks
- Use `tests/fixtures/` for reusable data
- Use `unittest.mock` or `pytest-mock` for Python, `jest` for JS

## Audit & Compliance
- All test logs are auditable and exportable (GDPR)

## Contribution
- See [CONTRIBUTING.md](../CONTRIBUTING.md)

---
© 2025 Dihya Coding. All rights reserved.
