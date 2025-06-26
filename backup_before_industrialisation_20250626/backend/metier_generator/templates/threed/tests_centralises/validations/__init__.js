// Point d'entrée pour les tests de validation d'asset (Node.js)
// Permet d'importer tous les tests du dossier validations

module.exports = {
  testThreedAssetValidation: require('./test_threed_asset_validation'),
  ...require('./test_validations')
};
