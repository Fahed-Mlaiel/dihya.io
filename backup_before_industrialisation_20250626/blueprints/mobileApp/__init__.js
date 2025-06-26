// Initialisation avancée des blueprints mobileApp (Node.js)
// Export harmonisé de la fonction de génération d'app mobile

const { generateMobileApp } = require('./mobileApp');

/**
 * Exporte la fonction de génération d'app mobile
 * @module mobileApp
 */
module.exports = {
  generateMobileApp
};

/**
 * Exemple d'utilisation :
 * const { generateMobileApp } = require('./mobileApp');
 * const code = generateMobileApp({ metier: 'Inventaire', textes: { fr: { titre: 'Inventaire Mobile' } }, composants: {} });
 * console.log(code);
 */
