// sample_audit.js
// Exemple d’intégration avancée pour l’audit

const { logEvent, alertOnSuspiciousActivity } = require('./helpers_audit');

logEvent('LOGIN', { user: 'Alice', status: 'success' });
const alert = alertOnSuspiciousActivity({ level: 'high', action: 'delete' });
console.log(alert);
