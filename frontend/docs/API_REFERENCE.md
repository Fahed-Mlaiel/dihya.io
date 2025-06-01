# API Reference – Dihya

## Overview
Dihya exposes a secure, extensible, multilingual API (REST & GraphQL) for all métiers (tourisme, transport, VR/AR, etc.), with full RBAC, multitenancy, plugins, audit, RGPD, SEO, and accessibility.

## Authentication & Security
- JWT, CORS, WAF, anti-DDOS, audit logging, RBAC (admin, user, invité)
- Plugins security (API/CLI)

## Internationalization
- Dynamic: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
- Fallback open source AI (LLaMA, Mixtral, Mistral)

## REST Endpoints (examples)
- `GET /api/tourisme/sites` – List sites (i18n, SEO, RBAC)
- `POST /api/transport/flottes` – Create fleet (validation, audit)
- `POST /api/voice/speech-to-text` – Speech recognition (multilingual, secure)
- `GET /api/vr_ar/experiences` – List VR/AR experiences (SEO, i18n)

## GraphQL
- `POST /graphql` – Custom queries for all métiers (secure, plugins, i18n)

## Plugins
- Add/extend API via API/CLI (ex: météo, analyse IA, assets 3D)

## RGPD & Audit
- Data anonymization, export, structured logs, full compliance

## SEO & Accessibility
- Dynamic sitemap, robots.txt, logs, WCAG

## Example Query
```http
GET /api/tourisme/sites?lang=de
POST /graphql { "query": "{ vrArExperiences(lang: \"ar\") { id name } }" }
```

## Structure
- Code, tests, assets, configs, docs, plugins, policies, etc.
