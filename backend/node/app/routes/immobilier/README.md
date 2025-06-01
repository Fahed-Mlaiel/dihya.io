# Module Immobilier – Dihya Backend Node.js

## Description
API RESTful & GraphQL pour la gestion de projets immobiliers (biens, transactions, locations, etc.), sécurisée, multitenant, extensible, RGPD, plugins, SEO, audit, i18n, fallback IA.

## Fonctionnalités principales
- Gestion des biens, transactions, locations
- Sécurité maximale (CORS, JWT, WAF, anti-DDOS, validation)
- Multitenancy, gestion des rôles (admin, agent, invité)
- Internationalisation dynamique (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es)
- Plugins extensibles (API/CLI)
- Fallback IA open source (LLaMA, Mixtral, Mistral)
- RGPD, audit, export, anonymisation
- SEO backend (robots.txt, sitemap.xml, logs structurés)
- Documentation intégrée, exemples d’utilisation

## Exemples d’utilisation
```bash
# Création d’un bien
POST /api/immobilier/biens
{
  "adresse": "12 rue des Palmiers",
  "type": "appartement",
  "prix": 250000
}

# Récupération multilingue
GET /api/immobilier/biens?lang=nl
```

## Sécurité & RGPD
- JWT obligatoire, CORS dynamique, logs auditables, export RGPD, anonymisation, plugins sandboxés.

## Multilingue
- Français, English, العربية, ⴰⵎⴰⵣⵉⵖ, Deutsch, 中文, 日本語, 한국어, Nederlands, עברית, فارسی, हिन्दी, Español.

---

# Real Estate Module – Dihya Backend Node.js

## Description
RESTful & GraphQL API for real estate project management (properties, transactions, rentals, etc.), secure, multitenant, extensible, RGPD, plugins, SEO, audit, i18n, AI fallback.

## Main Features
- Manage properties, transactions, rentals
- Maximum security (CORS, JWT, WAF, anti-DDOS, validation)
- Multitenancy, role management (admin, agent, guest)
- Dynamic internationalization (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es)
- Extensible plugins (API/CLI)
- Open source AI fallback (LLaMA, Mixtral, Mistral)
- RGPD, audit, export, anonymization
- Backend SEO (robots.txt, sitemap.xml, structured logs)
- Integrated documentation, usage examples

## Usage Examples
```bash
# Create a property
POST /api/immobilier/biens
{
  "adresse": "12 Palm Street",
  "type": "apartment",
  "prix": 250000
}

# Multilingual retrieval
GET /api/immobilier/biens?lang=nl
```

## Security & RGPD
- JWT required, dynamic CORS, auditable logs, RGPD export, anonymization, sandboxed plugins.

## Multilingual
- Français, English, العربية, ⴰⵎⴰⵣⵉⵖ, Deutsch, 中文, 日本語, 한국어, Nederlands, עברית, فارسی, हिन्दी, Español.
