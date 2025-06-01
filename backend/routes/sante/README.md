# Santé – API & Documentation

Ce module gère la santé (dossiers, RDV, alertes, IA santé, etc.) pour projets IA, VR, AR, etc.

- API RESTful & GraphQL (multilingue, sécurisé, RGPD, plugins)
- Gestion des rôles (admin, user, invité)
- Intégration IA (diagnostic, alertes, analyse)
- Audit, logs, anonymisation, export
- Extensible par plugins

## Endpoints
- `GET /sante/dossiers` : Liste des dossiers santé
- `POST /sante/rdv` : Prendre un rendez-vous

## Multilingue
Support : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es

## Sécurité
- JWT, CORS, WAF, anti-DDOS, audit, anonymisation, RGPD

## Plugins
Ajoutez des modules santé via API/CLI (voir `/plugins`)

## Tests
Tests unitaires, intégration, e2e fournis dans `/tests/sante/`

## Déploiement
Compatible Docker, K8s, GitHub Actions, Codespaces, Linux.
