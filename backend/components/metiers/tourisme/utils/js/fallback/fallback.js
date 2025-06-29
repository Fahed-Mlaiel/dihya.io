// fallback.js
// Fallback JS pour Tourisme – exemple clé en main

/**
 * Retourne une valeur par défaut si la fonction échoue
 * @param {Function} fn
 * @param {*} defaultValue
 * @returns {*}
 */
function jsFallback(fn, defaultValue) {
  try {
    return fn();
  } catch {
    return defaultValue;
  }
}

module.exports = { jsFallback };
