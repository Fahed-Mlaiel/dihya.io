# Dihya Coding – Threat Model

## Overview
Dihya Coding is designed with a defense-in-depth approach, covering all layers (API, plugins, DB, infra, CI/CD). The threat model is regularly updated and audited.

## Threats Considered
- **Authentication/Authorization**: JWT, RBAC, multitenancy
- **Input Validation**: All API inputs validated (OWASP Top 10)
- **CORS, CSRF, XSS, SSRF, SQLi, RCE**: Mitigated via framework and custom middleware
- **Plugin Isolation**: Sandboxed, permissioned, auditable
- **AI/ML Security**: Prompt injection, model poisoning, fallback to open-source models
- **DDoS & Bot Protection**: WAF, rate limiting, anti-bot
- **Data Privacy**: GDPR, anonymization, export, audit logs
- **Supply Chain**: Dependency scanning, SBOM, signed releases

## Security Controls
- All endpoints require JWT (except login/register)
- CORS strict policy
- WAF and rate limiting enabled
- All actions logged and auditable
- Plugins reviewed and sandboxed
- Regular penetration tests

## Audit & Compliance
- All logs are exportable and GDPR-compliant
- Security incidents are documented and reviewed

---
© 2025 Dihya Coding. All rights reserved.
