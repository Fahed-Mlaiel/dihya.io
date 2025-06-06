# README - Plugins Threed

Ce dossier contient les plugins pour le module Threed, en Python et JavaScript.

# Plugins Threed – Documentation Complète

Ce dossier contient :
- Plugins JS et Python ultra avancés (hooks, audit, sécurité, CI/CD)
- Helpers pour l’intégration, l’audit, la traçabilité
- Exemples d’activation, de hooks, de tests unitaires et d’intégration
- Bonnes pratiques pour la sécurité, la traçabilité, la CI/CD

## Exemples JS
```js
const plugin = require('./sample_plugin');
plugin.activate({ user: { role: 'admin' } });
plugin.run({ foo: 'bar' });
console.log(plugin.getAuditTrail());
```

## Exemples Python
```python
from .sample_plugin import SamplePlugin
plugin = SamplePlugin()
plugin.activate({'user': {'role': 'admin'}})
plugin.run({'foo': 'bar'})
print(plugin.get_audit_trail())
```

## Synchronisation JS/Python
- Les helpers et hooks sont disponibles dans les deux langages
- Les tests unitaires couvrent tous les cas métiers

## Bonnes pratiques
- Toujours auditer l’activation/désactivation
- Vérifier la signature des plugins avant activation
- Utiliser les hooks pour la traçabilité et la CI/CD

# Plugins – Threed

Ce module regroupe tous les plugins du domaine 3D, avec une structure ultra professionnelle, modulaire, testée et prête pour CI/CD, audit et documentation automatique.

## Structure du dossier

- `index.js` : Point d'entrée principal JS, centralise l'accès à tous les sous-modules (core, fallback, helpers).
- `index.test.js` : Test d'import du point d'entrée JS.
- `index.test.py` : Test d'import du point d'entrée Python.
- `__init__.js` / `__init__.py` : Points d'entrée pour la découverte automatique (JS/Python).
- `__init__.test.js` / `__init__.test.py` : Tests d'import des points d'entrée.
- `core/` : Plugins principaux (advanced, samples, etc.).
- `fallback/` : Plugins fallback (advanced, core, etc.).
- `helpers/` : Plugins utilitaires et helpers métier.

## core/
Plugins principaux (ex: advanced_plugin, audit_plugin), synchronisés JS/Python, tests, documentation, points d'entrée, CI/CD.

## helpers/
Helpers pour plugins (validation, audit, sécurité, extension), synchronisés JS/Python, tests, documentation, .keep.

## samples/
Exemples d'utilisation, edge cases, synchronisation JS/Python, tests, documentation, .keep.

## Exemples d'utilisation

**JavaScript**
```js
const plugins = require('./index');
const adv = plugins.AdvancedPlugin;
const fallback = plugins.FallbackPlugin;
```

**Python**
```python
from backend.components.metiers.threed.plugins.core.advanced import AdvancedPlugin
from backend.components.metiers.threed.plugins.fallback.advanced import FallbackPlugin
```

## Bonnes pratiques
- Tous les points d'entrée sont testés (JS & Python).
- Synchronisation JS/Python assurée.
- Prêt pour CI/CD, audit et documentation automatique.
- Respect strict de la logique métier et du cahier des charges.

## CI/CD & Documentation
- Les tests sont automatiquement détectés et exécutés.
- La documentation est générée à partir de ce README et des docstrings.

## Conformité
- Structure modulaire, sans doublons, 100% testée, prête pour audit.
- Respect strict des conventions du projet `threed`.
