// fallback.js
// Fallback helper JS pour Ressources_humaines – exemple clé en main

/**
 * Fallback minimal : retourne une valeur par défaut si la fonction échoue
 * @param {Function} fn
 * @param {*} defaultValue
 * @returns {*}
 */
function fallbackHelper(fn, defaultValue) {
  try {
    return fn();
  } catch {
    return defaultValue;
  }
}

module.exports = { fallbackHelper };
