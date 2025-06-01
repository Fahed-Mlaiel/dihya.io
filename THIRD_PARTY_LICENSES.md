# 📜 Dihya – Third Party Licenses Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Introduction](#introduction)
- [Politique de gestion des licences](#politique-de-gestion-des-licences)
- [Résumé des licences tierces](#résumé-des-licences-tierces)
- [Textes de licences](#textes-de-licences)
- [Audit & conformité](#audit--conformité)
- [Templates & exemples](#templates--exemples)
- [Multilingue](#multilingue)
- [Contact & support](#contact--support)

---

## Introduction

Ce document recense toutes les licences des dépendances tierces utilisées dans **Dihya** (librairies, frameworks, plugins, scripts, assets, outils CI/CD, etc.), leur conformité, leur impact sur la souveraineté et la sécurité.
Il garantit la conformité RGPD/NIS2, la traçabilité, la sécurité, la compatibilité multi-stack (React, Flask, Node, Django, Flutter…), la portabilité (Linux, Codespaces, cloud souverain), l’accessibilité et le fallback IA open source.

---

## Politique de gestion des licences

- **Priorité open source** : toute dépendance doit être open source, auditable, maintenue.
- **Compatibilité** : toutes les licences doivent être compatibles AGPL-3.0.
- **Souveraineté** : aucun composant critique propriétaire sans fallback open source.
- **Conformité** : RGPD, NIS2, audit régulier, SBOM CycloneDX.
- **Traçabilité** : chaque licence est listée, versionnée, documentée.
- **Multilingue** : documentation et alertes en fr, en, ar, tzm.

---

## Résumé des licences tierces

| Stack      | Nom           | Version   | Licence        | Type        | Lien officiel                  |
|------------|---------------|-----------|----------------|-------------|-------------------------------|
| Backend    | Flask         | 3.0.3     | BSD-3-Clause   | Library     | https://palletsprojects.com/p/flask/ |
| Backend    | Django        | 5.0.6     | BSD-3-Clause   | Library     | https://www.djangoproject.com/ |
| Backend    | Node.js       | 20.12.2   | MIT            | Runtime     | https://nodejs.org/            |
| Frontend   | React         | 18.2.0    | MIT            | Library     | https://react.dev/             |
| Mobile     | Flutter       | 3.22.1    | BSD-3-Clause   | Framework   | https://flutter.dev/           |
| DevOps     | GitHub Actions| N/A       | MIT            | CI/CD       | https://github.com/features/actions |
| DevOps     | MinIO         | 7.2.5     | Apache-2.0     | Library     | https://min.io/                |
| IA         | Ollama        | 0.1.0     | Apache-2.0     | Library     | https://ollama.com/            |
| IA         | Mixtral       | 8x7B      | Apache-2.0     | Model       | https://mistral.ai/            |
| Test       | pytest        | 8.2.0     | MIT            | Library     | https://pytest.org/            |
| Test       | axe-core      | 4.8.2     | MPL-2.0        | Library     | https://www.deque.com/axe/     |
| Test       | pa11y         | 6.3.1     | MIT            | Library     | https://pa11y.org/             |
| i18n       | babel         | 2.14.0    | BSD-3-Clause   | Library     | https://babel.pocoo.org/       |

---

## Textes de licences

### BSD-3-Clause

```
Copyright (c) <year> <copyright holders>
Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
...
(texte complet : https://opensource.org/license/bsd-3-clause/)
```

### MIT

```
MIT License

Copyright (c) <year> <copyright holders>

Permission is hereby granted, free of charge, to any person obtaining a copy...
(texte complet : https://opensource.org/license/mit/)
```

### Apache-2.0

```
Apache License
Version 2.0, January 2004
http://www.apache.org/licenses/
...
(texte complet : https://www.apache.org/licenses/LICENSE-2.0)
```

### MPL-2.0

```
Mozilla Public License Version 2.0
...
(texte complet : https://www.mozilla.org/en-US/MPL/2.0/)
```

### AGPL-3.0 (Licence principale Dihya)

```
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
...
(texte complet : https://www.gnu.org/licenses/agpl-3.0.html)
```

---

## Audit & conformité

- **Automatisé** : SBOM CycloneDX, audit Bandit, Snyk, npm audit, pip-audit
- **CI/CD** : chaque build vérifie les licences, conformité RGPD/NIS2
- **Logs** : `/logs/audit/`, rapports `/reports/licenses.html`
- **Procédure** : toute nouvelle dépendance doit être validée par le Tech Lead & RSSI

---

## Templates & exemples

### Template de fiche licence

```
- Nom :
- Version :
- Stack :
- Type :
- Licence :
- Lien officiel :
- Texte de licence :
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
- Type : Library
- Licence : BSD-3-Clause
- Lien officiel : https://palletsprojects.com/p/flask/
- Texte de licence : https://opensource.org/license/bsd-3-clause/
- Traductions :
    - en : Flask backend REST API, BSD-3-Clause license
    - ar : فلاسـك API خلفية، رخصة BSD-3-Clause
    - tzm : Flask backend REST API, BSD-3-Clause
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

- **Slack** : #dihya-licenses
- **Email** : licenses@dihya.eu
- **GitHub Issues** : [Lien](https://github.com/votre-org/dihya/issues)

---

> **Ce document est validé pour la production. Toute modification doit être soumise via PR et validée par le Tech Lead et le RSSI.**

# Licences tierces Dihya

- Liste des licences tierces utilisées
- Conformité, sécurité, reporting
- Procédure de vérification, d’audit

Voir [DEPENDENCIES.md](DEPENDENCIES.md), [THIRD_PARTY_DEPENDENCIES.md](THIRD_PARTY_DEPENDENCIES.md)
