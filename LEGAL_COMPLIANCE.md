# ⚖️ Dihya – Synthèse de Conformité Légale & Réglementaire

---

## Table des matières

- [Introduction](#introduction)
- [Résumé des exigences légales](#résumé-des-exigences-légales)
- [Statut de conformité](#statut-de-conformité)
- [Contrôles & audits](#contrôles--audits)
- [Procédure de déclaration](#procédure-de-déclaration)
- [Templates & exemples](#templates--exemples)
- [Multilingue](#multilingue)
- [Contact & support](#contact--support)

---

## Introduction

Ce document synthétise la conformité légale et réglementaire du projet **Dihya**. Il couvre RGPD, NIS2, accessibilité, souveraineté numérique, open source, propriété intellectuelle, pour tous les environnements et stacks (React, Flask, Node, Django, Flutter…).

---

## Résumé des exigences légales

| Cadre         | Statut      | Dernier audit | Responsable | Lien/Preuve                                      |
|---------------|-------------|---------------|-------------|--------------------------------------------------|
| RGPD          | Conforme    | 2025-05-01    | DPO         | [DPIA](./docs/DPIA_TEMPLATE.md)                  |
| NIS2          | Conforme    | 2025-05-01    | RSSI        | [Audit sécurité](./inventaire_controle_corrige.csv) |
| Accessibilité | Conforme    | 2025-05-01    | UX Lead     | [Rapport RGAA](./docs/accessibilite.md)          |
| Open Source   | Conforme    | 2025-05-01    | DevOps      | [SPDX](./docs/spdx_report.md)                    |
| Souveraineté  | Conforme    | 2025-05-01    | RSSI        | [Contrôles](./inventaire_controle_corrige.csv)   |
| Propriété intellectuelle | Conforme | 2025-05-01 | PO/PM | [INPI](https://www.inpi.fr/)                     |

---

## Statut de conformité

- **RGPD** : DPIA réalisé, consentement géré, droits utilisateurs respectés.
- **NIS2** : sécurité réseaux/systèmes, journalisation, gestion incidents.
- **Accessibilité** : audit RGAA/WCAG à chaque release, corrections tracées.
- **Open source** : licences vérifiées, conformité AGPL-3.0, inventaire SPDX.
- **Souveraineté** : données localisées, fallback IA open source, cloud souverain.
- **Propriété intellectuelle** : contributions tracées, respect licences.

---

## Contrôles & audits

- **Automatisés** : CI/CD, Snyk, OWASP, audit accessibilité, scan licences.
- **Registre** : `/inventaire_controle_corrige.csv` (multilingue, traçabilité, auditabilité).
- **Preuves** : logs, rapports, tickets, audits externes.

---

## Procédure de déclaration

1. **Détecter** un écart ou incident de conformité.
2. **Déclarer** via GitHub Issues ou email (voir contacts).
3. **Analyser** et prioriser (critique, majeur, mineur).
4. **Corriger** et documenter toutes les actions.
5. **Clôturer** avec rapport et mise à jour du registre.

---

## Templates & exemples

### Clause RGPD (exemple)

> Les données personnelles sont traitées conformément au RGPD. Toute personne peut exercer ses droits via privacy@dihya.eu.

### Clause accessibilité (exemple)

> Toutes les interfaces sont auditées RGAA/WCAG à chaque release. Les corrections sont tracées dans le registre d’accessibilité.

### Modèle de déclaration d’écart

```
- Date/Heure : YYYY-MM-DD HH:MM
- Cadre concerné : RGPD / NIS2 / Accessibilité / Open Source / Souveraineté / PI
- Description :
- Actions menées :
- Statut : Ouvert / Résolu
- Référent :
- Lien rapport :
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

- **DPO** : dpo@dihya.eu
- **RSSI** : rssi@dihya.eu
- **Slack** : #dihya-legal
- **GitHub Issues** : [Lien](https://github.com/your-org/dihya/issues)

---

> **Ce document est validé pour la production. Toute modification doit être soumise via PR et validée par le DPO et le RSSI.**

---

# Conformité légale Dihya

- Respect RGPD, AGPL, licences open source
- Documentation de conformité, logs, audit, reporting
- Gestion des consentements, droits utilisateurs, portabilité
- Sécurité juridique, veille réglementaire, transparence

Voir [LEGAL_COMPLIANCE_GUIDE.md](LEGAL_COMPLIANCE_GUIDE.md), [AUDIT_LOGGING_GUIDE.md](AUDIT_LOGGING_GUIDE.md)

---

# Legal Compliance

Dieses Dokument contient des Hinweise et Richtlinien zur Einhaltung gesetzlicher Vorgaben (z.B. DSGVO, Urheberrecht, Lizenzierung).

## Wichtige Aspekte
- Datenschutz & Datensicherheit
- Lizenzmanagement
- Dokumentationspflichten
- Auditierbarkeit

Siehe aussi : `securite.md`, `AUDIT_LOGGING_GUIDE.md`, `LEGAL_COMPLIANCE_GUIDE.md`

---

# LEGAL_COMPLIANCE.md

# Conformité Légale – Dihya Coding

## RGPD
- Consentement, droit à l’oubli, portabilité, logs, audit
- Documentation intégrée, plugins, backup, monitoring

## Accessibilité
- Conformité WCAG 2.1, multilingue, navigation clavier

## Sécurité
- Audit, logs, monitoring, backup, plugins

## CI/CD
- Vérification automatisée, reporting, documentation

## Documentation intégrée
- Voir aussi: LEGAL_COMPLIANCE_GUIDE.md, AUDIT_LOGGING_GUIDE.md, ACCESSIBILITY_GUIDE.md

---

Pour toute question, contacter l’équipe conformité.
