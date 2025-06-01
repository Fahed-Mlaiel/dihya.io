# Transport – API & Documentation

Ce module gère le transport (trajets, réservations, IA, VR, AR, etc.) pour projets IA, VR, AR, etc.

- API RESTful & GraphQL (multilingue, sécurisé, RGPD, plugins)
- Gestion des rôles (admin, user, invité)
- Intégration IA (suggestion, analyse, réservation)
- Audit, logs, anonymisation, export
- Extensible par plugins

## Endpoints
- `GET /transport/trajets` : Liste des trajets
- `POST /transport/reservation` : Réserver un trajet

## Multilingue
Support : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es

## Sécurité
- JWT, CORS, WAF, anti-DDOS, audit, anonymisation, RGPD

## Plugins
Ajoutez des modules transport via API/CLI (voir `/plugins`)

## Tests
Tests unitaires, intégration, e2e fournis dans `/tests/transport/`

## Déploiement
Compatible Docker, K8s, GitHub Actions, Codespaces, Linux.
