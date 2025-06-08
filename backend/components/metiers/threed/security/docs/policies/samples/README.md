# 📦 Samples – Politiques de sécurité

Ce dossier centralise les exemples d’intégration ultra avancés pour les politiques d’accès, d’audit et RGPD.

## Structure
- Un sous-dossier par domaine métier : `access/`, `audit/`, `rgpd/`
- Chaque sous-dossier contient des exemples JS et Python, un README, des points d'entrée (`__init__.js`, `__init__.py`)
- Un fichier `index.js` permet l'import centralisé de tous les samples JS

## Utilisation de l'index modulaire
```js
import * as samples from './index.js';
samples.access.demoAccessPolicy();
samples.audit.demoAuditPolicy();
samples.rgpd.demoRgpdPolicy();
```

---

> Ajoutez ici vos propres exemples d’intégration avancée pour chaque domaine métier.
