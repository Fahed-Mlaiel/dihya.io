# 📦 Integration Samples (Node.js & Python)

Ce dossier centralise les exemples d’intégration ultra avancés pour tous les modules métier (API, RBAC, Audit, Compliance, Monitoring, Onboarding) côté Node.js et Python.

## Structure
- Un sous-dossier `nodejs/` pour les samples Node.js
- Un sous-dossier `python/` pour les samples Python
- Un fichier `index.js` permet l'import centralisé de tous les samples Node.js et Python

## Utilisation de l'index modulaire
```js
import * as samples from './index.js';
samples.nodejs.api.runApiSample();
samples.python.api.runApiSample();
// ...etc.
```

---

> Ajoutez ici des liens ou des guides pour naviguer entre les samples Node.js et Python.
