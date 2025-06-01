# 📚 Dihya – Decision Log Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Introduction](#introduction)
- [Format du decision log](#format-du-decision-log)
- [Décisions techniques majeures](#décisions-techniques-majeures)
- [Templates & exemples](#templates--exemples)
- [Multilingue](#multilingue)
- [Contact & gouvernance](#contact--gouvernance)

---

## Introduction

Ce document trace toutes les décisions structurantes du projet **Dihya** : architecture, sécurité, accessibilité, RGPD, plugins, templates, DevOps, souveraineté numérique, etc.
Il est multilingue (fr, en, ar, tzm), structuré, compatible audit, CI/CD, production, démo, contribution.

---

## Format du decision log

Chaque entrée doit inclure :
- ID, date, auteur, stack concernée
- Décision (fr, en, ar, tzm)
- Contexte, alternatives, justification, impact
- Lien PR/commit, preuve de test, statut (validée, en cours, rejetée)
- Impact sécurité/accessibilité/souveraineté

---

# Decision Log Dihya

- Historique des décisions techniques, produit, sécurité, architecture
- Date, contexte, alternatives, décision prise, impact
- Liens vers les discussions, issues, PR

Voir [PRODUCT_DECISIONS.md](PRODUCT_DECISIONS.md), [ROADMAP.md](ROADMAP.md)

## Décisions techniques majeures

### DEC-001 – 2025-05-20 – Tech Lead

- **Décision** :
    - fr : Adoption d’une architecture multi-stack (React, Flask, Node, Django, Flutter) avec fallback IA open source et stockage souverain (MinIO/IPFS)
    - en : Adoption of a multi-stack architecture (React, Flask, Node, Django, Flutter) with open source AI fallback and sovereign storage (MinIO/IPFS)
    - ar : اعتماد بنية متعددة الطبقات (React, Flask, Node, Django, Flutter) مع fallback IA مفتوح المصدر وتخزين سيادي (MinIO/IPFS)
    - tzm : Ttwasna n tazwart multi-stack (React, Flask, Node, Django, Flutter) s fallback IA open source d uselkim amatu (MinIO/IPFS)
- **Contexte** : Besoin de portabilité, souveraineté, auditabilité, compatibilité cloud souverain, RGPD/NIS2.
- **Alternatives** : Stack monolithique, cloud propriétaire, IA SaaS.
- **Justification** : Sécurité, modularité, conformité, indépendance technologique.
- **Lien PR/commit** : #1
- **Preuve de test** : CI/CD, e2e, audit SBOM
- **Statut** : validée
- **Impact** : sécurité, souveraineté, extensibilité

### DEC-002 – 2025-05-20 – DPO

- **Décision** :
    - fr : Implémentation RGPD/NIS2 stricte, logs anonymisés, consentement exportable, purge sur demande
    - en : Strict RGPD/NIS2 implementation, anonymized logs, exportable consent, on-demand purge
    - ar : تنفيذ صارم لـ RGPD/NIS2، سجلات مجهولة، موافقة قابلة للتصدير، حذف عند الطلب
    - tzm : Asnul RGPD/NIS2 s uselkim, logs ur nttwaf ara, consent exportable, purge s uselkim
- **Contexte** : Conformité légale, confiance utilisateurs, auditabilité.
- **Alternatives** : RGPD partiel, logs non anonymisés.
- **Justification** : Obligations légales, réputation, sécurité.
- **Lien PR/commit** : #2
- **Preuve de test** : audit RGPD, tests purge/export
- **Statut** : validée
- **Impact** : conformité, sécurité, confiance

### DEC-003 – 2025-05-20 – DevOps Lead

- **Décision** :
    - fr : Pipelines CI/CD GitHub Actions, artefacts signés, rollback automatisé, monitoring Prometheus/Grafana
    - en : CI/CD pipelines with GitHub Actions, signed artefacts, automated rollback, Prometheus/Grafana monitoring
    - ar : خطوط أنابيب CI/CD مع GitHub Actions، توقيع الحزم، استرجاع تلقائي، مراقبة Prometheus/Grafana
    - tzm : Pipelines CI/CD s GitHub Actions, artefacts yettwaznen, rollback automatic, monitoring Prometheus/Grafana
- **Contexte** : Besoin de traçabilité, sécurité, monitoring temps réel.
- **Alternatives** : CI/CD manuel, monitoring partiel.
- **Justification** : Robustesse, auditabilité, rapidité de réaction.
- **Lien PR/commit** : #3
- **Preuve de test** : CI, rollback test, alertes monitoring
- **Statut** : validée
- **Impact** : sécurité, fiabilité, traçabilité

---

## Templates & exemples

### Template de décision

```
- ID :
- Date :
- Auteur :
- Stack concernée :
- Décision :
    - fr :
    - en :
    - ar :
    - tzm :
- Contexte :
- Alternatives :
- Justification :
- Lien PR/commit :
- Preuve de test :
- Statut : validée / en cours / rejetée
- Impact sécurité/accessibilité/souveraineté :
```

### Exemple rempli

```
- ID : DEC-004
- Date : 2025-05-20
- Auteur : QA Lead
- Stack concernée : Frontend, Mobile
- Décision :
    - fr : Audit accessibilité AA/AAA, navigation clavier, i18n complet
    - en : Accessibility audit AA/AAA, keyboard navigation, full i18n
    - ar : تدقيق الوصولية AA/AAA، تنقل لوحة المفاتيح، دعم i18n كامل
    - tzm : Audit n tazwart n useqdec AA/AAA, tazwart n taddart, i18n
- Contexte : Inclusion, conformité RGAA/WCAG, accessibilité universelle.
- Alternatives : Accessibilité partielle, audit manuel.
- Justification : Obligations légales, expérience utilisateur, image projet.
- Lien PR/commit : #4
- Preuve de test : axe-core, pa11y, lighthouse
- Statut : validée
- Impact sécurité/accessibilité/souveraineté : accessibilité, inclusion, conformité

---

## Multilingue

- **Français** : Ce document est disponible en français.
- **English** : This document is available in English.
- **العربية** : هذا المستند متوفر باللغة العربية.
- **ⴰⵣⵉⵖⴻⵏⵜ** : Asnif n tamedyazt-agi d-ittwasnen s tmazight.

*(Voir `/docs/i18n/` pour les versions traduites)*

---

## Contact & gouvernance

- **Slack** : #dihya-decisions
- **Email** : decisions@dihya.eu
- **GitHub Issues** : [Lien](https://github.com/votre-org/dihya/issues)

---

> **Ce decision log est validé pour la production. Toute modification doit être soumise via PR et validée par le Tech Lead, le DPO et le RSSI.**
