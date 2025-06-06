# Components – Dihya

Ce dossier regroupe tous les composants métiers, services, utilitaires et APIs du backend Dihya.

## Structure professionnelle de référence
- `api/` : Points d'entrée API, contrôleurs, routes, middlewares, hooks, etc.
- `services/` : Services métier, helpers, implémentations, fallback, samples, etc.
- `tests/` : Tests unitaires, d'intégration, de conformité, etc.
- `utils/` : Utilitaires transverses, helpers, validateurs, etc.
- `plugins/` : Plugins métiers, extensions, connecteurs, etc.
- `migrations/` : Scripts de migration de données ou de schéma.
- `fixtures/` : Données de test, mocks, helpers de fixtures.
- `views/` : Vues, templates, rendering, etc.
- `guides/` : Guides d'utilisation, documentation technique, etc.
- `README.md` : Documentation d'ensemble du dossier components.
- `index.js` : Point d'entrée principal JS pour l'import global.

## Bonnes pratiques
- Respect strict du cahier des charges métier.
- Synchronisation et harmonisation des points d'entrée.
- Structure modulaire, scalable, testée et prête pour CI/CD.
- Aucun doublon, aucune redondance, tout est centralisé et documenté.
