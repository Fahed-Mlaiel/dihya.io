# Module Hôtellerie – Dihya Backend Node.js

## Description
API RESTful & GraphQL pour la gestion de projets hôtellerie (réservations, chambres, clients, etc.), sécurisée, multitenant, extensible, RGPD, plugins, SEO, audit, i18n, fallback IA.

## Fonctionnalités principales
- Gestion des réservations, chambres, clients
- Sécurité maximale (CORS, JWT, WAF, anti-DDOS, validation)
- Multitenancy, gestion des rôles (admin, réceptionniste, invité)
- Internationalisation dynamique (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es)
- Plugins extensibles (API/CLI)
- Fallback IA open source (LLaMA, Mixtral, Mistral)
- RGPD, audit, export, anonymisation
- SEO backend (robots.txt, sitemap.xml, logs structurés)
- Documentation intégrée, exemples d’utilisation

## Exemples d’utilisation
```bash
# Création d’une réservation
POST /api/hotellerie/reservations
{
  "client": "Karim",
  "chambre": "101",
  "date": "2025-06-01"
}

# Récupération multilingue
GET /api/hotellerie/reservations?lang=ko
```

## Sécurité & RGPD
- JWT obligatoire, CORS dynamique, logs auditables, export RGPD, anonymisation, plugins sandboxés.

## Multilingue
- Français, English, العربية, ⴰⵎⴰⵣⵉⵖ, Deutsch, 中文, 日本語, 한국어, Nederlands, עברית, فارسی, हिन्दी, Español.

---

# Hospitality Module – Dihya Backend Node.js

## Description
RESTful & GraphQL API for hospitality project management (reservations, rooms, clients, etc.), secure, multitenant, extensible, RGPD, plugins, SEO, audit, i18n, AI fallback.

## Main Features
- Manage reservations, rooms, clients
- Maximum security (CORS, JWT, WAF, anti-DDOS, validation)
- Multitenancy, role management (admin, receptionist, guest)
- Dynamic internationalization (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es)
- Extensible plugins (API/CLI)
- Open source AI fallback (LLaMA, Mixtral, Mistral)
- RGPD, audit, export, anonymization
- Backend SEO (robots.txt, sitemap.xml, structured logs)
- Integrated documentation, usage examples

## Usage Examples
```bash
# Create a reservation
POST /api/hotellerie/reservations
{
  "client": "Karim",
  "chambre": "101",
  "date": "2025-06-01"
}

# Multilingual retrieval
GET /api/hotellerie/reservations?lang=ko
```

## Security & RGPD
- JWT required, dynamic CORS, auditable logs, RGPD export, anonymization, sandboxed plugins.

## Multilingual
- Français, English, العربية, ⴰⵎⴰⵣⵉⵖ, Deutsch, 中文, 日本語, 한국어, Nederlands, עברית, فارسی, हिन्दी, Español.
