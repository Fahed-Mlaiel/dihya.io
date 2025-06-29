# Feature : Plugins

Ce dossier gère l’intégration, l’installation et la gestion des plugins mobile.

## Composants
- PluginInstaller.jsx : UI d’installation de plugins
- PluginManager.jsx : UI de gestion des plugins installés
- PluginExample.jsx : exemple d’intégration de plugin

## Cas d’usage
- Installation d’un plugin
- Activation/désactivation
- Gestion dynamique des plugins

## Flux utilisateur
1. L’utilisateur accède à la gestion des plugins
2. Installe ou active un plugin

## Exemples d’intégration
```jsx
import PluginManager from './PluginManager';
<PluginManager />
```

## Schéma d’architecture
[PluginManager] → [PluginInstaller] → [PluginExample]

## À faire
- Ajouter des exemples d’intégration réelle
- Ajouter des hooks/services pour la gestion dynamique
