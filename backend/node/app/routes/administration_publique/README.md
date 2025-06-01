# Module Administration Publique – Dihya Backend Node.js

## Description
API RESTful & GraphQL pour la gestion de l’administration publique (démarches, documents, citoyens, etc.), sécurisée, multitenant, extensible, RGPD, plugins, SEO, audit, i18n, fallback IA.

## Fonctionnalités principales
- Gestion des démarches, documents, citoyens, agents
- Sécurité maximale (CORS, JWT, WAF, anti-DDOS, validation)
- Multitenancy, gestion des rôles (admin, agent, citoyen, invité)
- Internationalisation dynamique (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es)
- Plugins extensibles (API/CLI)
- Fallback IA open source (LLaMA, Mixtral, Mistral)
- RGPD, audit, export, anonymisation
- SEO backend (robots.txt, sitemap.xml, logs structurés)
- Documentation intégrée, exemples d’utilisation

## Exemples d’utilisation
```bash
# Création d’une démarche
POST /api/administration_publique/demarches
{
  "type": "Passeport",
  "citoyen": "user1"
}

# Récupération multilingue
GET /api/administration_publique/demarches?lang=ar
```

## Sécurité & RGPD
- JWT obligatoire, CORS dynamique, logs auditables, export RGPD, anonymisation, plugins sandboxés.

## Multilingue
- Français, English, العربية, ⴰⵎⴰⵣⵉⵖ, Deutsch, 中文, 日本語, 한국어, Nederlands, עברית, فارسی, हिन्दी, Español.

---

# Public Administration Module – Dihya Backend Node.js

## Description
RESTful & GraphQL API for public administration management (procedures, documents, citizens, etc.), secure, multitenant, extensible, RGPD, plugins, SEO, audit, i18n, AI fallback.

## Main Features
- Manage procedures, documents, citizens, agents
- Maximum security (CORS, JWT, WAF, anti-DDOS, validation)
- Multitenancy, role management (admin, agent, citizen, guest)
- Dynamic internationalization (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es)
- Extensible plugins (API/CLI)
- Open source AI fallback (LLaMA, Mixtral, Mistral)
- RGPD, audit, export, anonymization
- Backend SEO (robots.txt, sitemap.xml, structured logs)
- Integrated documentation, usage examples

## Usage Examples
```bash
# Create a procedure
POST /api/administration_publique/demarches
{
  "type": "Passport",
  "citizen": "user1"
}

# Multilingual retrieval
GET /api/administration_publique/demarches?lang=ar
```

## Security & RGPD
- JWT required, dynamic CORS, auditable logs, RGPD export, anonymization, sandboxed plugins.

## Multilingual
- Français, English, العربية, ⴰⵎⴰⵣⵉⵖ, Deutsch, 中文, 日本語, 한국어, Nederlands, עברית, فارسی, हिन्दी, Español.
