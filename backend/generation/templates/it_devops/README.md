# IT/DevOps Template

## Description
Template avancé pour la génération de projets IT/DevOps (web, scripts, CI/CD, monitoring) avec sécurité, i18n, RGPD, plugins, multitenancy.

## Fonctionnalités
- Routes RESTful/GraphQL pour pipelines, jobs, utilisateurs, logs.
- Sécurité maximale (CORS, JWT, audit, WAF, anti-DDOS).
- Internationalisation dynamique.
- Gestion des rôles et multitenancy.
- Intégration IA (fallback open source).
- SEO backend, logs structurés.
- Plugins extensibles.
- RGPD.

## Utilisation
```js
const itDevops = require('./template');
itDevops.generateProject({ lang: 'fr', tenant: 'opsTeam', role: 'admin' });
```

## Personnalisation
- Adapter `policy.md` pour les règles métier.
- Étendre `template.js` pour de nouveaux modules.

## Tests
Lancer `test_it_devops.js`.

## Licence
MIT
