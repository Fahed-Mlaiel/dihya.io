# Module Publicité pour projets IA, VR, AR

Ce module gère la création, diffusion et analyse de campagnes publicitaires multi-canaux, avec IA et sécurité avancée.

## Fonctionnalités principales
- Création et gestion de campagnes (web, mobile, VR/AR)
- Analyse IA, optimisation, reporting
- Sécurité maximale (CORS, JWT, WAF, audit)
- Internationalisation dynamique (fr, en, ar, ...)
- API RESTful & GraphQL
- Multitenancy, gestion des rôles
- RGPD, audit, export
- Plugins extensibles

## Exemples d'utilisation
```js
import { PubliciteManager } from './index.js';
const pub = new PubliciteManager({ lang: 'es', role: 'admin' });
pub.createCampaign({ name: 'Ultra2025', channel: 'VR' });
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
