# 📦 Dihya – Third Party Dependencies Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Introduction](#introduction)
- [Politique d’utilisation des dépendances](#politique-dutilisation-des-dépendances)
- [Liste des dépendances tierces](#liste-des-dépendances-tierces)
- [Audit de sécurité & conformité](#audit-de-sécurité--conformité)
- [Fallback open source & souveraineté](#fallback-open-source--souveraineté)
- [Templates & exemples](#templates--exemples)
- [Multilingue](#multilingue)
- [Contact & support](#contact--support)

---

## Introduction

Ce document recense toutes les dépendances tierces utilisées dans **Dihya** (librairies, frameworks, plugins, scripts, assets, outils CI/CD, etc.), leur usage, leur licence, leur impact sur la souveraineté et la sécurité.
Il garantit la conformité RGPD/NIS2, la traçabilité, la sécurité, la compatibilité multi-stack (React, Flask, Node, Django, Flutter…), la portabilité (Linux, Codespaces, cloud souverain), l’accessibilité et le fallback IA open source.

---

## Politique d’utilisation des dépendances

- **Priorité open source** : toute dépendance doit être open source, auditable, maintenue.
- **Souveraineté** : aucun composant critique propriétaire sans fallback open source.
- **Sécurité** : audit régulier (Bandit, Snyk, npm audit), CVE monitoring, MAJ proactive.
- **Conformité** : RGPD, NIS2, licences compatibles AGPL-3.0.
- **Traçabilité** : chaque dépendance est listée, versionnée, documentée (SBOM CycloneDX).
- **Multilingue** : documentation et alertes en fr, en, ar, tzm.

---

## Liste des dépendances tierces

| Stack      | Nom           | Version   | Licence        | Usage principal           | Souveraineté | Fallback open source | Audit sécurité | Lien officiel                  |
|------------|---------------|-----------|----------------|--------------------------|--------------|----------------------|----------------|-------------------------------|
| Backend    | Flask         | 3.0.3     | BSD-3-Clause   | API REST, microservices  | Oui          | Oui                  | Oui            | https://palletsprojects.com/p/flask/ |
| Backend    | Django        | 5.0.6     | BSD-3-Clause   | API REST, admin, ORM     | Oui          | Oui                  | Oui            | https://www.djangoproject.com/ |
| Backend    | Node.js       | 20.12.2   | MIT            | API REST, plugins        | Oui          | Oui                  | Oui            | https://nodejs.org/            |
| Frontend   | React         | 18.2.0    | MIT            | UI, builder, i18n        | Oui          | Oui                  | Oui            | https://react.dev/             |
| Mobile     | Flutter       | 3.22.1    | BSD-3-Clause   | App mobile, UI           | Oui          | Oui                  | Oui            | https://flutter.dev/           |
| DevOps     | GitHub Actions| N/A       | MIT            | CI/CD, build, tests      | Oui          | Oui                  | Oui            | https://github.com/features/actions |
| DevOps     | MinIO         | 7.2.5     | Apache-2.0     | Stockage objet souverain | Oui          | Oui                  | Oui            | https://min.io/                |
| IA         | Ollama        | 0.1.0     | Apache-2.0     | Fallback IA open source  | Oui          | Oui                  | Oui            | https://ollama.com/            |
| IA         | Mixtral       | 8x7B      | Apache-2.0     | Fallback IA open source  | Oui          | Oui                  | Oui            | https://mistral.ai/            |
| Test       | pytest        | 8.2.0     | MIT            | Tests unitaires          | Oui          | Oui                  | Oui            | https://pytest.org/            |
| Test       | axe-core      | 4.8.2     | MPL-2.0        | Audit accessibilité      | Oui          | Oui                  | Oui            | https://www.deque.com/axe/     |
| Test       | pa11y         | 6.3.1     | MIT            | Audit accessibilité      | Oui          | Oui                  | Oui            | https://pa11y.org/             |
| i18n       | babel         | 2.14.0    | BSD-3-Clause   | Internationalisation     | Oui          | Oui                  | Oui            | https://babel.pocoo.org/       |

---

## Audit de sécurité & conformité

- **Automatisé** : Bandit (Python), Snyk (Node), npm audit, pip-audit, SBOM CycloneDX
- **CI/CD** : chaque build vérifie les CVE, licences, conformité RGPD/NIS2
- **Logs** : `/logs/audit/`, rapports `/reports/dependencies.html`
- **Procédure** : toute nouvelle dépendance doit être validée par le Tech Lead & RSSI

---

## Fallback open source & souveraineté

- **Fallback IA** : Mixtral, LLaMA, Ollama (jamais de dépendance critique à une API propriétaire)
- **Stockage** : MinIO, IPFS, SOPS pour secrets
- **CI/CD** : GitHub Actions, runners auto-hébergés possibles
- **Plugins** : sandbox, audit, scoring, fallback open source

---

## Templates & exemples

### Template de fiche dépendance

```
- Nom :
- Version :
- Stack :
- Licence :
- Usage principal :
- Souveraineté : Oui / Non
- Fallback open source : Oui / Non
- Audit sécurité : Oui / Non
- Lien officiel :
- Traductions :
    - en :
    - ar :
    - tzm :
```

### Exemple rempli

```
- Nom : Flask
- Version : 3.0.3
- Stack : Backend
- Licence : BSD-3-Clause
- Usage principal : API REST, microservices
- Souveraineté : Oui
- Fallback open source : Oui
- Audit sécurité : Oui
- Lien officiel : https://palletsprojects.com/p/flask/
- Traductions :
    - en : Flask backend REST API
    - ar : فلاسـك API خلفية
    - tzm : Flask backend REST API
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

- **Slack** : #dihya-dependencies
- **Email** : dependencies@dihya.eu
- **GitHub Issues** : [Lien](https://github.com/votre-org/dihya/issues)

---

> **Ce document est validé pour la production. Toute modification doit être soumise via PR et validée par le Tech Lead et le RSSI.**

# Dépendances tierces Dihya

- Liste des dépendances tierces utilisées (librairies, frameworks, outils)
- Sécurité, licences, conformité
- Procédure d’ajout, de mise à jour, de suppression

Voir [DEPENDENCIES.md](DEPENDENCIES.md), [THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md)
