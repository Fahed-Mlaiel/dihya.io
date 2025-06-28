// fallback.js
// Fallback validator JS pour Immobilier – exemple clé en main

/**
 * Fallback minimal : valide toujours (utilisé en cas d'échec du vrai validateur)
 * @param {*} value
 * @returns {boolean}
 */
// eslint-disable-next-line no-unused-vars
function validatorFallback(value) {
  return true;
}

module.exports = {
  validatorFallback,
  fallbackValidate: validatorFallback
};
