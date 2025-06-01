/**
 * @file RouteGuard.js
 * @description Garde d’accès générique pour routes dans Dihya Coding (authentification, rôles, permissions).
 * Garantit sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les vérifications sont strictes, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Vérifie si l’utilisateur courant a accès à une route selon les rôles et permissions requis.
 * @param {object} user - Objet utilisateur (doit contenir au minimum { id, roles })
 * @param {object} route - Objet route (doit contenir { requiredRoles?: string[], requiredPermissions?: string[] })
 * @param {object} [options]
 * @param {boolean} [options.log=true] - Active le log local pour auditabilité
 * @returns {boolean} true si accès autorisé, sinon false
 */
export function canAccessRoute(user, route, options = {}) {
  if (!hasConsent()) throw new Error('Consentement requis pour vérification de route.');
  if (!user || typeof user !== 'object' || !Array.isArray(user.roles)) return false;
  if (!route || typeof route !== 'object') return false;

  let allowed = true;

  if (Array.isArray(route.requiredRoles) && route.requiredRoles.length > 0) {
    allowed = route.requiredRoles.some(role => user.roles.includes(role));
  }

  if (allowed && Array.isArray(route.requiredPermissions) && route.requiredPermissions.length > 0) {
    allowed = route.requiredPermissions.every(perm => Array.isArray(user.permissions) && user.permissions.includes(perm));
  }

  if (options.log !== false) {
    logRouteGuardEvent('route_check', {
      userId: anonymizeUserId(user.id),
      route: anonymizeRoute(route),
      allowed
    });
  }
  return allowed;
}

/**
 * Middleware/guard pour protéger une route React ou Express.
 * @param {object} user
 * @param {object} route
 * @param {function} onDenied - Callback si accès refusé
 * @param {object} [options]
 * @returns {boolean}
 */
export function routeGuard(user, route, onDenied, options = {}) {
  const allowed = canAccessRoute(user, route, options);
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
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('route_guard_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logRouteGuardEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('route_guard_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString(),
    });
    window.localStorage.setItem('route_guard_logs', JSON.stringify(logs));
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
 * Anonymise une route pour les logs.
 * @param {object} route
 * @returns {object}
 */
function anonymizeRoute(route) {
  if (!route || typeof route !== 'object') return {};
  const clone = { ...route };
  if (clone.path) clone.path = clone.path.replace(/[^a-zA-Z0-9/_-]/g, '');
  if (clone.requiredRoles) clone.requiredRoles = clone.requiredRoles.map(() => '[role]');
  if (clone.requiredPermissions) clone.requiredPermissions = clone.requiredPermissions.map(() => '[perm]');
  return clone;
}

/**
 * Efface les logs de garde de route (droit à l’oubli RGPD).
 */
export function clearLocalRouteGuardLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('route_guard_logs');
  }
}