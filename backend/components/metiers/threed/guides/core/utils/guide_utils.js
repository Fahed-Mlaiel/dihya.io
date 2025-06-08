// guide_utils.js - Guide d'utilisation avancée des utilitaires Threed (JS)

/**
 * Ce fichier documente les helpers JS, les patterns de validation, de formatage et de clonage utilisés dans Threed.
 *
 * Exemples :
 *   - deepClone
 *   - formatDate
 *   - isObject
 */

module.exports = {
  doc: 'Voir README_ADVANCED.md pour les exemples détaillés.'
};

/**
 * Exemples avancés :
 *
 * // Formatage de date
 * const { formatDate } = require('../utils/utils_helper');
 * formatDate(Date.now());
 *
 * // Validation d'objet
 * const { isObject } = require('../utils/utils_helper');
 * isObject({ foo: 'bar' });
 *
 * // Clonage profond
 * const { deepClone } = require('../utils/utils_helper');
 * deepClone({ a: 1 });
 */
