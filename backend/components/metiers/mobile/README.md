# Gestion mobile pour projets IA, VR, AR

Ce module fournit des composants pour l'intégration mobile avancée (iOS, Android, PWA) dans des projets multi-métiers.

## Fonctionnalités principales
- API RESTful & GraphQL
- Authentification sécurisée (JWT, OAuth2, CORS, WAF)
- Internationalisation dynamique (fr, en, ar, ...)
- Intégration IA (génération, analyse, fallback open source)
- Multitenancy, gestion des rôles
- RGPD, audit, export
- Plugins extensibles

## Exemples d'utilisation
```js
import { MobileManager } from './index.js';
const mobile = new MobileManager({ lang: 'en', role: 'user' });
mobile.deployApp({ type: 'PWA', project: 'AR2025' });
```

## Documentation
Voir `index.js` pour l'API complète et les exemples.

## Sécurité
- CORS strict
- JWT obligatoire
- Validation et audit
- WAF intégré

## Déploiement
Compatible Docker, K8s, GitHub Actions, Codespaces, Linux.

---
*English, العربية, ⴰⵣⵉⵖ, Deutsch, 中文, 日本語, 한국어, Nederlands, עִבְרִית, فارسی, हिन्दी, Español: See below for translations.*
