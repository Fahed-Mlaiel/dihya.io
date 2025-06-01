# 🚨 Dihya – Politique et Procédure de Gestion des Incidents de Sécurité

---

## Table des matières

- [Introduction](#introduction)
- [Objectifs](#objectifs)
- [Définitions](#définitions)
- [Rôles et responsabilités](#rôles-et-responsabilités)
- [Typologie des incidents](#typologie-des-incidents)
- [Procédure de gestion des incidents](#procédure-de-gestion-des-incidents)
- [Communication & notification](#communication--notification)
- [Journalisation & traçabilité](#journalisation--traçabilité)
- [Tests & exercices](#tests--exercices)
- [Amélioration continue](#amélioration-continue)
- [Multilingue](#multilingue)
- [Contact & support](#contact--support)
- [Réponse aux incidents Dihya](#réponse-aux-incidents-dihya)

---

## Introduction

Ce document décrit la politique et la procédure de gestion des incidents de sécurité pour le projet **Dihya**. Il garantit la souveraineté numérique, la conformité RGPD, la réactivité, la traçabilité et la transparence, quel que soit le stack technique (React, Flask, Node, Django, Flutter…).

---

## Objectifs

- Détecter, signaler, analyser et résoudre tout incident de sécurité.
- Limiter l’impact, restaurer les services, préserver la confidentialité, l’intégrité et la disponibilité.
- Assurer la conformité légale (RGPD, NIS2, etc.).
- Documenter chaque incident pour l’amélioration continue.

---

## Définitions

- **Incident de sécurité** : tout événement compromettant la confidentialité, l’intégrité ou la disponibilité des systèmes, données ou services.
- **Exemples** : fuite de données, compromission de compte, attaque DDoS, malware, faille 0-day, erreur humaine, etc.

---

## Rôles et responsabilités

| Rôle                | Responsabilités principales                                   |
|---------------------|--------------------------------------------------------------|
| Utilisateur         | Signaler tout incident ou comportement suspect               |
| Dev/DevOps          | Analyser, corriger, documenter, appliquer les correctifs     |
| RSSI                | Piloter la gestion, valider la communication, rapporter      |
| DPO                 | Gérer les aspects RGPD, notifier la CNIL si nécessaire       |
| Support             | Assister les utilisateurs, escalader les incidents critiques |

---

## Typologie des incidents

- **Confidentialité** : fuite, accès non autorisé, interception.
- **Intégrité** : altération, corruption, suppression non autorisée.
- **Disponibilité** : déni de service, panne, perte d’accès.
- **Authentification** : compromission de compte, élévation de privilèges.
- **Souveraineté** : fuite hors UE, dépendance cloud non maîtrisée.

---

## Procédure de gestion des incidents

1. **Détection**
   - Surveillance automatisée (SIEM, Sentry, Prometheus, logs centralisés).
   - Signalement utilisateur (formulaire, email, Slack, GitHub Issues).

2. **Signalement**
   - Utiliser le template d’incident (`.github/ISSUE_TEMPLATE/incident_report.md`).
   - Préciser date, heure, impact, contexte, actions déjà entreprises.

3. **Analyse**
   - Priorisation (critique, majeur, mineur).
   - Investigation technique (logs, forensics, audit).
   - Identification des causes et périmètre.

4. **Réponse & correction**
   - Contenir l’incident (isolation, blocage, rollback).
   - Corriger la faille, restaurer les services.
   - Documenter toutes les actions.

5. **Communication**
   - Notification interne (équipe, RSSI, DPO).
   - Notification externe (utilisateurs, CNIL, autorités si requis).

6. **Clôture & retour d’expérience**
   - Rédiger un rapport post-mortem.
   - Mettre à jour la documentation, les procédures, les tests.

---

## Communication & notification

- **Canaux** : Slack #dihya-incident, email sécurité, GitHub Issues.
- **RGPD** : notification CNIL sous 72h si données personnelles concernées.
- **Transparence** : communication adaptée selon la gravité et l’impact.

---

## Journalisation & traçabilité

- **Logs centralisés** (ELK, Loki, SIEM).
- **Horodatage précis, horloge synchronisée (NTP)**.
- **Conservation** : 1 an minimum, accès restreint.
- **Auditabilité** : chaque action d’incident est tracée et archivée.

---

## Tests & exercices

- **Tests automatisés** : injection, faille, simulation d’incident (CI/CD).
- **Exercices réguliers** : table-top, simulation phishing, faille 0-day.
- **Revue annuelle** de la procédure.

---

## Amélioration continue

- **Retour d’expérience** après chaque incident.
- **Mise à jour** régulière des outils, procédures, formations.
- **Veille sécurité** (CERT-FR, ANSSI, CVE…).

---

## Multilingue

- **Français** : Ce guide est disponible en français.
- **English** : This guide is available in English.
- **العربية** : هذا الدليل متوفر باللغة العربية.
- **ⴰⵣⵉⵖⴻⵏⵜ** : Asnif n tamedyazt-agi d-ittwasnen s tmazight.

*(Voir `/docs/i18n/` pour les versions traduites)*

---

## Contact & support

- **Slack** : #dihya-incident
- **Email** : security@dihya.eu
- **GitHub Issues** : [Lien](https://github.com/your-org/dihya/issues)

---

## Réponse aux incidents Dihya

- Procédures d’alerte, escalade, communication
- Journalisation, analyse, post-mortem, reporting
- Outils recommandés (Sentry, PagerDuty, ELK, etc.)
- Templates de rapport d’incident

Voir [INCIDENTS_GUIDE.md](INCIDENTS_GUIDE.md), [AUDIT_LOGGING_GUIDE.md](AUDIT_LOGGING_GUIDE.md)

---

> **Ce document est validé pour la production. Toute modification doit être soumise via PR et validée par le RSSI et le DPO.**
