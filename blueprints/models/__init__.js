// Initialisation avancée des modèles métier (Node.js)
// Découverte et export automatique de tous les modèles du dossier

const { AssetModel } = require('./asset_model');

/**
 * Exporte tous les modèles métier du dossier
 * @module models
 */
module.exports = {
  AssetModel
};

/**
 * Exemple d'utilisation :
 * const { AssetModel } = require('./models');
 * const model = new AssetModel('Ordinateur');
 * console.log(model.serialize());
 */
