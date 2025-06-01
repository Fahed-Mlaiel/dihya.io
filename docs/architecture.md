# Architecture – Dihya

- Description détaillée de l’architecture globale, modules, flux, sécurité, i18n, accessibilité, extensibilité
- Diagrammes, exemples, bonnes pratiques

Voir [ARCHITECTURE.md](../../ARCHITECTURE.md), [ARCHITECTURE_DIAGRAM.png](ARCHITECTURE_DIAGRAM.png)

Ce document décrit l’architecture technique de la plateforme Dihya Coding, conforme au cahier des charges : sécurité, modularité, multistack, extensibilité, bonnes pratiques DevOps et multilingue.

---

## Vue d’ensemble

- **Architecture modulaire** : chaque stack (Flask, Node.js, blockchain, frontend, mobile) est isolée et extensible.
- **API RESTful** : backend Flask (Python) et Node.js (Express) exposent des APIs sécurisées.
- **Frontend** : React (web), Flutter/React Native (mobile).
- **Blockchain** : smart contracts EVM (Solidity), scripts de déploiement.
- **DevOps** : Docker, Kubernetes, Terraform, CI/CD.
- **Internationalisation** : multilingue, prise en charge des dialectes.

---

## Schéma global

```
+-------------------+       +-------------------+       +-------------------+
|    Frontend Web   | <---> |     API Gateway   | <---> |   Backend Flask   |
|   (React, Nginx)  |       |   (optionnel)     |       |   (Python, JWT)   |
+-------------------+       +-------------------+       +-------------------+
        |                           |                           |
        |                           |                           |
        v                           v                           v
+-------------------+       +-------------------+       +-------------------+
|  Backend Node.js  | <---> |   Blockchain      | <---> |   Mobile Apps     |
|   (Express, JWT)  |       | (Smart Contracts) |       | (Flutter/ReactN)  |
+-------------------+       +-------------------+       +-------------------+
```

---

## Backend

### Flask (Python)

- **Organisation** : `app/` (routes, models, services, utils), `config/`, `tests/`
- **Sécurité** : JWT, CORS, headers, validation stricte, rate limiting
- **Internationalisation** : Flask-Babel, multilingue/dialectes
- **Tests** : Unittest/Pytest, couverture obligatoire
- **Extensible** : blueprints, services, schémas

### Node.js (Express)

- **Organisation** : `src/` (routes, controllers, middleware, models), `tests/`
- **Sécurité** : JWT, Helmet, CORS, validation, rate limiting
- **Internationalisation** : i18n, multilingue
- **Extensible** : routes, services, middlewares

---

## Frontend

- **React** : SPA, communication API REST, gestion multilingue, SEO (robots.txt, sitemap.xml)
- **Mobile** : Flutter (Dart), React Native (JS), structure modulaire, assets partagés

---

## Blockchain

- **Smart contracts** : Solidity (EVM), modularité, sécurité OpenZeppelin, tests et scripts de déploiement
- **Interopérabilité** : scripts JS (ethers.js) pour déploiement/migration

---

## DevOps

- **Docker** : images séparées backend/frontend, utilisateurs non-root, build multi-étapes
- **Kubernetes** : déploiement scalable, probes, ressources limitées, services, Ingress prêt
- **Terraform** : infrastructure as code, cloud-agnostique, variables sécurisées
- **CI/CD** : GitHub Actions (build, test, lint, déploiement auto)

---

## Sécurité

- JWT pour toutes les APIs sensibles
- Headers HTTP de sécurité (CORS, XSS, HSTS, etc.)
- Validation stricte des entrées (backend et frontend)
- Rate limiting sur toutes les APIs publiques
- Secrets et variables d’environnement hors code source
- Tests de sécurité automatisés (lint, audit, tests unitaires)

---

## Internationalisation

- Prise en charge multilingue (fr, en, ar, ber, tzm, etc.)
- Détection automatique de la langue côté backend et frontend
- Fichiers de traduction organisés dans `/Dihya/i18n/`

---

## Extensibilité

- Ajout facile de nouvelles stacks (ex : Go, Rust, etc.)
- Ajout de modules/plugins via blueprints (Flask) ou routes/controllers (Node)
- Smart contracts extensibles pour plugins, tokens, NFT, etc.

---

## Bonnes pratiques

- Code commenté, typé, documenté
- Tests unitaires pour chaque module critique
- CI/CD obligatoire avant merge en production
- Respect des licences open-source (AGPL)
- Documentation à jour dans `/docs/`

---

## Pour aller plus loin

- Voir la documentation API dans `docs/api.md`
- Voir les guides développeur et utilisateur dans `docs/dev_guide.md` et `docs/user_guide.md`
- Pour toute contribution, lire le fichier `CONTRIBUTING.md` (à créer)

---
