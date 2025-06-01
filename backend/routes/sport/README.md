# Sport – API & Documentation

Ce module gère le sport (activités, réservations, IA, VR, AR, etc.) pour projets IA, VR, AR, etc.

- API RESTful & GraphQL (multilingue, sécurisé, RGPD, plugins)
- Gestion des rôles (admin, user, invité)
- Intégration IA (suggestion, analyse, réservation)
- Audit, logs, anonymisation, export
- Extensible par plugins

## Endpoints
- `GET /sport/activites` : Liste des activités sportives
- `POST /sport/reservation` : Réserver une activité

## Multilingue
Support : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es

## Sécurité
- JWT, CORS, WAF, anti-DDOS, audit, anonymisation, RGPD

## Plugins
Ajoutez des modules sport via API/CLI (voir `/plugins`)

## Tests
Tests unitaires, intégration, e2e fournis dans `/tests/sport/`

## Déploiement
Compatible Docker, K8s, GitHub Actions, Codespaces, Linux.
