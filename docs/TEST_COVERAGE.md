# Dihya Coding – Test Coverage

## Coverage Policy
- **Minimum required:** 95% (unit, integration, e2e)
- **Critical modules:** 100% (security, plugins, i18n, RBAC, audit)
- **Accessibility:** All user flows tested (WCAG 2.2)

## Tools
- Python: `pytest-cov`, `coverage.py`
- JS/TS: `jest`, `nyc`
- E2E: `playwright`, `cypress`

## Reporting
- Coverage reports in `coverage/` and `jest-coverage/`
- Failing coverage blocks CI/CD

## Example
```bash
pytest --cov=src
jest --coverage
```

## Auditability
- All test runs are logged and exportable (GDPR)

---
© 2025 Dihya Coding. All rights reserved.
