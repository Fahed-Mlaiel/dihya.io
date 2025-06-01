# 🧑‍💼 Dihya – Guide des Métiers, Rôles & Accès (Ultra avancé, multilingue, souveraineté)

---

## Table des matières

- [Introduction](#introduction)
- [Principes de gestion des rôles](#principes-de-gestion-des-rôles)
- [Liste des métiers & rôles](#liste-des-métiers--rôles)
- [Gestion des accès (RBAC)](#gestion-des-accès-rbac)
- [Exemples d’intégration](#exemples-dintégration)
- [Templates & modèles](#templates--modèles)
- [Multilingue](#multilingue)
- [Contact & support](#contact--support)

---

## Introduction

Ce guide décrit la gestion avancée des métiers, rôles et accès du projet **Dihya**.
Il garantit la traçabilité, la sécurité, la conformité RGPD, la souveraineté numérique, l’accessibilité, et la compatibilité multi-stack (React, Flask, Node, Django, Flutter…).

---

## Principes de gestion des rôles

- **RBAC** (Role-Based Access Control) sur tous les modules sensibles.
- **Séparation des droits** : chaque métier a des accès limités à ses besoins.
- **Traçabilité** : chaque action critique est journalisée.
- **Multilingue** : chaque rôle/documentation est disponible en fr, en, ar, tzm.
- **Auditabilité** : chaque attribution/modification de rôle est tracée.
- **Souveraineté** : gestion des rôles sans dépendance cloud externe.

---

## Liste des métiers & rôles

| Métier                  | Rôle système           | Accès principaux                        | Docs associées                   |
|-------------------------|------------------------|-----------------------------------------|----------------------------------|
| DevOps                  | devops                 | CI/CD, sécurité, monitoring, rollback   | [devops.md](docs/metiers/devops.md) |
| Développeur Frontend    | frontend               | UI, accessibilité, i18n, tests          | [frontend.md](docs/metiers/frontend.md) |
| Développeur Backend     | backend                | API, sécurité, RGPD, fallback IA        | [backend.md](docs/metiers/backend.md) |
| Data Privacy Officer    | dpo                    | RGPD, DPIA, notification CNIL, audit    | [dpo.md](docs/metiers/dpo.md)    |
| QA/Accessibility Lead   | qa                     | Tests, accessibilité, audit, conformité | [qa.md](docs/metiers/qa.md)      |
| Product Owner           | po                     | Documentation, conformité, roadmap      | [po.md](docs/metiers/po.md)      |
| Utilisateur             | user                   | Accès restreint, usage applicatif       | -                                |
| ...                     | ...                    | ...                                     | ...                              |

---

## Gestion des accès (RBAC)

- **Définition des rôles** : chaque rôle est défini dans la config (ex : `roles.yaml`, DB, IAM).
- **Attribution** : chaque utilisateur se voit attribuer un ou plusieurs rôles selon son métier.
- **Exemple de mapping** :

```yaml
# Exemple roles.yaml
roles:
  devops:
    permissions: [deploy, monitor, rollback, manage-secrets]
  frontend:
    permissions: [ui:edit, i18n:manage, a11y:test]
  backend:
    permissions: [api:edit, rgpd:manage, ai:fallback]
  dpo:
    permissions: [rgpd:audit, dpi:manage, notify:cnil]
  qa:
    permissions: [test:run, a11y:audit, report:issue]
  po:
    permissions: [doc:edit, roadmap:manage, consent:manage]
  user:
    permissions: [app:use]
```

- **Gestion dynamique** : modification des rôles via interface admin sécurisée, journalisation de chaque changement.
- **Sécurité** : MFA obligatoire pour tout accès admin, logs d’accès, audit régulier.

---

## Exemples d’intégration

### Exemple 1 : Attribution d’un rôle à un nouvel utilisateur

- L’utilisateur s’inscrit, le PO valide le métier, le rôle est attribué via l’interface admin.
- Toute modification est tracée (qui, quand, quoi).

### Exemple 2 : Accès à une ressource protégée

- Un utilisateur avec le rôle `backend` tente d’accéder à une API sensible.
- Le middleware RBAC vérifie la permission `api:edit`.
- Accès accordé ou refusé, action loggée.

---

## Templates & modèles

### Modèle d’attribution de rôle (Markdown)

```
- Utilisateur : [ex. alice@dihya.eu]
- Métier : [ex. DevOps]
- Rôle attribué : [ex. devops]
- Permissions : [deploy, monitor, rollback]
- Date d’attribution :
- Attribué par :
- Preuve : [capture/log]
- Commentaire :
```

### Exemple rempli

```
- Utilisateur : alice@dihya.eu
- Métier : DevOps
- Rôle attribué : devops
- Permissions : deploy, monitor, rollback
- Date d’attribution : 2025-05-20
- Attribué par : @admin
- Preuve : /logs/roles/2025-05-20_alice.log
- Commentaire : MFA activé, accès validé
```

---

## Multilingue

- **Français** : Ce guide est disponible en français.
- **English** : This guide is available in English.
- **العربية** : هذا الدليل متوفر باللغة العربية.
- **ⴰⵣⵉⵖⴻⵏⵜ** : Asnif n tamedyazt-agi d-ittwasnen s tmazight.

*(Voir `/docs/i18n/` pour les versions traduites)*

---

## Contact & support

- **Slack** : #dihya-roles
- **Email** : roles@dihya.eu
- **GitHub Issues** : [Lien](https://github.com/your-org/dihya/issues)

---

> **Ce guide est validé pour la production. Toute modification doit être soumise via PR et validée par le Doc Lead et le RSSI.**

# Guide des métiers et rôles Dihya

- Définition des métiers, rôles, permissions, héritage
- Exemples de configuration (backend, frontend, cloud)
- Sécurité, audit, reporting, tests
- Contribution, extension, personnalisation

Voir [METIERS_OVERVIEW.md](METIERS_OVERVIEW.md), [ROLES_PERMISSIONS.md](ROLES_PERMISSIONS.md)
