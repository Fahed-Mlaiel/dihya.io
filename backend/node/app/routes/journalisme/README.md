# Module Journalisme – Dihya Backend Node.js

## Description
API RESTful & GraphQL pour la gestion de projets journalisme (articles, auteurs, publications, etc.), sécurisée, multitenant, extensible, RGPD, plugins, SEO, audit, i18n, fallback IA.

## Fonctionnalités principales
- Gestion des articles, auteurs, publications
- Sécurité maximale (CORS, JWT, WAF, anti-DDOS, validation)
- Multitenancy, gestion des rôles (admin, journaliste, invité)
- Internationalisation dynamique (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es)
- Plugins extensibles (API/CLI)
- Fallback IA open source (LLaMA, Mixtral, Mistral)
- RGPD, audit, export, anonymisation
- SEO backend (robots.txt, sitemap.xml, logs structurés)
- Documentation intégrée, exemples d’utilisation

## Exemples d’utilisation
```bash
# Création d’un article
POST /api/journalisme/articles
{
  "titre": "Dihya révolutionne l’IA",
  "auteur": "Nora",
  "date": "2025-05-25"
}

# Récupération multilingue
GET /api/journalisme/articles?lang=es
```

## Sécurité & RGPD
- JWT obligatoire, CORS dynamique, logs auditables, export RGPD, anonymisation, plugins sandboxés.

## Multilingue
- Français, English, العربية, ⴰⵎⴰⵣⵉⵖ, Deutsch, 中文, 日本語, 한국어, Nederlands, עברית, فارسی, हिन्दी, Español.

---

# Journalism Module – Dihya Backend Node.js

## Description
RESTful & GraphQL API for journalism project management (articles, authors, publications, etc.), secure, multitenant, extensible, RGPD, plugins, SEO, audit, i18n, AI fallback.

## Main Features
- Manage articles, authors, publications
- Maximum security (CORS, JWT, WAF, anti-DDOS, validation)
- Multitenancy, role management (admin, journalist, guest)
- Dynamic internationalization (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es)
- Extensible plugins (API/CLI)
- Open source AI fallback (LLaMA, Mixtral, Mistral)
- RGPD, audit, export, anonymization
- Backend SEO (robots.txt, sitemap.xml, structured logs)
- Integrated documentation, usage examples

## Usage Examples
```bash
# Create an article
POST /api/journalisme/articles
{
  "titre": "Dihya revolutionizes AI",
  "auteur": "Nora",
  "date": "2025-05-25"
}

# Multilingual retrieval
GET /api/journalisme/articles?lang=es
```

## Security & RGPD
- JWT required, dynamic CORS, auditable logs, RGPD export, anonymization, sandboxed plugins.

## Multilingual
- Français, English, العربية, ⴰⵎⴰⵣⵉⵖ, Deutsch, 中文, 日本語, 한국어, Nederlands, עברית, فارسی, हिन्दी, Español.
