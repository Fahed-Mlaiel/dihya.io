# 3D GDPR GUIDE – Dihya (EN)

This guide details all requirements, best practices, tools, and GDPR tests for the 3D module (API, plugins, export, anonymization, logs, CI/CD).

## Requirements
- GDPR export/delete, anonymization, exportable logs, auditability
- User consent, exportable access, deletion on request
- CI/CD compliance, auditability, monitoring

## Tests
- `pytest tests/test_rgpd.py`
- Export/anonymization/deletion, audit, GDPR logs

## Contribution
- All new routes, plugins, or templates must be GDPR-compliant and tested.
- See global LEGAL_COMPLIANCE_GUIDE.md for Dihya methodology.
