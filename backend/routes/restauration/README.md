# Restauration – API & Documentation

Ce module gère la restauration (cantines, menus, commandes, allergies, etc.) pour projets IA, VR, AR, etc.

- API RESTful & GraphQL (multilingue, sécurisé, RGPD, plugins)
- Gestion des rôles (admin, user, invité)
- Intégration IA (suggestion menus, analyse allergies)
- Audit, logs, anonymisation, export
- Extensible par plugins

## Endpoints
- `GET /restauration/menus` : Liste des menus
- `POST /restauration/commande` : Passer une commande

## Multilingue
Support : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es

## Sécurité
- JWT, CORS, WAF, anti-DDOS, audit, anonymisation, RGPD

## Plugins
Ajoutez des modules restauration via API/CLI (voir `/plugins`)

## Tests
Tests unitaires, intégration, e2e fournis dans `/tests/restauration/`

## Déploiement
Compatible Docker, K8s, GitHub Actions, Codespaces, Linux.
