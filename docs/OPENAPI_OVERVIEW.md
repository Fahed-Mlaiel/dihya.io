# Dihya Coding – OpenAPI Overview

## Introduction
Dihya Coding exposes a secure, extensible, multilingual RESTful and GraphQL API for managing AI, VR, AR, web, and mobile projects. The API is designed for maximum security (CORS, JWT, WAF, anti-DDOS), internationalization, multitenancy, plugin extensibility, and full auditability (GDPR compliant).

## Key Features
- **RESTful & GraphQL endpoints**
- **Dynamic i18n**: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
- **Role-based access**: admin, user, guest
- **Multitenancy**
- **Plugin system**: add/extend endpoints via API/CLI
- **AI integration**: fallback to open-source LLaMA, Mixtral, Mistral
- **SEO optimization**: robots.txt, dynamic sitemap, structured logs
- **Security**: JWT, CORS, WAF, anti-DDOS, validation, audit logs
- **RGPD compliance**: anonymization, export, logs

## Authentication
- JWT Bearer tokens required for all endpoints except `/auth/login` and `/auth/register`.
- CORS enforced on all routes.

## Example Endpoints
- `POST /api/projects` – Create a new project (AI, VR, AR, web, mobile)
- `GET /api/projects` – List all projects (paginated, filterable)
- `POST /api/plugins` – Add a new plugin
- `GET /api/tenants` – List tenants (admin only)
- `POST /api/ai/generate` – Generate code or content via AI (with fallback)

## Internationalization
- All endpoints accept `Accept-Language` header.
- Error and success messages are localized.

## API Documentation
- Full OpenAPI 3.1 spec: [openapi.yaml](../openapi.yaml)
- Interactive docs: `/docs` endpoint (Swagger UI, Redoc)

## Security & Compliance
- All requests logged and auditable.
- GDPR: Data export, anonymization, right to be forgotten.
- Rate limiting, anti-bot, and WAF enabled by default.

## Example Request
```bash
curl -X POST https://api.dihya.dev/api/projects \
  -H 'Authorization: Bearer <token>' \
  -H 'Accept-Language: en' \
  -d '{"type": "ai", "name": "My AI Project"}'
```

---
© 2025 Dihya Coding. All rights reserved.
