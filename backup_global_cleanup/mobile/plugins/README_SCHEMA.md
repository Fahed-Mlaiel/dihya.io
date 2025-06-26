# README_SCHEMA.md – Plugins

## Schéma d’architecture (ASCII)
```
[PluginManager] → [pluginLoader] → [plugins métiers]
   |                  |
[analytics]      [stripe]
[cms]            [webhook]
[monitoring]     [ia]
[rgpd]
```

## Conventions
- Un plugin = une fonctionnalité métier autonome
- Documenté, versionné, typé, sans placeholder
- README_ARCHITECTURE.md pour la structure, conventions, exemples d’intégration
- Respect RGPD, accessibilité, i18n, sécurité

## Exemples d’intégration réels
```js
import { analytics } from './analytics.js';
import { monitoring } from './monitoring.js';
import { ia } from './ia.js';
import { rgpd } from './rgpd.js';
```

## Cas métier réels
- Export PDF, analytics RGPD, gestion CMS, paiement Stripe, webhooks, monitoring, IA, anonymisation RGPD, gestion dynamique
