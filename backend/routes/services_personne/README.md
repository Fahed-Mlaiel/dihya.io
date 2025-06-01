# Services à la personne – API & Documentation

Ce module gère les services à la personne (aide, assistance, IA, VR, AR, etc.) pour projets IA, VR, AR, etc.

- API RESTful & GraphQL (multilingue, sécurisé, RGPD, plugins)
- Gestion des rôles (admin, user, invité)
- Intégration IA (matching, suggestion, analyse)
- Audit, logs, anonymisation, export
- Extensible par plugins

## Endpoints
- `GET /services_personne/services` : Liste des services
- `POST /services_personne/demande` : Créer une demande

## Multilingue
Support : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es

## Sécurité
- JWT, CORS, WAF, anti-DDOS, audit, anonymisation, RGPD

## Plugins
Ajoutez des modules services à la personne via API/CLI (voir `/plugins`)

## Tests
Tests unitaires, intégration, e2e fournis dans `/tests/services_personne/`

## Déploiement
Compatible Docker, K8s, GitHub Actions, Codespaces, Linux.
