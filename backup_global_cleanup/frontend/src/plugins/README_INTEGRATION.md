# README_INTEGRATION.md – Plugins

## Exemple d’intégration
```js
import { analytics } from './analytics.js';
import { monitoring } from './monitoring.js';
import { ia } from './ia.js';
import { rgpd } from './rgpd.js';
```

## Flux utilisateur complet
1. Activation d’un plugin via PluginManager
2. Utilisation métier (ex : export PDF, analytics, paiement, monitoring, IA, RGPD)
3. Respect RGPD, accessibilité, i18n, sécurité à chaque étape
