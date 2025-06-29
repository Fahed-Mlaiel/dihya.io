# Architecture des Plugins

Ce document décrit l’architecture, les conventions, les schémas et les exemples d’intégration du système de plugins.

## Schéma d’architecture

```ascii
+-------------------+
|   PluginManager   |
+-------------------+
         |
+-------------------+
|  PluginInstaller  |
+-------------------+
         |
+-------------------+
|   Plugins (ex:    |
|  analytics, CMS,  |
|  stripe, webhook) |
+-------------------+
```

## Conventions
- Tous les plugins sont chargés dynamiquement via `PluginManager`.
- L’installation se fait via `PluginInstaller`.
- Chaque plugin expose une interface standardisée (init, activate, deactivate, config, etc.).

## Exemples d’intégration

```js
import { PluginManager } from './PluginManager';

const manager = new PluginManager();
manager.load('analytics');
manager.activate('analytics');
```

## Cas d’usage
- Ajout d’un plugin analytics
- Activation/désactivation d’un plugin Stripe
- Gestion de plugins custom via UI
