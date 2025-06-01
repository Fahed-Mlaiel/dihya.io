# Guide d’Intégration – Dihya Coding

Ce guide explique comment intégrer Dihya Coding dans vos projets, connecter des services externes, ajouter des plugins, et exploiter l’API (REST/GraphQL) de façon sécurisée et multilingue.

## Intégration API
- Authentification JWT, CORS, rôles, audit logging
- Endpoints REST : `/projects`, `/users`, `/plugins`, `/generate`, etc.
- Endpoint GraphQL : `/graphql` (requêtes multilingues, filtrage par rôle)

## Services externes
- Intégration IA (LLaMA, Mixtral, Mistral) via plugins ou API
- Webhooks, OAuth2, SSO, notifications (Slack, Matrix, Email)

## Plugins
- Ajout dynamique via API ou CLI
- Sécurité : sandbox, audit, logs, RGPD
- Exemple : voir `PLUGINS_README.md`

## Internationalisation
- API et UI multilingues (fr, en, ar, de, etc.)
- Ajout de langues via `/i18n/` et configuration

## Sécurité
- Respect des politiques (`securite_GUIDE.md`)
- Validation, WAF, anti-DDOS, anonymisation RGPD

## Tests d’intégration
- Utiliser les fixtures/mocks fournis
- Automatiser avec CI/CD (GitHub Actions, Docker)

## Déploiement
- Docker, K8s, fallback local
- Workflows CI/CD prêts à l’emploi

---

Pour toute question, voir les guides d’intégration, d’API, et contacter les mainteneurs.
