# Utils – API & Documentation

Ce module fournit des utilitaires backend (validation, logs, i18n, plugins, etc.) pour projets IA, VR, AR, etc.

- API RESTful & GraphQL (multilingue, sécurisé, RGPD, plugins)
- Validation, logs, audit, anonymisation, export
- Extensible par plugins

## Endpoints
- `GET /utils/validate` : Validation de données
- `GET /utils/logs` : Logs structurés

## Multilingue
Support : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es

## Sécurité
- JWT, CORS, WAF, anti-DDOS, audit, anonymisation, RGPD

## Plugins
Ajoutez des modules utilitaires via API/CLI (voir `/plugins`)

## Tests
Tests unitaires, intégration, e2e fournis dans `/tests/utils/`

## Déploiement
Compatible Docker, K8s, GitHub Actions, Codespaces, Linux.
