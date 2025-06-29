// metrics_helper.js
// Helper metrics JS pour Banque_Finance – exemple clé en main

/**
 * Calcule la moyenne d'un tableau de valeurs numériques
 * @param {number[]} values
 * @returns {number}
 */
function average(values) {
  if (!Array.isArray(values) || values.length === 0) return 0;
  return values.reduce((a, b) => a + b, 0) / values.length;
}

module.exports = { average };
