# Legacy Threed – Documentation Ultra Avancée (JS)

Ce dossier contient :
- Mocks pour tests unitaires legacy (JS)
- Helpers et validateurs JS
- Exemples de migration, validation, audit
- Bonnes pratiques pour la gestion de l’historique et la traçabilité

## Exemples JS
```js
const { migrateLegacyModel } = require('./legacy_migration');
const migrated = migrateLegacyModel({ legacy_id: 'old-1', legacy_name: 'AncienCube' });
```

## Bonnes pratiques
- Toujours tracer la source et la date de migration
- Valider la structure avant conversion
- Documenter les différences de schéma entre legacy et nouveau format
