# 3D SECURITY GUIDE – Dihya (EN)

This guide details all requirements, best practices, tools, and security tests for the 3D module (API, plugins, GDPR, CI/CD).

## Requirements
- Strict CORS, mandatory JWT, WAF, anti-DDOS, strict validation
- RBAC, structured logs, monitoring, auditability
- Automated intrusion tests (XSS, injection, brute-force, anti-bot, CSRF)
- GDPR export/delete, anonymization, exportable logs

## Tests
- `pytest tests/test_security_e2e.py`
- Brute-force, XSS, injection, anti-bot, CSRF checks

## Contribution
- All new routes, plugins, or templates must be security-tested.
- See global API_SECURITY_GUIDE.md for Dihya methodology.
