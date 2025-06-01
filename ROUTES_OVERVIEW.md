# 🗺️ Dihya – Routes & Endpoints Overview Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Introduction](#introduction)
- [Principes de conception des routes](#principes-de-conception-des-routes)
- [Tableau des routes principales](#tableau-des-routes-principales)
- [Détails par stack](#détails-par-stack)
  - [Frontend](#frontend)
  - [Backend API](#backend-api)
  - [Mobile](#mobile)
  - [Plugins & extensions](#plugins--extensions)
- [Templates & exemples](#templates--exemples)
- [Multilingue](#multilingue)
- [Contact & support](#contact--support)

---

## Introduction

Ce document centralise la cartographie des routes, endpoints et APIs du projet **Dihya**.
Il garantit la cohérence, la sécurité, la souveraineté numérique, la conformité RGPD/NIS2, la compatibilité multi-stack (React, Flask, Node, Django, Flutter…), la portabilité (Linux, Codespaces, cloud souverain), l’accessibilité et le fallback IA open source.

---

## Principes de conception des routes

- **RESTful** : conventions HTTP, stateless, versionnement (`/api/v1/…`)
- **Sécurité** : RBAC, MFA, JWT, logs, rate limiting, CORS, auditabilité
- **Multilingue** : support natif fr, en, ar, tzm (paramètre `lang`)
- **Accessibilité** : messages d’erreur accessibles, codes HTTP explicites
- **Extensibilité** : endpoints plugins, hooks, webhooks, fallback IA open source
- **Souveraineté** : aucune dépendance critique à une API propriétaire

---

## Tableau des routes principales

| Route / Endpoint                | Méthode | Auth | Rôles      | Description (fr/en/ar/tzm)                | Stack      |
|---------------------------------|---------|------|------------|-------------------------------------------|------------|
| `/`                             | GET     | Non  | public     | Page d’accueil / Home page                | Frontend   |
| `/login`                        | POST    | Non  | public     | Authentification / Login                  | Frontend   |
| `/api/auth/login`               | POST    | Non  | public     | Authentification API                      | Backend    |
| `/api/auth/logout`              | POST    | Oui  | user+      | Déconnexion API                           | Backend    |
| `/api/rapport/metier/<id>`      | GET     | Oui  | user+      | Génération rapport métier                 | Backend    |
| `/api/ia/fallback`              | POST    | Oui  | user+      | Fallback IA open source                   | Backend    |
| `/api/plugins/<plugin>/run`     | POST    | Oui  | user+      | Exécution plugin                          | Backend    |
| `/api/templates/import`         | POST    | Oui  | admin+     | Import template métier                    | Backend    |
| `/api/templates/export`         | GET     | Oui  | admin+     | Export template métier                    | Backend    |
| `/api/monitoring/health`        | GET     | Non  | public     | Healthcheck API                           | Backend    |
| `/api/monitoring/metrics`       | GET     | Oui  | devops+    | Export Prometheus metrics                 | Backend    |
| `/mobile/home`                  | GET     | Oui  | user+      | Accueil mobile                            | Mobile     |
| `/mobile/notifications`         | GET     | Oui  | user+      | Notifications push                        | Mobile     |
| `/plugins/<plugin>/settings`    | GET/PUT | Oui  | admin+     | Gestion des plugins                       | Plugins    |
| `/docs`                         | GET     | Non  | public     | Documentation utilisateur                 | Frontend   |
| `/api/docs/openapi.yaml`        | GET     | Non  | public     | Spécification OpenAPI                     | Backend    |

---

## Détails par stack

### Frontend

- `/` : Page d’accueil, multilingue, accessibilité AA/AAA
- `/login` : Authentification, MFA, i18n
- `/dashboard` : Tableau de bord, accès selon rôle
- `/settings` : Préférences, i18n, accessibilité
- `/docs` : Documentation, guides, multilingue

### Backend API

- `/api/auth/login` : Authentification, JWT, logs, MFA
- `/api/auth/logout` : Déconnexion, logs
- `/api/rapport/metier/<id>` : Génération rapport métier, RBAC, logs
- `/api/ia/fallback` : Fallback IA open source, logs, RGPD
- `/api/plugins/<plugin>/run` : Exécution plugin, RBAC, audit
- `/api/templates/import/export` : Import/export templates métiers, RBAC, logs
- `/api/monitoring/health` : Healthcheck, monitoring
- `/api/monitoring/metrics` : Prometheus, logs, RBAC

### Mobile

- `/mobile/home` : Accueil mobile, i18n, accessibilité
- `/mobile/notifications` : Notifications push, logs, RGPD
- `/mobile/settings` : Préférences, i18n

### Plugins & extensions

- `/plugins/<plugin>/settings` : Gestion plugins, RBAC, logs
- `/api/plugins/<plugin>/run` : Exécution, logs, audit

---

## Templates & exemples

### Template de documentation de route

```
- Route / Endpoint :
- Méthode :
- Authentification : Oui / Non
- Rôles requis :
- Description :
- Stack concernée :
- Paramètres :
- Exemple d’appel :
- Codes retour :
- Traductions :
    - fr :
    - en :
    - ar :
    - tzm :
```

### Exemple rempli

```
- Route / Endpoint : /api/rapport/metier/1
- Méthode : GET
- Authentification : Oui
- Rôles requis : user, admin
- Description : Génère un rapport métier pour l’ID donné
- Stack concernée : Backend
- Paramètres : id (int), lang (fr/en/ar/tzm)
- Exemple d’appel : curl -H "Authorization: Bearer <token>" "https://dihya.eu/api/rapport/metier/1?lang=fr"
- Codes retour : 200 (OK), 401 (Non authentifié), 403 (Accès refusé), 404 (Non trouvé)
- Traductions :
    - fr : Génère un rapport métier pour l’ID donné
    - en : Generate a business report for the given ID
    - ar : إنشاء تقرير مهني للمعرف المحدد
    - tzm : Snes rapport n umetti s ID i d-yettunefken
```

---

## Multilingue

- **Français** : Ce document est disponible en français.
- **English** : This document is available in English.
- **العربية** : هذا المستند متوفر باللغة العربية.
- **ⴰⵣⵉⵖⴻⵏⵜ** : Asnif n tamedyazt-agi d-ittwasnen s tmazight.

*(Voir `/docs/i18n/` pour les versions traduites)*

---

## Contact & support

- **Slack** : #dihya-routes
- **Email** : routes@dihya.eu
- **GitHub Issues** : [Lien](https://github.com/votre-org/dihya/issues)

---

> **Ce document est validé pour la production. Toute modification doit être soumise via PR et validée par le Doc Lead et le Tech Lead.**

# Vue d’ensemble des routes Dihya

- Liste des routes principales (API, frontend, mobile)
- Méthodes, accès, sécurité, versioning
- Exemples de routes critiques, documentation associée

Voir [ARCHITECTURE.md](ARCHITECTURE.md), [API_REFERENCE_FR.md](docs/API_REFERENCE_FR.md)
