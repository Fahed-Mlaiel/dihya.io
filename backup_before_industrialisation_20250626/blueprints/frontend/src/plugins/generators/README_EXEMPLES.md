# README_EXEMPLES.md – Plugins Generators (Lead Dev)

## Exemples d’intégration avancés

### Génération de code métier (conforme au cahier des charges)
```js
import { codeGenerator } from './codeGenerator.js';
const code = codeGenerator({ name: 'User', type: 'model', rgpd: true });
console.log('Code généré:', code);
```

### Scaffolding de template multi-stack
```js
import { templateScaffolder } from './templateScaffolder.js';
const scaffold = templateScaffolder({ type: 'dashboard', stack: 'react', i18n: true });
console.log('Template scaffoldé:', scaffold);
```

### Génération automatisée clé en main
```js
import { codeGenerator } from './codeGenerator.js';
import { templateScaffolder } from './templateScaffolder.js';
const code = codeGenerator({ name: 'Project', type: 'service', rgpd: true });
const scaffold = templateScaffolder({ type: 'crm', stack: 'node', i18n: true });
// Intégration directe dans le pipeline CI/CD ou onboarding
```
