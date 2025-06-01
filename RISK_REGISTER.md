# ⚠️ Dihya – Risk Register Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Introduction](#introduction)
- [Principes de gestion des risques](#principes-de-gestion-des-risques)
- [Registre des risques](#registre-des-risques)
- [Templates & exemples](#templates--exemples)
- [Multilingue](#multilingue)
- [Contact & support](#contact--support)

---

## Introduction

Ce registre centralise tous les risques identifiés pour le projet **Dihya** (techniques, métiers, sécurité, souveraineté, RGPD, accessibilité, IA, DevOps, plugins, mobile, etc.).
Il garantit la traçabilité, la souveraineté numérique, la conformité RGPD/NIS2, la sécurité, la compatibilité multi-stack (React, Flask, Node, Django, Flutter…), la portabilité (Linux, Codespaces, cloud souverain), l’accessibilité et le fallback IA open source.

---

## Principes de gestion des risques

- **Identification proactive** : chaque risque est détecté, documenté, évalué.
- **Multilingue** : chaque risque est décrit en fr, en, ar, tzm.
- **Souveraineté** : priorité aux solutions open source, cloud souverain, fallback local.
- **Conformité** : RGPD, NIS2, accessibilité, sécurité, auditabilité.
- **Transparence** : chaque risque est consultable par tous les métiers.
- **Mise à jour continue** : revue à chaque sprint/release.

---

## Registre des risques

# Registre des risques Dihya

- Identification, évaluation, mitigation des risques (sécurité, technique, produit)
- Suivi, reporting, alertes
- Liens vers les incidents, décisions, roadmap

Voir [INCIDENTS.md](INCIDENTS.md), [PRODUCT_DECISIONS.md](PRODUCT_DECISIONS.md)

| ID        | Date       | Catégorie      | Description (fr/en/ar/tzm)                | Impact | Probabilité | Criticité | Mesures de mitigation         | Statut   | Responsable | Preuve / Lien                | Commentaire |
|-----------|------------|----------------|-------------------------------------------|--------|-------------|-----------|-------------------------------|----------|-------------|------------------------------|-------------|
| RISK-2025-01 | 2025-05-20 | Sécurité       | Fuite de secrets dans les logs (fr/en/ar/tzm) | Élevé  | Moyenne     | Critique  | Audit logs, rotation secrets, RBAC | Ouvert   | DevOps      | /logs/audit/2025-05-20.log   | MFA activé  |
| RISK-2025-02 | 2025-05-20 | Souveraineté   | Dépendance à une API propriétaire (fr/en/ar/tzm) | Élevé  | Faible      | Majeur    | Fallback IA open source, monitoring | Ouvert   | Backend     | /docs/ai/FALLBACK_POLICY.md  | Testé OK    |
| RISK-2025-03 | 2025-05-20 | RGPD           | Consentement non journalisé (fr/en/ar/tzm) | Moyen  | Moyenne     | Majeur    | Logs anonymisés, export consentement | Fermé    | DPO         | /docs/rgpd/CONSENT.md        | Conforme    |
| RISK-2025-04 | 2025-05-20 | Accessibilité  | Non conformité RGAA/WCAG (fr/en/ar/tzm)   | Moyen  | Moyenne     | Majeur    | Audit axe-core, pa11y, correctifs    | Ouvert   | QA          | /reports/accessibility.html  | En cours    |
| RISK-2025-05 | 2025-05-20 | DevOps         | Rollback non testé (fr/en/ar/tzm)         | Élevé  | Faible      | Critique  | Procédure rollback, test CI/CD       | Ouvert   | DevOps      | /docs/restore/ROLLBACK.md    | À planifier |
| ...       | ...        | ...            | ...                                       | ...    | ...         | ...       | ...                               | ...      | ...         | ...                          | ...         |

---

## Templates & exemples

### Template de risque

```
- ID :
- Date :
- Catégorie :
- Description :
- Impact : Faible / Moyen / Élevé
- Probabilité : Faible / Moyenne / Élevée
- Criticité : Mineur / Majeur / Critique
- Mesures de mitigation :
- Statut : Ouvert / Fermé / En cours
- Responsable :
- Preuve / Lien :
- Commentaire :
- Traductions :
    - en :
    - ar :
    - tzm :
```

### Exemple rempli

```
- ID : RISK-2025-01
- Date : 2025-05-20
- Catégorie : Sécurité
- Description : Fuite de secrets dans les logs
- Impact : Élevé
- Probabilité : Moyenne
- Criticité : Critique
- Mesures de mitigation : Audit logs, rotation secrets, RBAC
- Statut : Ouvert
- Responsable : DevOps
- Preuve / Lien : /logs/audit/2025-05-20.log
- Commentaire : MFA activé
- Traductions :
    - en : Secrets leak in logs
    - ar : تسرب الأسرار في السجلات
    - tzm: Ttufin n secrets deg yixfawn
```

---

## Multilingue

- **Français** : Ce registre est disponible en français.
- **English** : This register is available in English.
- **العربية** : هذا السجل متوفر باللغة العربية.
- **ⴰⵣⵉⵖⴻⵏⵜ** : Asnif n tamedyazt-agi d-ittwasnen s tmazight.

*(Voir `/docs/i18n/` pour les versions traduites)*

---

## Contact & support

- **Slack** : #dihya-risk
- **Email** : risk@dihya.eu
- **GitHub Issues** : [Lien](https://github.com/votre-org/dihya/issues)

---

> **Ce registre est validé pour la production. Toute modification doit être soumise via PR et validée par le RSSI et le DPO.**
