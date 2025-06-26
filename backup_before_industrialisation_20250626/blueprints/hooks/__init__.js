// Initialisation avancée des hooks métier (Node.js)
// Découverte et export automatique des hooks du dossier

const { beforeCreate } = require('./asset_hooks');

/**
 * Exporte tous les hooks métier du dossier
 * @module hooks
 */
module.exports = {
  beforeCreate
};

/**
 * Exemple d'utilisation :
 * const { beforeCreate } = require('./hooks');
 * beforeCreate(() => console.log('Avant création d’un asset'));
 */
