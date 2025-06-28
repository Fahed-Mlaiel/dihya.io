// audit_helper.js
// Helper d'audit JS pour Mobile – exemple clé en main

/**
 * Génère un log d'audit structuré pour une action métier
 * @param {string} action
 * @param {object} details
 * @returns {object}
 */
function generateAuditLog(action, details = {}) {
  return {
    timestamp: new Date().toISOString(),
    action,
    ...details
  };
}

module.exports = { generateAuditLog };
