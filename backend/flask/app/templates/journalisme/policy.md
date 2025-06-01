# Politique de gestion des projets de journalisme

- Sécurité maximale (CORS, JWT, validation, audit, WAF, anti-DDOS)
- Internationalisation dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
- Modèle RESTful + support GraphQL
- Multitenancy + gestion des rôles (admin, user, invité)
- Conformité RGPD, auditabilité, anonymisation, logs exportables
- Plugins extensibles (API/CLI)
- Tests complets (unit, integration, e2e)
- Déploiement GitHub Actions, Docker, K8s, fallback local
- SEO backend (robots, sitemap dynamique, logs structurés)
- Code 100% compatible Codespaces/Linux/CI

## Exigences spécifiques
- Toute création/modification de projet doit être auditée et validée.
- Les accès sont strictement contrôlés par JWT et rôles.
- Les données sensibles sont anonymisées et exportables.
- Les plugins doivent pouvoir enrichir les projets journalisme sans redéploiement.
- Les logs sont structurés, horodatés, et exportables.
- L'API doit être multilingue et accessible.
