# README_EXEMPLES.md – Plugins Audit (Lead Dev)

## Exemples d’intégration avancés

### Audit des accès (RGPD, sécurité)
```js
import { accessLogger } from './accessLogger.js';
const log = accessLogger('login', 'Amina');
console.log('Log structuré:', log);
```

### Export des logs d’audit (reporting clé en main)
```js
import { exportAudit } from './exportAudit.js';
const logs = [
  { date: '2025-06-18', user: 'Amina', action: 'login' },
  { date: '2025-06-19', user: 'Yanis', action: 'export' }
];
const csv = exportAudit(logs);
console.log('Export CSV:', csv);
```

### Audit automatique industrialisé
```js
import { accessLogger } from './accessLogger.js';
import { exportAudit } from './exportAudit.js';
const logs = [accessLogger('login', 'Amina'), accessLogger('export', 'Yanis')];
const csv = exportAudit(logs);
// Envoi du CSV à un service de monitoring ou backup
```
