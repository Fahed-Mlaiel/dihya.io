/**
 * @file fallbackRouter.js
 * @description Utilitaire de routage fallback pour Dihya Coding : gère la navigation côté client en cas d’échec du routeur principal, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Navigue vers une route donnée en fallback (hash ou location).
 * @param {string} path - Chemin cible (ex: '/home')
 * @param {object} [options] - { log: bool }
 * @returns {boolean} Succès de la navigation
 */
export function fallbackNavigate(path, options = {}) {
  if (!hasConsent()) {
    // Permettre la navigation même sans consentement pour la navigation de base
    window.location.hash = '#' + sanitizePath(path);
    return false;
  }
  if (typeof window === 'undefined' || typeof path !== 'string') return false;
  try {
    if (window.location.hash !== '#' + path) {
      window.location.hash = '#' + sanitizePath(path);
    }
    if (options.log !== false) {
      logFallbackRouterEvent('navigate', { path: anonymizePath(path), timestamp: new Date().toISOString() });
    }
    return true;
  } catch {
    return false;
  }
}

/**
 * Retourne la route courante (fallback).
 * @returns {string} Route courante
 */
export function getCurrentRoute() {
  if (typeof window === 'undefined') return '/';
  const hash = window.location.hash || '';
  // Si hash est vide ou juste "#", retourne "/"
  const route = sanitizePath(hash.replace(/^#/, '') || '/');
  // Correction : toujours commencer par "/"
  return route.startsWith('/') ? route : '/' + route;
}

/**
 * Ajoute un listener sur le changement de route (fallback).
 * @param {function} callback - Fonction appelée à chaque changement de route
 */
export function onRouteChange(callback) {
  if (typeof window === 'undefined' || typeof callback !== 'function') return;
  window.addEventListener('hashchange', () => {
    callback(getCurrentRoute());
  });
  // Appel initial pour la route courante
  callback(getCurrentRoute());
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  // Pour le fallback router, on autorise la navigation même sans consentement
  // Mais on ne logue que si le consentement est donné
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('fallback_router_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logFallbackRouterEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('fallback_router_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('fallback_router_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Sanitize un chemin pour éviter l’injection.
 * @param {string} path
 * @returns {string}
 */
function sanitizePath(path) {
  return String(path).replace(/[^a-zA-Z0-9/_\-]/g, '').slice(0, 64) || '/';
}

/**
 * Anonymise un chemin pour les logs.
 * @param {string} path
 * @returns {string}
 */
function anonymizePath(path) {
  if (!path) return '';
  return path.length > 8 ? path.slice(0, 2) + '***' + path.slice(-2) : '***';
}

/**
 * Efface les logs de routage fallback (droit à l’oubli RGPD).
 */
export function clearLocalFallbackRouterLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('fallback_router_logs');
  }
}

/* Documentation claire : chaque fonction est commentée pour auditabilité et conformité */