# Assurance Template

Ce dossier contient le template métier pour la génération de projets d'assurance (web, mobile, IA, etc.) avec sécurité, multilingue, conformité RGPD, plugins, tests, et déploiement automatisé.

## Fonctionnalités principales
- Génération de projets assurance (REST, GraphQL, plugins)
- Sécurité maximale (CORS, JWT, audit, WAF, anti-DDOS)
- Multilingue (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es)
- RGPD, audit, anonymisation, export
- Extensible (API, CLI, plugins)
- Tests complets (unit, integration, e2e)
- Déploiement GitHub Actions, Docker, K8s

## Utilisation
```js
const { generateAssuranceProject } = require('./template');
// ...
```

## Exemples
- Génération d'un projet assurance santé multilingue
- Ajout d'un plugin conformité
- Export RGPD

## Documentation
Voir `policy.md` et `template.js` pour plus de détails.
