# Sécurité – API & Documentation

Ce module gère la sécurité (audit, rôles, logs, WAF, anti-DDOS, RGPD, etc.) pour projets IA, VR, AR, etc.

- API RESTful & GraphQL (multilingue, sécurisé, RGPD, plugins)
- Gestion des rôles (admin, user, invité)
- Intégration IA (analyse, détection, alertes)
- Audit, logs, anonymisation, export
- Extensible par plugins

## Endpoints
- `GET /securite/audit` : Logs d’audit
- `GET /securite/roles` : Liste des rôles sécurité

## Multilingue
Support : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es

## Sécurité
- JWT, CORS, WAF, anti-DDOS, audit, anonymisation, RGPD

## Plugins
Ajoutez des modules sécurité via API/CLI (voir `/plugins`)

## Tests
Tests unitaires, intégration, e2e fournis dans `/tests/securite/`

## Déploiement
Compatible Docker, K8s, GitHub Actions, Codespaces, Linux.
