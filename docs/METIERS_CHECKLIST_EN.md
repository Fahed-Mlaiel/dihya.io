# Dihya Coding – Metiers Checklist (EN)

This document lists the control points for each business domain (AI, VR, AR, web, mobile, security, GDPR, accessibility, i18n, plugins, etc.) to ensure compliance, security, performance, and extensibility.

## Global checklist
- [ ] Maximum security (CORS, JWT, WAF, anti-DDOS, audit, GDPR anonymization)
- [ ] Dynamic internationalization (fr, en, ar, de, etc.)
- [ ] Accessibility (WCAG 2.1 AA, axe/Lighthouse audit)
- [ ] Multitenancy, role management (admin, user, guest)
- [ ] Extensible, sandboxed, audited plugins
- [ ] Automatic project generation (web, mobile, AI, etc.)
- [ ] Complete tests (unit, integration, e2e, mocks, fixtures)
- [ ] CI/CD deployment (GitHub Actions, Docker, K8s, local fallback)
- [ ] Exhaustive, up-to-date, multilingual documentation
- [ ] Structured, exportable, auditable logs
- [ ] GDPR compliance, export/anonymization, access logs
- [ ] Backend SEO (robots, sitemap, logs)

## Checklist by domain
- AI: open source fallback, auditability, explainability, model security
- VR/AR: performance, accessibility, device compatibility, logs
- Web/mobile: responsive, SEO, accessibility, i18n, security
- Security: WAF, anti-DDOS, logs, audit, GDPR, penetration tests
- Plugins: API/CLI, sandbox, audit, documentation, tests

---

For each release, validate every point in this checklist.
