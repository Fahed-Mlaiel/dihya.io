// helper_validators.js
// Ultra-avancé, clé en main : helpers de validation pour les fixtures/metiers/transport

/**
 * Valide si une valeur est un entier positif.
 * @param {any} value
 * @returns {boolean}
 */
function isPositiveInteger(value) {
  return Number.isInteger(value) && value > 0;
}

/**
 * Valide si une chaîne est un email valide.
 * @param {string} email
 * @returns {boolean}
 */
function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

/**
 * Valide si un objet possède toutes les clés requises.
 * @param {object} obj
 * @param {string[]} requiredKeys
 * @returns {boolean}
 */
function hasRequiredKeys(obj, requiredKeys) {
  return requiredKeys.every(key => Object.prototype.hasOwnProperty.call(obj, key));
}

/**
 * Valide si une valeur est une chaîne non vide.
 * @param {any} value
 * @returns {boolean}
 */
function isNonEmptyString(value) {
  return typeof value === 'string' && value.trim().length > 0;
}

/**
 * Valide si un tableau ne contient que des entiers positifs.
 * @param {any[]} arr
 * @returns {boolean}
 */
function isArrayOfPositiveIntegers(arr) {
  return Array.isArray(arr) && arr.every(isPositiveInteger);
}

module.exports = {
  isPositiveInteger,
  isValidEmail,
  hasRequiredKeys,
  isNonEmptyString,
  isArrayOfPositiveIntegers,
};
