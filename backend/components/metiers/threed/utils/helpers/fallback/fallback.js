// fallback.js
// Fallback helper JS pour Threed – exemple clé en main

/**
 * Fallback minimal : retourne une valeur par défaut si la fonction échoue
 * @param {Function} fn
 * @param {*} defaultValue
 * @returns {*}
 */
// eslint-disable-next-line no-unused-vars
function fallbackHelper(fn, defaultValue) {
  try {
    return fn();
  } catch (e) {
    // eslint-disable-next-line no-unused-vars
    return defaultValue;
  }
}

module.exports = { fallbackHelper };
