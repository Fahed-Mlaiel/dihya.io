# 📦 Python Integration Samples

Ce dossier contient des exemples d’intégration ultra avancés pour les modules métier (API, Audit, etc.) côté Python.

## Structure
- Un sous-dossier par domaine métier : `api`, `audit`, etc.
- Chaque sous-dossier contient des exemples Python et JS, un README, des points d'entrée (`__init__.js`, `__init__.py`)
- Un fichier `index.js` permet l'import centralisé de tous les samples JS

## Utilisation de l'index modulaire
```js
import * as samples from './index.js';
samples.api.runApiSample();
samples.audit.runAuditSample();
// ...etc.
```

---

> Ajoutez ici vos propres exemples d’intégration avancée pour chaque domaine métier.
