# 🧠 Dihya – Product Decisions Log (Ultra avancé, multilingue, souveraineté, traçabilité)

---

## Table des matières

- [Introduction](#introduction)
- [Principes de décision](#principes-de-décision)
- [Log des décisions produit](#log-des-décisions-produit)
- [Templates & exemples](#templates--exemples)
- [Multilingue](#multilingue)
- [Contact & support](#contact--support)

---

## Introduction

Ce document centralise toutes les décisions produit majeures du projet **Dihya** (fonctionnelles, techniques, UX, sécurité, souveraineté, accessibilité, RGPD, IA, etc.).
Il garantit la traçabilité, la transparence, la souveraineté numérique, la conformité RGPD/NIS2, la sécurité, la compatibilité multi-stack (React, Flask, Node, Django, Flutter…), et la portabilité (Linux, Codespaces, cloud souverain, fallback open source).

---

## Principes de décision

- **Traçabilité** : chaque décision est datée, motivée, validée, versionnée.
- **Multilingue** : chaque décision est documentée en fr, en, ar, tzm.
- **Souveraineté** : priorité aux solutions open source, cloud souverain, fallback local.
- **Conformité** : RGPD, NIS2, accessibilité, sécurité, auditabilité.
- **Transparence** : chaque décision est consultable par tous les métiers.

---

## Log des décisions produit

| ID        | Date       | Sujet / Décision                        | Motivation / Impact                         | Statut   | Validé par         | Preuve / Lien                | Commentaire |
|-----------|------------|-----------------------------------------|---------------------------------------------|----------|--------------------|------------------------------|-------------|
| DEC-2025-01 | 2025-05-20 | MFA obligatoire pour tous les accès prod | Sécurité, conformité NIS2, RGPD, traçabilité | Validé   | PO, DevOps, DPO    | /docs/security/MFA_POLICY.md | MFA TOTP/SMS |
| DEC-2025-02 | 2025-05-20 | Fallback IA open source (Ollama/LocalAI) | Souveraineté, continuité, conformité RGPD    | Validé   | PO, IA Lead        | /docs/ai/FALLBACK_POLICY.md  | Basculer <200ms |
| DEC-2025-03 | 2025-05-20 | Multilingue natif (fr, en, ar, tzm)      | Inclusion, accessibilité, conformité         | Validé   | PO, QA, DPO        | /docs/i18n/STRATEGY.md       | i18n dynamique |
| DEC-2025-04 | 2025-05-20 | Plugins signés, registry souverain       | Sécurité, modularité, auditabilité           | Validé   | DevOps, Backend    | /docs/plugins/SECURITY.md    | CI/CD signé   |
| DEC-2025-05 | 2025-05-20 | Monitoring open source (Prometheus, Grafana, Loki) | Souveraineté, conformité, auditabilité | Validé   | DevOps, QA         | /docs/monitoring/ARCH.md     | Alertes multilingues |
| ...       | ...        | ...                                     | ...                                         | ...      | ...                | ...                          | ...         |

---

## Templates & exemples

### Template de décision produit

```
- ID :
- Date :
- Sujet / Décision :
- Motivation / Impact :
- Statut : Proposé / Validé / Rejeté
- Validé par :
- Preuve / Lien :
- Commentaire :
- Traductions :
    - en :
    - ar :
    - tzm :
```

### Exemple rempli

```
- ID : DEC-2025-01
- Date : 2025-05-20
- Sujet / Décision : MFA obligatoire pour tous les accès prod
- Motivation / Impact : Sécurité, conformité NIS2, RGPD, traçabilité
- Statut : Validé
- Validé par : PO, DevOps, DPO
- Preuve / Lien : /docs/security/MFA_POLICY.md
- Commentaire : MFA TOTP/SMS
- Traductions :
    - en : Mandatory MFA for all production access
    - ar : المصادقة الثنائية إلزامية لكل وصول للإنتاج
    - tzm: MFA yella d wajib i yal unekcum n production
```

---

## Multilingue

- **Français** : Ce log est disponible en français.
- **English** : This log is available in English.
- **العربية** : هذا السجل متوفر باللغة العربية.
- **ⴰⵣⵉⵖⴻⵏⵜ** : Asnif n tamedyazt-agi d-ittwasnen s tmazight.

*(Voir `/docs/i18n/` pour les versions traduites)*

---

## Contact & support

- **Slack** : #dihya-decisions
- **Email** : decisions@dihya.eu
- **GitHub Issues** : [Lien](https://github.com/your-org/dihya/issues)

---

> **Ce log est validé pour la production. Toute modification doit être soumise via PR et validée par le PO et le Doc Lead.**

# Product Decisions Dihya

- Historique des décisions produit majeures
- Date, contexte, alternatives, décision prise, impact
- Liens vers les discussions, issues, PR

Voir [ROADMAP.md](ROADMAP.md), [PRODUCT_BACKLOG.md](PRODUCT_BACKLOG.md)
