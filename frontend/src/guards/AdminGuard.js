/**
 * @file AdminGuard.js
 * @description Garde d’accès pour routes/admins dans Dihya Coding.
 * Garantit sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les vérifications sont strictes, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Vérifie si l’utilisateur courant a les droits administrateur pour accéder à une route protégée.
 * @param {object} user - Objet utilisateur (doit contenir au minimum { id, roles })
 * @param {object} [options]
 * @param {boolean} [options.log=true] - Active le log local pour auditabilité
 * @returns {boolean} true si accès autorisé, sinon false
 */
export function isAdmin(user, options = {}) {
  if (!hasConsent()) throw new Error('Consentement requis pour vérification admin.');
  if (!user || typeof user !== 'object' || !Array.isArray(user.roles)) return false;
  const isAdmin = user.roles.includes('admin');
  if (options.log !== false) {
    logAdminGuardEvent('admin_check', { userId: anonymizeUserId(user.id), isAdmin });
  }
  return isAdmin;
}

/**
 * Middleware/guard pour protéger une route React ou Express.
 * @param {object} user
 * @param {function} onDenied - Callback si accès refusé
 * @param {object} [options]
 * @returns {boolean}
 */
export function adminGuard(user, onDenied, options = {}) {
  const allowed = isAdmin(user, options);
  if (!allowed && typeof onDenied === 'function') {
    onDenied();
  }
  return allowed;
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('admin_guard_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logAdminGuardEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('admin_guard_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString(),
    });
    window.localStorage.setItem('admin_guard_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise un userId pour les logs.
 * @param {string|number} userId
 * @returns {string}
 */
function anonymizeUserId(userId) {
  if (!userId) return '';
  const str = String(userId);
  return str.length > 4 ? str.slice(0, 2) + '***' + str.slice(-2) : '***';
}

/**
 * Efface les logs de garde admin (droit à l’oubli RGPD).
 */
export function clearLocalAdminGuardLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('admin_guard_logs');
  }
}