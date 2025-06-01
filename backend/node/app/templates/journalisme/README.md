# Template Journalisme – Dihya Coding

Ce template fournit une base avancée pour la gestion de projets de journalisme (articles, workflows, IA, multilingue, sécurité, RGPD, plugins, etc.).

## Fonctionnalités principales
- API RESTful & GraphQL, multitenant, rôles (admin, rédacteur, lecteur, invité)
- Sécurité maximale (CORS, JWT, WAF, anti-DDOS, validation, audit)
- Internationalisation dynamique (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- Intégration IA (LLaMA, Mixtral, fallback open source)
- Extensible par plugins (API/CLI)
- RGPD, logs structurés, anonymisation, export
- SEO backend (robots, sitemap, logs)
- Tests complets (unit, intégration, e2e)

## Utilisation
1. Personnalisez `template.js` et `policy.md` selon vos besoins métier.
2. Déployez via Docker, K8s, GitHub Actions, ou local.
3. Ajoutez des plugins via l’API ou CLI.

## Exemples d’API
- `GET /api/journalisme/articles` : liste des articles
- `POST /api/journalisme/publish` : publier un article

## Multilingue
Toutes les routes et messages sont disponibles en 12+ langues.

## Sécurité
Voir `policy.md` pour la politique complète.

## Tests
Voir `test_journalisme.js` pour une couverture maximale.

---

# Journalism Template – Dihya Coding (EN)

This template provides an advanced base for journalism projects (articles, workflows, AI, multilingual, security, GDPR, plugins, etc.).

*See French section above for full details.*
