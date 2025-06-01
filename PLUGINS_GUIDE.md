# 🧩 Dihya – Guide des Plugins & Extensions (Ultra avancé, multilingue, souveraineté)

---

## Table des matières

- [Introduction](#introduction)
- [Principes des plugins](#principes-des-plugins)
- [Architecture & sécurité](#architecture--sécurité)
- [Développement d’un plugin](#développement-dun-plugin)
- [Exemples de plugins](#exemples-de-plugins)
- [Tests & validation](#tests--validation)
- [Templates & modèles](#templates--modèles)
- [Multilingue](#multilingue)
- [Contact & support](#contact--support)

---

## Introduction

Ce guide décrit la politique de développement, d’intégration et de validation des plugins/extensions pour le projet **Dihya**.
Il garantit la modularité, la sécurité, la souveraineté numérique, la conformité RGPD, l’accessibilité, la compatibilité multi-stack (React, Flask, Node, Django, Flutter…), et la portabilité (Linux, Codespaces, cloud souverain, fallback open source).

---

## Principes des plugins

- **Modularité** : chaque plugin est indépendant, versionné, documenté, testé.
- **Sécurité** : audit de code, sandboxing, RBAC, pas de dépendance non souveraine.
- **Extensibilité** : API claire, hooks/events, injection dynamique.
- **Multilingue** : chaque plugin doit supporter fr, en, ar, tzm.
- **Accessibilité** : UI/UX accessible, conforme RGAA/WCAG.
- **Fallback** : plugins critiques doivent avoir un fallback open source.

---

## Architecture & sécurité

- **Isolation** : plugins chargés dynamiquement, isolation des droits et ressources.
- **Contrôles d’accès** : RBAC appliqué à chaque plugin.
- **Auditabilité** : chaque action plugin est loggée (voir [LOGGING_GUIDE.md](LOGGING_GUIDE.md)).
- **Conformité RGPD** : aucun traitement de donnée perso sans consentement explicite.
- **Souveraineté** : plugins validés, signés, hébergés sur registry souverain.

---

## Développement d’un plugin

### 1. Structure recommandée

```
plugins/
  myplugin/
    README.md
    plugin.json
    src/
      index.js (ou .py, .dart…)
    tests/
      test_myplugin.js
    i18n/
      fr.json
      en.json
      ar.json
      tzm.json
    assets/
      icon.svg
      ...
```

### 2. Exemple de manifest plugin.json

```json
{
  "name": "dihya-accessibility-audit",
  "version": "1.0.0",
  "description": "Audit d’accessibilité RGAA/WCAG multilingue",
  "author": "Dihya Core Team",
  "main": "src/index.js",
  "i18n": ["fr", "en", "ar", "tzm"],
  "permissions": ["a11y:audit", "logs:write"],
  "fallback": true,
  "sovereign": true
}
```

### 3. Exemple de code (React)

```javascript
// src/index.js
import { useTranslation } from 'react-i18next';

export default function AccessibilityAuditPlugin({ url }) {
  const { t } = useTranslation();
  return (
    <div>
      <h2>{t('audit.title')}</h2>
      {/* Appel API d’audit, affichage résultats multilingues */}
    </div>
  );
}
```

### 4. Exemple de code (Python/Flask)

```python
# src/index.py
from flask import Blueprint, request, jsonify
plugin = Blueprint('a11y_audit', __name__)

@plugin.route('/plugin/a11y/audit', methods=['POST'])
def audit():
    url = request.json.get('url')
    # Appel audit accessibilité, logs, i18n
    return jsonify({"result": "OK", "lang": request.json.get("lang", "fr")})
```

---

## Exemples de plugins

- **dihya-accessibility-audit** : Audit RGAA/WCAG, multilingue, fallback open source.
- **dihya-ia-fallback** : Fallback IA open source (Ollama, LocalAI).
- **dihya-logging-export** : Export logs structurés, anonymisés, multilingue.
- **dihya-rgpd-consent** : Gestion consentement RGPD, multilingue, journalisation.
- **dihya-i18n-switcher** : Changement dynamique de langue, UI/UX accessible.

---

## Tests & validation

- **Tests unitaires, intégration, e2e** pour chaque plugin.
- **Audit sécurité** (Bandit, npm audit, etc.).
- **Tests multilingues** (fr, en, ar, tzm).
- **Tests accessibilité** (axe-core, pa11y).
- **CI/CD** : pipeline dédié, zéro warning/fail, artefacts signés.

---

## Templates & modèles

### Template de manifest plugin

```json
{
  "name": "",
  "version": "",
  "description": "",
  "author": "",
  "main": "",
  "i18n": ["fr", "en", "ar", "tzm"],
  "permissions": [],
  "fallback": false,
  "sovereign": true
}
```

### Template README.md plugin

```
# [Nom du plugin] – Dihya

## Description
[Résumé, fonctionnalités, stack, multilingue, accessibilité, souveraineté…]

## Installation
[Procédure, dépendances, sécurité, fallback…]

## Utilisation
[Exemples, hooks, API, UI…]

## Tests
[Commandes, couverture, accessibilité, multilingue…]

## Contact
[Email, Slack, GitHub Issues]
```

---

## Multilingue

- **Français** : Ce guide est disponible en français.
- **English** : This guide is available in English.
- **العربية** : هذا الدليل متوفر باللغة العربية.
- **ⴰⵣⵉⵖⴻⵏⵜ** : Asnif n tamedyazt-agi d-ittwasnen s tmazight.

*(Voir `/docs/i18n/` pour les versions traduites)*

---

## Contact & support

- **Slack** : #dihya-plugins
- **Email** : plugins@dihya.eu
- **GitHub Issues** : [Lien](https://github.com/your-org/dihya/issues)

---

> **Ce guide est validé pour la production. Toute modification doit être soumise via PR et validée par le Doc Lead et le RSSI.**

# Guide des plugins Dihya

- Architecture des plugins (backend, frontend, mobile, IA)
- Création, installation, configuration, sécurité
- Marketplace, contribution, validation automatique
- Exemples de plugins métiers, templates, documentation
- Tests, CI/CD, multilingue, accessibilité

Voir [CONTRIBUTING.md](CONTRIBUTING.md), [ROADMAP.md](ROADMAP.md)

---

# PLUGINS_GUIDE.md

# Guide Plugins Ultra-Avancé – Dihya Coding

## Objectifs
- Extensibilité maximale, sécurité, auditabilité, RGPD, accessibilité, multilingue, CI/CD-ready

## Installation & gestion
1. **Installation** : via API `/api/plugins/install` ou CLI
2. **Sécurité** : sandbox, audit, logs, monitoring, rollback
3. **Mise à jour** : versioning, compatibilité, rollback
4. **Audit & RGPD** : logs, conformité RGPD, accessibilité

## Exemples de commandes
```bash
make plugins-install
```

## Documentation intégrée
- Voir aussi: API_REFERENCE.md, AUDIT_LOGGING_GUIDE.md, SECURITY.md

---

Pour toute question, contacter l’équipe plugins.
