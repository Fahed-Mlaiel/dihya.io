# README – Module Administration Publique (Dihya)

## Présentation
Module ultra avancé pour la gestion des services publics, conforme RGPD, sécurité, accessibilité, plugins, audit, i18n, SEO, souveraineté numérique.

## Fonctionnalités
- Sécurité : RBAC, JWT, audit log, plugins vérifiés
- RGPD : consentement, droit à l’oubli, portabilité, anonymisation
- Accessibilité : WCAG 2.2 AA+, ARIA, navigation clavier
- Plugins : extensible, audit, sécurité, RGPD
- i18n : multilingue (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- SEO : balises, logs, JSON-LD, audit
- Souveraineté numérique : fallback open source, logs locaux
- Tests : couverture > 95%, accessibilité, RGPD, plugins, CI/CD

## Utilisation
```js
import { AdministrationPublique } from './index';
const admin = new AdministrationPublique({ lang: 'fr', plugins: [] });
admin.manageService({ service: 'urbanisme', user: { id: 1 } });
```

## API
- `manageService(data)` : gestion sécurisée, auditée, multilingue
- `static api()` : endpoints REST/GraphQL sécurisés

## Guides
- [RGPD](./RGPD_GUIDE_ADMINISTRATION.md)
- [Sécurité](./SECURITY_GUIDE_ADMINISTRATION.md)
- [Accessibilité](./ACCESSIBILITY_GUIDE_ADMINISTRATION.md)
- [Plugins](./PLUGINS_GUIDE_ADMINISTRATION.md)
- [Tests](./TEST_STRATEGY_ADMINISTRATION.md)
- [Policy](./policy.md)

## Tests
- `index.test.js` (Jest/RTL)

## Badges
- ![Couverture > 95%](https://img.shields.io/badge/coverage-95%25-brightgreen)
- ![RGPD](https://img.shields.io/badge/RGPD-ok-blue)
- ![Accessibilité](https://img.shields.io/badge/a11y-AA%2B-blueviolet)
- ![Sécurité](https://img.shields.io/badge/security-ultra--secure-green)
- ![CI/CD](https://img.shields.io/badge/ci%2Fcd-passing-success)

---
© 2025 Dihya Coding – Souveraineté numérique, conformité totale, production ready.
