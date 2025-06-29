// fallback.js
// Fallback d'audit JS pour voice – exemple clé en main

/**
 * Fallback minimal : log d'audit en mémoire si la persistance échoue
 * @param {string} action
 * @param {object} details
 * @returns {object}
 */
const fallbackLogs = [];
function auditFallback(action, details = {}) {
  const log = {
    timestamp: new Date().toISOString(),
    action,
    ...details
  };
  fallbackLogs.push(log);
  return log;
}

module.exports = { auditFallback, fallbackLogs };
