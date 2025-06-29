// Initialisation avancée des fonctions sécurité métier (Node.js)
// Export harmonisé de la fonction RGPD

const { checkRgpd } = require('./rgpd');

/**
 * Exporte la fonction de vérification RGPD
 * @module security
 */
module.exports = {
  checkRgpd
};

/**
 * Exemple d'utilisation :
 * const { checkRgpd } = require('./security');
 * const result = checkRgpd({ user: 'Alice' });
 * console.log(result);
 */
