# 📋 Dihya – Product Backlog Ultra Avancé (Multi-stack, Multilingue, Souveraineté)

---

## Table des matières

- [Introduction](#introduction)
- [Vision produit](#vision-produit)
- [Backlog global](#backlog-global)
- [User stories détaillées](#user-stories-détaillées)
- [Épic & features](#épic--features)
- [Priorisation & roadmap](#priorisation--roadmap)
- [Templates & exemples](#templates--exemples)
- [Multilingue](#multilingue)
- [Contact & support](#contact--support)

---

## Introduction

Ce backlog centralise toutes les user stories, épics, features, tâches techniques et fonctionnelles du projet **Dihya**.
Il garantit la traçabilité, la souveraineté numérique, la conformité RGPD, l’accessibilité, la sécurité, la compatibilité multi-stack (React, Flask, Node, Django, Flutter…), la modularité, l’extensibilité, et la portabilité (Linux, Codespaces, cloud souverain, fallback open source).

---

## Vision produit

- **Souveraineté numérique** : aucune dépendance non maîtrisée, fallback open source, hébergement souverain.
- **Multilingue** : support natif fr, en, ar, tzm sur toutes les interfaces et APIs.
- **Sécurité & conformité** : RGPD, NIS2, MFA, RBAC, logs, accessibilité AA/AAA.
- **Performance & accessibilité** : UX/UI rapide, inclusive, accessible, SEO-ready.
- **Extensibilité** : plugins, modules, API, CI/CD, monitoring, tests automatisés.

---

## Backlog global

| ID      | Épic/Feature                | Description courte                                 | Priorité | Statut   | Sprint | Métier/Owner      |
|---------|----------------------------|----------------------------------------------------|----------|----------|--------|-------------------|
| EPIC-01 | Authentification MFA       | Connexion MFA, RBAC, logs, multilingue             | Haute    | En cours | S1     | Backend/Frontend  |
| EPIC-02 | Consentement RGPD          | Gestion consentement, logs, export, multilingue    | Haute    | À faire  | S1     | Backend/DPO       |
| EPIC-03 | Fallback IA open source    | Bascule IA locale si cloud KO, logs, multilingue   | Haute    | À faire  | S2     | Backend/IA        |
| EPIC-04 | Accessibilité AA/AAA       | Audit, correction, tests, reporting, multilingue   | Haute    | En cours | S1     | Frontend/QA       |
| EPIC-05 | Monitoring souverain       | Prometheus, Grafana, alertes, logs, multilingue    | Moyenne  | À faire  | S2     | DevOps            |
| EPIC-06 | Plugins & extensions       | Architecture, API, sécurité, fallback, multilingue | Moyenne  | À faire  | S3     | Backend/Frontend  |
| EPIC-07 | Mobile Flutter             | App mobile, i18n, accessibilité, fallback IA       | Moyenne  | À faire  | S3     | Mobile/Frontend   |
| EPIC-08 | Documentation multilingue  | Docs, guides, tests, accessibilité, SEO            | Haute    | En cours | S1     | PO/QA             |
| ...     | ...                        | ...                                                | ...      | ...      | ...    | ...               |

---

## User stories détaillées

### US-001 – Connexion MFA multilingue

- **En tant que** utilisateur
- **Je veux** me connecter avec MFA (TOTP/SMS), dans ma langue
- **Afin de** sécuriser mon accès, quel que soit mon contexte
- **Critères d’acceptation** :
  - MFA obligatoire, logs, RBAC, multilingue (fr, en, ar, tzm)
  - Message d’erreur accessible, pas de fuite info
  - Tests unitaires, intégration, e2e, manuels

### US-002 – Consentement RGPD

- **En tant que** utilisateur
- **Je veux** donner, retirer ou exporter mon consentement RGPD
- **Afin de** contrôler mes données, dans ma langue
- **Critères d’acceptation** :
  - Consentement journalisé, exportable, multilingue
  - UI/UX accessible, logs anonymisés
  - Tests automatisés et manuels

### US-003 – Fallback IA open source

- **En tant que** utilisateur
- **Je veux** que l’IA bascule automatiquement sur un modèle open source si le cloud est KO
- **Afin de** garantir la continuité de service et la souveraineté
- **Critères d’acceptation** :
  - Bascule < 200 ms, logs, multilingue
  - Tests de charge, fallback, conformité RGPD

### US-004 – Audit accessibilité

- **En tant que** QA/PO
- **Je veux** auditer l’accessibilité de toutes les interfaces et APIs
- **Afin de** garantir la conformité RGAA/WCAG et l’inclusion
- **Critères d’acceptation** :
  - Score AA/AAA, rapport multilingue, logs
  - Tests axe-core, pa11y, manuels

---

## Épic & features

- **EPIC-01** : Authentification MFA, RBAC, logs, multilingue
  - US-001, US-010, US-011
- **EPIC-02** : Consentement RGPD, export, logs, multilingue
  - US-002, US-012
- **EPIC-03** : Fallback IA open source, logs, multilingue
  - US-003, US-013
- **EPIC-04** : Accessibilité AA/AAA, audit, reporting, multilingue
  - US-004, US-014
- ...

---

## Priorisation & roadmap

| Sprint | Début      | Fin        | Features clés                         | Statut   |
|--------|------------|----------- |---------------------------------------|----------|
| S1     | 2025-05-20 | 2025-06-10 | MFA, RGPD, accessibilité, docs        | En cours |
| S2     | 2025-06-11 | 2025-07-01 | Fallback IA, monitoring, plugins      | À venir  |
| S3     | 2025-07-02 | 2025-07-22 | Mobile, extensions, optimisations     | À venir  |

---

## Templates & exemples

### Template user story

```
- ID : US-XXX
- Épic : EPIC-XX
- Titre :
- Description :
- Critères d’acceptation :
- Priorité : Haute / Moyenne / Basse
- Statut : À faire / En cours / Terminé
- Sprint :
- Métier/Owner :
- Preuve : [capture/log/test]
- Commentaire :
```

### Exemple rempli

```
- ID : US-001
- Épic : EPIC-01
- Titre : Connexion MFA multilingue
- Description : Authentification MFA, RBAC, logs, UI multilingue
- Critères d’acceptation : MFA obligatoire, logs, multilingue, accessibilité
- Priorité : Haute
- Statut : En cours
- Sprint : S1
- Métier/Owner : Backend/Frontend
- Preuve : /tests/manual/proofs/US-001_fr.png
- Commentaire : RAS
```

---

## Multilingue

- **Français** : Ce backlog est disponible en français.
- **English** : This backlog is available in English.
- **العربية** : هذا السجل متوفر باللغة العربية.
- **ⴰⵣⵉⵖⴻⵏⵜ** : Asnif n tamedyazt-agi d-ittwasnen s tmazight.

*(Voir `/docs/i18n/` pour les versions traduites)*

---

## Contact & support

- **Slack** : #dihya-backlog
- **Email** : backlog@dihya.eu
- **GitHub Issues** : [Lien](https://github.com/your-org/dihya/issues)

---

> **Ce backlog est validé pour la production. Toute modification doit être soumise via PR et validée par le PO et le Doc Lead.**

# Product Backlog Dihya

- Liste priorisée des fonctionnalités, modules, plugins, templates
- User stories, critères d’acceptation, dépendances
- Liens vers la roadmap, les issues, les PR

Voir [ROADMAP.md](ROADMAP.md), [CONTRIBUTING.md](CONTRIBUTING.md)
