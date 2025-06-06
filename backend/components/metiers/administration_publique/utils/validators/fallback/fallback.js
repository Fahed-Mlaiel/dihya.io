// fallback.js
// Fallback validator JS pour Threed – exemple clé en main

/**
 * Fallback minimal : valide toujours (utilisé en cas d'échec du vrai validateur)
 * @param {*} value
 * @returns {boolean}
 */
function validatorFallback(value) {
  return true;
}

module.exports = { validatorFallback };
