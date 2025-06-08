# Nettoyage des tests centralisés plugins

## Suppression des tests non métier

Les fichiers suivants ne correspondent à aucun module métier existant dans `/plugins` :
- `plugin_manager.test.js`
- `plugin_manager.test.py`

Ils sont supprimés pour garantir la conformité à la logique métier, la clarté et la robustesse de la démarche de tests centralisés.
