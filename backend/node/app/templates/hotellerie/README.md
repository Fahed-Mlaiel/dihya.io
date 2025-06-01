# Template Hôtellerie – Dihya Coding

Ce template fournit une base ultra avancée pour la gestion de projets d’hôtellerie (réservations, gestion clients, services, IA, multilingue, sécurité, RGPD, plugins, etc.).

## Fonctionnalités principales
- API RESTful & GraphQL, multitenant, rôles (admin, user, invité)
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
- `GET /api/hotellerie/rooms` : liste des chambres
- `POST /api/hotellerie/booking` : réservation sécurisée

## Multilingue
Toutes les routes et messages sont disponibles en 12+ langues.

## Sécurité
Voir `policy.md` pour la politique complète.

## Tests
Voir `test_hotellerie.js` pour une couverture maximale.

---

# Hotel Template – Dihya Coding (EN)

This template provides an advanced base for hotel management projects (booking, clients, services, AI, multilingual, security, GDPR, plugins, etc.).

*See French section above for full details.*
