// Blueprint plugin d’audit (Node.js)
// Exemples de hooks, extension, instructions d’extension

function auditPlugin(config) {
  return function logAction(action) {
    if (config && config.enabled) {
      console.log('[AUDIT]', action);
    }
    return true;
  };
}

module.exports = auditPlugin;
