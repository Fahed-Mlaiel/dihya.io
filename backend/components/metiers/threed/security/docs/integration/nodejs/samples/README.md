# 📦 Node.js Integration Samples

Ce dossier contient des exemples d’intégration Node.js pour les modules métier (API, RBAC, Audit, Compliance, Monitoring, Onboarding).

## Structure
- Un sous-dossier par domaine métier : `api`, `rbac`, `audit`, `compliance`, `monitoring`, `onboarding`
- Chaque sous-dossier contient des exemples Node.js et Python, un README, des points d'entrée (`__init__.js`, `__init__.py`)
- Un fichier `index.js` permet l'import centralisé de tous les samples Node.js

## Utilisation de l'index modulaire
```js
import * as samples from './index.js';
samples.api.runApiSample();
samples.audit.runAuditSample();
// ...etc.
```

## Exemple rapide
```js
// Exemple d’utilisation d’un helper Node.js
import { apiHello } from '../api/api_helper.js';
console.log(apiHello());
```

## Utilisation Python
```python
from ..api.api_helper import api_nodejs_hello
print(api_nodejs_hello())
```

---

> Ajoutez ici vos propres exemples d’intégration avancée pour chaque domaine métier.
