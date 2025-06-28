// fallback.js
// Fallback d'export JS pour Social – exemple clé en main

/**
 * Fallback minimal : export en mémoire si la persistance échoue
 * @param {object} data
 * @returns {object}
 */
const fallbackExports = [];
function exportFallback(data) {
  const exportObj = {
    timestamp: new Date().toISOString(),
    ...data
  };
  fallbackExports.push(exportObj);
  return exportObj;
}

module.exports = { exportFallback, fallbackExports };
