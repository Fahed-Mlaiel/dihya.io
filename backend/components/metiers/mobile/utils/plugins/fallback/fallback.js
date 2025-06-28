// fallback.js
// Fallback plugin JS pour Mobile – exemple clé en main

/**
 * Fallback minimal : plugin de secours qui log l'appel
 * @param {string} name
 * @returns {string}
 */
function pluginFallback(name) {
  return `[PLUGIN-FALLBACK] Appel du plugin: ${name}`;
}

module.exports = { pluginFallback };
