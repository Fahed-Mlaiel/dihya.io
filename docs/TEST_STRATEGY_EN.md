# Dihya Coding – Test Strategy (EN)

## Introduction
All code must be fully tested (unit, integration, e2e) with structured fixtures, mocks, and audit logs. Tests cover all roles (admin, user, guest) and all supported languages.

## Test Types
- Unit: functions, models, plugins
- Integration: API, DB, plugins, i18n, security
- E2E: user flows (web, mobile, API)
- Security: JWT, CORS, WAF, anti-DDOS, RBAC
- Accessibility: WCAG 2.2, ARIA

## Running Tests
```bash
make test
```

## Coverage
- Minimum: 95%
- Critical modules: 100%

## Fixtures & Audit
- Use `tests/fixtures/`
- All logs are auditable/exportable (GDPR)

---
© 2025 Dihya Coding. All rights reserved.
