// logger_helper.js
// Helper logger JS pour Mode – exemple clé en main

/**
 * Formate un message de log avec niveau et timestamp
 * @param {string} level
 * @param {string} message
 * @returns {string}
 */
function formatLog(level, message) {
  return `[${level.toUpperCase()}][${new Date().toISOString()}] ${message}`;
}

module.exports = { formatLog };
