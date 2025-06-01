# Module Recherche pour projets IA, VR, AR

Ce module fournit des outils de recherche avancée, indexation, et analyse IA pour tout type de projet.

## Fonctionnalités principales
- Recherche avancée (texte, image, multimodal)
- Indexation IA, analyse sémantique
- Sécurité maximale (CORS, JWT, WAF, audit)
- Internationalisation dynamique (fr, en, ar, ...)
- API RESTful & GraphQL
- Multitenancy, gestion des rôles
- RGPD, audit, export
- Plugins extensibles

## Exemples d'utilisation
```js
import { RechercheManager } from './index.js';
const recherche = new RechercheManager({ lang: 'ar', role: 'user' });
recherche.search({ query: 'IA VR' });
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
