// Initialisation avancée des validations métier (Node.js)
// Découverte et export automatique des fonctions de validation du dossier

const { validateAsset } = require('./asset_validation');

/**
 * Exporte toutes les fonctions de validation métier du dossier
 * @module validations
 */
module.exports = {
  validateAsset
};

/**
 * Exemple d'utilisation :
 * const { validateAsset } = require('./validations');
 * const result = validateAsset({ id: 1, name: 'Ordinateur' });
 * console.log(result);
 */
