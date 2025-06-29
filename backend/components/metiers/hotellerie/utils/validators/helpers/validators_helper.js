// validators_helper.js
// Ultra-avancé, clé en main : helpers pour la validation métier et technique des données plugins/hotellerie

/**
 * Valide qu’un objet possède toutes les clés requises et que leurs valeurs ne sont pas nulles ou vides.
 * @param {object} obj
 * @param {string[]} requiredKeys
 * @returns {boolean}
 */
function hasValidKeys(obj, requiredKeys) {
  if (!obj || typeof obj !== 'object') return false;
  return requiredKeys.every(key => obj[key] !== undefined && obj[key] !== null && obj[key] !== '');
}

/**
 * Valide qu’une chaîne est un identifiant métier valide (alphanumérique, tirets, min 3 caractères).
 * @param {string} id
 * @returns {boolean}
 */
function isValidBusinessId(id) {
  return typeof id === 'string' && /^[a-zA-Z0-9\-]{3,}$/.test(id);
}

/**
 * Valide qu’un tableau ne contient que des objets valides selon un validateur fourni.
 * @param {Array} arr
 * @param {Function} validator
 * @returns {boolean}
 */
function isArrayOfValidObjects(arr, validator) {
  return Array.isArray(arr) && arr.every(validator);
}

/**
 * Valide qu’une valeur est un booléen strict.
 * @param {any} value
 * @returns {boolean}
 */
function isStrictBoolean(value) {
  return value === true || value === false;
}

module.exports = {
  hasValidKeys,
  isValidBusinessId,
  isArrayOfValidObjects,
  isStrictBoolean,
};
