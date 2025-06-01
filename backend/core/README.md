# 🧩 Dihya – Backend Core Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Rôle du dossier `backend/core`](#rôle-du-dossier-backendcore)
- [Fonctions principales](#fonctions-principales)
- [Structure recommandée](#structure-recommandée)
- [Sécurité & conformité](#sécurité--conformité)
- [Exemples de routes critiques](#exemples-de-routes-critiques)
- [Bonnes pratiques](#bonnes-pratiques)
- [Multilingue](#multilingue)
- [Documentation associée](#documentation-associée)
- [Documentation interactive](#documentation-interactive)
- [Intégration Node.js/Express](#intégration-nodejsexpress)

---

## 🧩 Rôle du dossier `backend/core`

Ce dossier contient le cœur logique du backend de la plateforme **Dihya Coding** : gestion des modules critiques, logique métier centrale, orchestrateur de génération, sécurité, extensibilité et robustesse.

- **Multi-stack** : Node.js, Python (Flask), plugins, CI/CD, Codespaces, cloud souverain
- **Souveraineté** : aucun code propriétaire, tout est open source, versionné, auditable
- **Sécurité** : gestion centralisée des rôles, logs, RBAC, conformité RGPD/NIS2, auditabilité
- **Accessibilité** : documentation multilingue (fr, en, ar, tzm), structure claire, API REST/GraphQL

---

## 🧠 Fonctions principales

- **Initialisation de l’application backend** (Express/Flask, configuration, extensions)
- **Gestion des modules critiques** : authentification, rôles, permissions, sécurité, sessions
- **Orchestration de la génération automatique** (frontend, backend, mobile, devops, blockchain)
- **Gestion des routes principales** (API REST/GraphQL, endpoints métiers, preview, marketplace)
- **Chargement dynamique des plugins et templates métiers**
- **Gestion des erreurs, logs, audit et conformité**
- **Extensibilité** : intégration facile de nouveaux modules, métiers, IA, plugins

---

## 📁 Structure recommandée

```
core/
├── app.py         # Initialisation Flask, extensions, blueprints (si Python)
├── index.js       # Entrypoint Node.js (services, middlewares, i18n, RBAC)
├── logic.py       # Logique métier centrale, orchestrateur de génération
├── security.py    # Sécurité, authentification, rôles, permissions
├── plugins.py     # Chargement dynamique des plugins/templates métiers
├── routes.py      # Déclaration des routes principales API
├── errors.py      # Gestion centralisée des erreurs et exceptions
├── utils.py       # Fonctions utilitaires partagées
├── configs/       # Fichiers de configuration du noyau (JSON, YAML)
├── tests/         # Tests unitaires et d’intégration du noyau
└── README.md      # Ce fichier (documentation multilingue)
```

---

## 🔒 Sécurité & conformité

- **Séparation stricte** des responsabilités (auth, logique métier, plugins)
- **Validation forte** des entrées/sorties (schemas, types, permissions)
- **Logs horodatés** pour chaque action critique (auditabilité, RGPD)
- **Gestion centralisée des erreurs** pour éviter les fuites d’information
- **Extensibilité** sans compromettre la sécurité (plugins sandboxés, vérification de signature)
- **RBAC** : gestion des rôles (admin, ai_user, auditor, user, guest) sur chaque endpoint
- **CI/CD-ready** : tous les scripts/tests sont compatibles GitHub Actions, Codespaces, cloud souverain

---

## 🛠️ Exemples de routes critiques

| Route                        | Méthode | Description                                 | Sécurité           |
|------------------------------|---------|---------------------------------------------|--------------------|
| `/api/generate`              | POST    | Génération automatique de projet            | Auth/JWT, RBAC     |
| `/api/auth/login`            | POST    | Authentification utilisateur                | Public             |
| `/api/user/profile`          | GET     | Profil utilisateur                          | Auth/JWT, RBAC     |
| `/api/plugins`               | GET     | Liste/chargement des plugins                | Auth/JWT, RBAC     |
| `/api/templates`             | GET     | Liste des templates métiers                 | Public             |

*Note : "Auth/JWT" (JSON Web Token) et RBAC (Role-Based Access Control) assurent une authentification et une gestion des droits robustes.*

---

## 📝 Bonnes pratiques

- **Documenter chaque module** et chaque fonction critique (docstrings, commentaires, i18n)
- **Automatiser les tests** pour garantir la robustesse du noyau (unit, integration, e2e)
- **Limiter l’accès** aux fonctions sensibles aux rôles autorisés (RBAC)
- **Mettre à jour la documentation** à chaque évolution du noyau ou des routes
- **Exporter tous les logs et rapports** (CSV, JSON, badge conformité)
- **Traduire** tous les messages critiques (fr, en, ar, tzm)
- **Automatiser** l’exécution en CI/CD (GitHub Actions, Codespaces)
- **Séparer** scripts Python et Node.js pour compatibilité maximale

---

## 🌍 Multilingue

- **Français** : Ce dossier est documenté en français.
- **English** : This folder is documented in English.
- **العربية** : هذا المجلد موثق باللغة العربية.
- **ⴰⵣⵉⵖⴻⵏⵜ** : Afaylu agi yettwarnan s tmazight.

*(Voir `/docs/i18n/` pour les versions traduites)*

---

## 📚 Documentation associée

- [Architecture backend](../../docs/architecture.md)
- [Configuration backend](../config/README.md)
- [Sécurité & RGPD](../../SECURITY.md)
- [API principale](../../docs/openapi.yaml)
- [Décisions structurantes](../../decision_log.md)
- [Changelog technique](../../TECHNICAL_CHANGELOG.md)
- [Tests E2E](../../E2E_TESTS_GUIDE.md)
- [Webhooks](../../WEBHOOKS_GUIDE.md)

---

## 📚 Documentation interactive

- [OpenAPI/Swagger REST core](openapi_core.yaml)
- [OpenAPI/Swagger GraphQL core](openapi_graphql_core.yaml)
- [Exemples d’utilisation avancés (Flask, Express, plugins, CI/CD)](EXAMPLES_ADVANCED.md)
- [Exemples d’appels API/GraphQL multilingues](EXAMPLES_API_CORE.md)
- [Dashboard conformité/monitoring core](dashboard_core.md)
- [Dashboard global conformité/monitoring](../dashboard_global.md)

---

## 🚀 Intégration Node.js/Express

Voir `index.js` pour l’intégration middleware, RBAC, logs, i18n, plugins côté Node.js/Express.

---

**Dihya Coding** – Noyau robuste, souverain, extensible, multilingue, prêt pour la production, la démo et la contribution.

---
