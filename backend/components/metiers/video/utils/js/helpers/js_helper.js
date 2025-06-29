// js_helper.js
// Helper JS générique pour Video – exemple clé en main

/**
 * Capitalise la première lettre d'une chaîne
 * @param {string} str
 * @returns {string}
 */
function capitalizeFirst(str) {
  if (!str) return '';
  return str.charAt(0).toUpperCase() + str.slice(1);
}

module.exports = { capitalizeFirst };
