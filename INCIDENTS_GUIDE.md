# 🛡️ Dihya – Guide Opérationnel de Gestion des Incidents

---

## Table des matières

- [Introduction](#introduction)
- [Principes de gestion des incidents](#principes-de-gestion-des-incidents)
- [Typologie des incidents](#typologie-des-incidents)
- [Procédure détaillée](#procédure-détaillée)
- [Rôles et responsabilités](#rôles-et-responsabilités)
- [Outils & automatisation](#outils--automatisation)
- [Templates & exemples](#templates--exemples)
- [Tests & exercices](#tests--exercices)
- [Multilingue](#multilingue)
- [Contact & support](#contact--support)

---

## Introduction

Ce guide opérationnel décrit comment détecter, signaler, analyser, corriger et documenter tout incident de sécurité ou de production dans le projet **Dihya**. Il s’applique à tous les environnements (dev, staging, prod), tous les stacks (React, Flask, Node, Django, Flutter…), et garantit souveraineté, conformité RGPD, traçabilité, et amélioration continue.

---

## Principes de gestion des incidents

- **Réactivité** : tout incident doit être détecté et traité sans délai.
- **Transparence** : chaque étape est tracée, chaque action documentée.
- **Souveraineté** : aucune donnée sensible ne sort du périmètre souverain.
- **Automatisation** : détection, notification, et correction automatisées dès que possible.
- **Amélioration continue** : chaque incident nourrit la sécurité future.

---

## Typologie des incidents

- **Sécurité** : fuite de données, compromission, malware, DDoS, faille 0-day.
- **Production** : panne, dégradation de service, bug critique, rollback.
- **Conformité** : violation RGPD, fuite hors UE, accès non autorisé.
- **Souveraineté** : dépendance cloud non maîtrisée, perte de contrôle.

---

## Procédure détaillée

1. **Détection**
   - Automatique : SIEM, Sentry, Prometheus, logs centralisés, alertes CI/CD.
   - Manuelle : signalement utilisateur, support, audit.

2. **Signalement**
   - Utiliser le template `.github/ISSUE_TEMPLATE/incident_report.md`.
   - Préciser date, heure, impact, contexte, actions déjà entreprises.

3. **Analyse**
   - Prioriser (critique, majeur, mineur).
   - Investiguer (logs, forensics, audit, replay).
   - Identifier cause racine et périmètre.

4. **Réponse & correction**
   - Contenir (isolation, blocage, rollback).
   - Corriger la faille, restaurer les services.
   - Documenter toutes les actions.

5. **Communication**
   - Notification interne (équipe, RSSI, DPO).
   - Notification externe (utilisateurs, CNIL, autorités si requis).

6. **Clôture & retour d’expérience**
   - Rapport post-mortem.
   - Mise à jour documentation, procédures, tests.

---

## Rôles et responsabilités

| Rôle        | Responsabilités principales                                   |
|-------------|--------------------------------------------------------------|
| Utilisateur | Signaler tout incident ou comportement suspect               |
| Dev/DevOps  | Analyser, corriger, documenter, appliquer les correctifs     |
| RSSI        | Piloter la gestion, valider la communication, rapporter      |
| DPO         | Gérer RGPD, notifier la CNIL si nécessaire                   |
| Support     | Assister, escalader les incidents critiques                  |

---

## Outils & automatisation

- **Surveillance** : ELK, Loki, Prometheus, Sentry, SIEM open source.
- **Notification** : Slack #dihya-incident, email, GitHub Actions.
- **Journalisation** : logs centralisés, horodatage NTP, conservation 1 an min.
- **CI/CD** : tests d’injection, simulation d’incident, rollback automatisé.
- **Scripts** : `/scripts/incident_report.sh`, `/scripts/incident_notify.py`.

---

## Templates & exemples

### Template de signalement d’incident (GitHub)

```
Titre : [Incident][Date][Criticité] Description courte

- Date/Heure : YYYY-MM-DD HH:MM
- Impact : (service, données, utilisateurs concernés)
- Description :
- Actions déjà entreprises :
- Logs/Preuves :
- Personne référente :
```

### Exemple de script de notification (Python)

````python
import requests, os

def notify_incident(message):
    webhook = os.getenv("DIHYA_INCIDENT_WEBHOOK")
    if webhook:
        requests.post(webhook, json={"text": message})

notify_incident("Incident critique détecté sur prod. Voir logs pour détails.")
````

# Guide des incidents Dihya

- Typologie des incidents (sécurité, infra, données, code, utilisateurs)
- Procédures de gestion, communication, résolution
- Documentation, reporting, post-mortem
- Exemples de gestion d’incident

Voir [INCIDENT_RESPONSE.md](INCIDENT_RESPONSE.md), [AUDIT_LOGGING_GUIDE.md](AUDIT_LOGGING_GUIDE.md)
