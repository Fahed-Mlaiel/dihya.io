# Module Preview pour projets IA, VR, AR

Ce module permet la génération de previews dynamiques (web, mobile, VR/AR) pour tout type de projet.

## Fonctionnalités principales
- Génération de previews dynamiques (web, mobile, VR/AR)
- Sécurité maximale (CORS, JWT, WAF, audit)
- Internationalisation dynamique (fr, en, ar, ...)
- API RESTful & GraphQL
- Multitenancy, gestion des rôles
- RGPD, audit, export
- Plugins extensibles

## Exemples d'utilisation
```js
import { PreviewManager } from './index.js';
const preview = new PreviewManager({ lang: 'de', role: 'user' });
preview.generate({ type: 'VR', project: 'Ultra2025' });
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
