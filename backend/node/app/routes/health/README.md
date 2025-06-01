# Module Santé – Dihya Backend Node.js

## Description
API RESTful & GraphQL pour la gestion de projets santé (patients, dossiers, traitements, etc.), sécurisée, multitenant, extensible, RGPD, plugins, SEO, audit, i18n, fallback IA.

## Fonctionnalités principales
- Gestion des patients, dossiers, traitements
- Sécurité maximale (CORS, JWT, WAF, anti-DDOS, validation)
- Multitenancy, gestion des rôles (admin, médecin, invité)
- Internationalisation dynamique (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es)
- Plugins extensibles (API/CLI)
- Fallback IA open source (LLaMA, Mixtral, Mistral)
- RGPD, audit, export, anonymisation
- SEO backend (robots.txt, sitemap.xml, logs structurés)
- Documentation intégrée, exemples d’utilisation

## Exemples d’utilisation
```bash
# Création d’un patient
POST /api/health/patients
{
  "nom": "Amina",
  "age": 32,
  "maladie": "diabète"
}

# Récupération multilingue
GET /api/health/patients?lang=fa
```

## Sécurité & RGPD
- JWT obligatoire, CORS dynamique, logs auditables, export RGPD, anonymisation, plugins sandboxés.

## Multilingue
- Français, English, العربية, ⴰⵎⴰⵣⵉⵖ, Deutsch, 中文, 日本語, 한국어, Nederlands, עברית, فارسی, हिन्दी, Español.

---

# Health Module – Dihya Backend Node.js

## Description
RESTful & GraphQL API for health project management (patients, records, treatments, etc.), secure, multitenant, extensible, RGPD, plugins, SEO, audit, i18n, AI fallback.

## Main Features
- Manage patients, records, treatments
- Maximum security (CORS, JWT, WAF, anti-DDOS, validation)
- Multitenancy, role management (admin, doctor, guest)
- Dynamic internationalization (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es)
- Extensible plugins (API/CLI)
- Open source AI fallback (LLaMA, Mixtral, Mistral)
- RGPD, audit, export, anonymization
- Backend SEO (robots.txt, sitemap.xml, structured logs)
- Integrated documentation, usage examples

## Usage Examples
```bash
# Create a patient
POST /api/health/patients
{
  "nom": "Amina",
  "age": 32,
  "maladie": "diabetes"
}

# Multilingual retrieval
GET /api/health/patients?lang=fa
```

## Security & RGPD
- JWT required, dynamic CORS, auditable logs, RGPD export, anonymization, sandboxed plugins.

## Multilingual
- Français, English, العربية, ⴰⵎⴰⵣⵉⵖ, Deutsch, 中文, 日本語, 한국어, Nederlands, עברית, فارسی, हिन्दी, Español.
