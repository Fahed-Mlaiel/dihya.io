// js_core.js
// Fonction utilitaire JS principale pour Health – exemple clé en main

/**
 * Vérifie si une valeur est un objet pur (plain object)
 * @param {*} value
 * @returns {boolean}
 */
function isPlainObject(value) {
  return Object.prototype.toString.call(value) === '[object Object]';
}

module.exports = { isPlainObject };
