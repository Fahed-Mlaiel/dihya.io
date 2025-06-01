# Template e-commerce Dihya

Ce template fournit une structure avancée pour la gestion de projets e-commerce (Node.js, REST, GraphQL, sécurité, i18n, plugins, RGPD, SEO, tests, déploiement).

## Fonctionnalités principales
- Sécurité maximale (CORS, JWT, validation, audit, WAF, anti-DDOS)
- Internationalisation dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
- Modèle RESTful + support GraphQL
- Multitenancy, gestion des rôles (admin, user, invité)
- Intégration IA (LLaMA, Mixtral, Mistral)
- SEO backend (robots, sitemap, logs structurés)
- Système de plugins extensible
- Conformité RGPD, auditabilité
- Tests complets (unit, integration, e2e)
- Déploiement GitHub Actions, Docker, K8s

## Utilisation
1. Copier le dossier dans votre projet Node.js
2. Adapter les routes, contrôleurs, policies selon vos besoins
3. Lancer les tests : `npm test`
4. Déployer via Docker/K8s/GitHub Actions

## Multilingue
- Tous les messages sont internationalisés (voir `i18n/`)

## Exemples de routes
- `GET /ecommerce/products` : liste produits
- `POST /ecommerce/orders` : création commande

## Sécurité
- JWT, CORS, validation, audit, WAF, anti-DDOS intégrés

## RGPD
- Export, anonymisation, logs, audit

## Plugins
- Ajout dynamique via API ou CLI

## Tests
- Couverture maximale, mocks, fixtures, e2e

## Déploiement
- Compatible Linux, Codespaces, CI/CD

