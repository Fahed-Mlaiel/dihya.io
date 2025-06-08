# plugins – Tests centralisés Threed

## Structure et logique
Ce dossier contient uniquement les tests ultra avancés pour les plugins existants dans le module métier Threed. Il respecte la structure réelle : core, helpers, samples. Aucun test ne cible un module inexistant ou non métier.

- Découverte automatique via `__init__.js` et `__init__.py`
- Parité JS/Python, documentation, CI/CD
- Respect strict de la logique métier et de la structure réelle du code source

## Structure actuelle
- `core/` : Tests pour les plugins cœur métier
- `helpers/` : Tests pour les helpers plugins
- `samples/` : Tests pour les samples plugins

## Exécution
- **JS** : Utiliser `npm test` ou exécuter via l’`index.js` parent
- **Python** : `pytest`

## CI/CD
- Intégration complète dans les pipelines existants
- Synchronisation automatique JS/Python
- Aucun test ne cible un module inexistant (ex : plugin_manager)
