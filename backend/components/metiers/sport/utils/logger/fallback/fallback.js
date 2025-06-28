// fallback.js
// Fallback logger JS pour Sport – exemple clé en main

/**
 * Fallback minimal : log en mémoire si la persistance échoue
 * @param {string} message
 * @returns {object}
 */
const fallbackLogs = [];
function loggerFallback(message) {
  const log = {
    timestamp: new Date().toISOString(),
    message
  };
  fallbackLogs.push(log);
  return log;
}

module.exports = { loggerFallback, fallbackLogs };
