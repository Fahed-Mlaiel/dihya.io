# Dihya Architecture (EN)

## Overview
Dihya is a sovereign, ultra-secure, multi-tenant, multi-language platform for AI, VR, AR, Voice, and Web/Mobile project generation.

### Key Principles
- RESTful + GraphQL API, plugin system, dynamic i18n (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
- Maximum security (CORS, JWT, WAF, anti-DDOS, audit, RGPD)
- Multi-stack: backend, frontend, mobile, VR/AR, scripts
- Extensible: plugins via API/CLI, custom business modules
- SEO, accessibility, auditability, export, anonymization
- 100% Codespaces/Linux/CI compatible

### Main Components
- API Gateway (FastAPI/Flask, GraphQL, OpenAPI)
- Auth & RBAC/ABAC (JWT, multi-tenant, admin/user/guest)
- Project Generator (web, mobile, IA, VR/AR, Voice)
- Plugin Engine (dynamic loading, API/CLI)
- Audit/Logs (structured, exportable, anonymizable)
- CI/CD (GitHub Actions, Docker, K8s, fallback local)

### See ARCHITECTURE_DIAGRAM.png for the full diagram.
