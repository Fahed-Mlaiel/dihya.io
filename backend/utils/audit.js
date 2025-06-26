/**
 * 🚀 DIHYA.IO - UTILITAIRES D'AUDIT
 * Logging des actions sensibles pour conformité
 */

/**
 * Log d'audit pour actions sensibles
 */
const logAudit = (action, userId, details = {}) => {
  const auditLog = {
    timestamp: new Date().toISOString(),
    action,
    userId,
    details,
    ip: details.ip || 'unknown',
    userAgent: details.userAgent || 'unknown'
  };

  // En production : envoyer vers un service de logging sécurisé
  console.log('🔍 AUDIT:', JSON.stringify(auditLog));

  // TODO: Intégrer avec un vrai système d'audit (Splunk, ELK, etc.)
};

module.exports = {
  logAudit
};
