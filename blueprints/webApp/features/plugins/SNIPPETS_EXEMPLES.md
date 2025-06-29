# Exemples de snippets pour les plugins

## Charger et activer un plugin

```js
import { PluginManager } from './PluginManager';
const manager = new PluginManager();
manager.load('cms');
manager.activate('cms');
```

## Installer un plugin

```js
import { PluginInstaller } from './PluginInstaller';
const installer = new PluginInstaller();
installer.install('stripe');
```
