# 🛡️ Dihya – Registre et Historique des Incidents

---

## Table des matières

- [Introduction](#introduction)
- [Registre des incidents](#registre-des-incidents)
- [Statistiques globales](#statistiques-globales)
- [Procédure de déclaration](#procédure-de-déclaration)
- [Templates & exemples](#templates--exemples)
- [Multilingue](#multilingue)
- [Contact & support](#contact--support)

---

## Introduction

Ce registre centralise tous les incidents de sécurité et de production du projet **Dihya**. Il garantit la traçabilité, la conformité RGPD, la souveraineté numérique, et l’amélioration continue.
Chaque incident doit être consigné ici ou via le template GitHub dédié.

---

## Registre des incidents

# Registre des incidents Dihya

- Historique des incidents majeurs
- Date, impact, résolution, post-mortem
- Liens vers les rapports détaillés

Voir [INCIDENTS_GUIDE.md](INCIDENTS_GUIDE.md)

| Date/Heure         | Criticité | Impact                  | Description courte           | Statut     | Actions menées           | Référent         | Lien rapport           |
|--------------------|-----------|-------------------------|------------------------------|------------|--------------------------|------------------|------------------------|
| 2024-05-01 14:32   | Critique  | API prod indisponible   | DDoS sur endpoint public     | Résolu     | Blocage IP, rollback     | @devops-lead     | [Rapport #12](https://github.com/your-org/dihya/issues/12) |
| 2024-04-18 09:10   | Majeur    | Fuite logs staging      | Logs sensibles exposés       | Résolu     | Rotation clés, purge     | @dpo             | [Rapport #9](https://github.com/your-org/dihya/issues/9)   |
| ...                | ...       | ...                     | ...                          | ...        | ...                      | ...              | ...                    |

---

## Statistiques globales

- **Incidents critiques** : 1
- **Incidents majeurs** : 1
- **Incidents mineurs** : 0
- **Incidents ouverts** : 0
- **Incidents résolus** : 2
- **Dernière mise à jour** : 2025-05-20

---

## Procédure de déclaration

1. **Détecter** l’incident (automatique ou manuel).
2. **Déclarer** via le template GitHub `.github/ISSUE_TEMPLATE/incident_report.md` ou ce registre.
3. **Analyser** et prioriser (critique, majeur, mineur).
4. **Corriger** et documenter toutes les actions.
5. **Clôturer** avec un rapport post-mortem.

---

## Templates & exemples

### Template d’incident (Markdown)

```
- Date/Heure : YYYY-MM-DD HH:MM
- Criticité : Critique / Majeur / Mineur
- Impact : (service, données, utilisateurs concernés)
- Description :
- Actions menées :
- Statut : Ouvert / Résolu
- Référent :
- Lien rapport :
```

### Exemple d’incident

```
- Date/Heure : 2024-05-01 14:32
- Criticité : Critique
- Impact : API prod indisponible
- Description : Attaque DDoS sur endpoint public, saturation du service.
- Actions menées : Blocage IP, rollback, renforcement WAF.
- Statut : Résolu
- Référent : @devops-lead
- Lien rapport : https://github.com/your-org/dihya/issues/12
```

---

## Multilingue

- **Français** : Ce registre est disponible en français.
- **English** : This logbook is available in English.
- **العربية** : هذا السجل متوفر باللغة العربية.
- **ⴰⵣⵉⵖⴻⵏⵜ** : Asnif n tamedyazt-agi d-ittwasnen s tmazight.

*(Voir `/docs/i18n/` pour les versions traduites)*

---

## Contact & support

- **Slack** : #dihya-incident
- **Email** : security@dihya.eu
- **GitHub Issues** : [Lien](https://github.com/your-org/dihya/issues)

---

> **Ce registre est validé pour la production. Toute modification doit être soumise via PR et validée par le RSSI et le DPO.**
