# Module Sécurité pour projets IA, VR, AR

Ce module fournit une sécurité maximale pour toutes les routes et composants métiers (CORS, JWT, validation, audit, WAF, anti-DDOS, multitenancy, RGPD, plugins).

## Fonctionnalités principales
- Middleware CORS strict, whitelist dynamique
- Authentification JWT, gestion des rôles (admin, user, invité)
- Validation avancée (schémas, payload, anti-injection)
- Audit logging, traçabilité, anonymisation RGPD
- WAF intégré, détection d'anomalies, anti-DDOS
- Plugins de sécurité extensibles
- Internationalisation dynamique (fr, en, ar, ...)
- API RESTful & GraphQL
- Multitenancy, gestion des accès
- Export RGPD, logs structurés

## Exemples d'utilisation
```js
import { SecurityMiddleware } from './index.js';
app.use(SecurityMiddleware({ roles: ['admin', 'user'], lang: 'fr' }));
```

## Documentation
Voir `index.js` pour l'API complète et les exemples.

## Déploiement
Compatible Docker, K8s, GitHub Actions, Codespaces, Linux.

---
*English, العربية, ⴰⵣⵉⵖ, Deutsch, 中文, 日本語, 한국어, Nederlands, עִבְרִית, فارسی, हिन्दी, Español: See below for translations.*
