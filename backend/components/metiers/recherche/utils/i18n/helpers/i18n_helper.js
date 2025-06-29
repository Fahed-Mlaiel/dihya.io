// i18n_helper.js
// Helper i18n JS pour Recherche – exemple clé en main

/**
 * Transforme une clé i18n en format lisible (ex: 'HELLO_WORLD' => 'Hello world')
 * @param {string} key
 * @returns {string}
 */
function humanizeKey(key) {
  if (!key) return '';
  return key.replace(/_/g, ' ').toLowerCase().replace(/^\w/, c => c.toUpperCase());
}

module.exports = { humanizeKey };
