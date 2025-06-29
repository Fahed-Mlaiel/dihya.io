# Scripts Métier Blockchain

Ce dossier regroupe tous les scripts métiers avancés pour la gestion, l’audit, le déploiement, la migration et le monitoring des assets et smart contracts blockchain du projet Dihya.io.

## Structure
- `index.js` : Point d’entrée, centralise les exports.
- `deploy.js` : Déploiement avancé d’assets et de smart contracts.
- `audit.js` : Audit métier, conformité, scoring et rapports détaillés.
- `migrate.js` : Migration de données et de contrats.
- `monitor.js` : Monitoring, alerting, logs et santé des scripts.
- `helpers.js` : Fonctions utilitaires réutilisables.

## Extension
Ajoutez vos scripts métiers dans ce dossier, exportez-les via `index.js` et documentez chaque fonction.

## Exemples d’usage
```js
const { deployAsset, auditAsset } = require('./scripts');
const result = deployAsset({ id: 'nft-001', type: 'NFT' });
```

## Bonnes pratiques
- Toujours valider les entrées.
- Gérer les erreurs de façon explicite.
- Documenter chaque fonction métier.
