# Social – API & Documentation

Ce module gère le social (réseaux, entraide, IA, VR, AR, etc.) pour projets IA, VR, AR, etc.

- API RESTful & GraphQL (multilingue, sécurisé, RGPD, plugins)
- Gestion des rôles (admin, user, invité)
- Intégration IA (analyse, suggestion, modération)
- Audit, logs, anonymisation, export
- Extensible par plugins

## Endpoints
- `GET /social/activites` : Liste des activités sociales
- `POST /social/message` : Envoyer un message

## Multilingue
Support : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es

## Sécurité
- JWT, CORS, WAF, anti-DDOS, audit, anonymisation, RGPD

## Plugins
Ajoutez des modules social via API/CLI (voir `/plugins`)

## Tests
Tests unitaires, intégration, e2e fournis dans `/tests/social/`

## Déploiement
Compatible Docker, K8s, GitHub Actions, Codespaces, Linux.
