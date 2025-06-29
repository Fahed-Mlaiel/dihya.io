// exporter_helper.js
// Helper d'export JS pour Culture – exemple clé en main

/**
 * Formate les données à exporter en JSON compacté
 * @param {object} data
 * @returns {string}
 */
function formatExportJSON(data) {
  return JSON.stringify(data);
}

module.exports = { formatExportJSON };
