// fallback.js
// Fallback JS pour Threed – exemple clé en main

/**
 * Retourne une valeur par défaut si la fonction échoue
 * @param {Function} fn
 * @param {*} defaultValue
 * @returns {*}
 */
// eslint-disable-next-line no-unused-vars
function jsFallback(fn, defaultValue) {
  try {
    return fn();
  } catch (e) {
    // eslint-disable-next-line no-unused-vars
    return defaultValue;
  }
}

module.exports = { jsFallback };
