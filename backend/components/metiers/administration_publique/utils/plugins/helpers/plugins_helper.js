// plugins_helper.js
// Helper plugins JS pour Threed – exemple clé en main

/**
 * Valide le nom d'un plugin (alphanumérique, tirets, underscores)
 * @param {string} name
 * @returns {boolean}
 */
function isValidPluginName(name) {
  return /^[a-zA-Z0-9_-]+$/.test(name);
}

module.exports = { isValidPluginName };
