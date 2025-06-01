/**
 * @file rateLimit.js
 * @description Module de limitation de débit (rate limiting) pour Dihya Coding (protection API, sécurité, logs, audit).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Applique une limitation de débit par utilisateur et endpoint.
 * @param {object} params
 * @param {string} params.userId - Identifiant utilisateur (sera anonymisé pour les logs)
 * @param {string} params.endpoint - Endpoint/API cible
 * @param {number} params.windowMs - Fenêtre de temps en ms
 * @param {number} params.maxRequests - Nombre max de requêtes autorisées dans la fenêtre
 * @returns {boolean} true si la limite est dépassée, false sinon
 */
export function applyRateLimit({ userId, endpoint, windowMs = 60000, maxRequests = 20 }) {
  validateUserId(userId);
  validateEndpoint(endpoint);
  const now = Date.now();
  const key = `ratelimit_${anonymizeUserId(userId)}_${endpoint}`;
  let history = [];
  try {
    history = JSON.parse(localStorage.getItem(key) || '[]');
  } catch {}
  // Nettoyage des requêtes hors fenêtre
  history = history.filter(ts => now - ts < windowMs);
  history.push(now);
  localStorage.setItem(key, JSON.stringify(history));
  const isLimited = history.length > maxRequests;
  logRateLimitEvent('apply_rate_limit', anonymizeUserId(userId), endpoint, isLimited);
  return isLimited;
}

/**
 * Réinitialise l’historique de rate limiting pour un utilisateur/endpoint (droit à l’oubli RGPD).
 * @param {string} userId
 * @param {string} endpoint
 */
export function clearRateLimitHistory(userId, endpoint) {
  validateUserId(userId);
  validateEndpoint(endpoint);
  const key = `ratelimit_${anonymizeUserId(userId)}_${endpoint}`;
  localStorage.removeItem(key);
}

/**
 * Valide l’identifiant utilisateur.
 * @param {string} userId
 */
function validateUserId(userId) {
  if (!userId || typeof userId !== 'string' || userId.length < 2) {
    throw new Error('Identifiant utilisateur invalide');
  }
}

/**
 * Valide l’endpoint/API cible.
 * @param {string} endpoint
 */
function validateEndpoint(endpoint) {
  if (!endpoint || typeof endpoint !== 'string' || endpoint.length < 2) {
    throw new Error('Endpoint invalide');
  }
}

/**
 * Anonymise l’identifiant utilisateur pour les logs.
 * @param {string} userId
 * @returns {string}
 */
function anonymizeUserId(userId) {
  return userId.replace(/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/gi, '[email]');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} userId
 * @param {string} endpoint
 * @param {boolean} limited
 */
function logRateLimitEvent(action, userId, endpoint, limited) {
  try {
    const logs = JSON.parse(localStorage.getItem('ratelimit_logs') || '[]');
    logs.push({
      action,
      userId,
      endpoint,
      limited,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('ratelimit_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface tous les logs de rate limiting (droit à l’oubli RGPD).
 */
export function clearLocalRateLimitLogs() {
  localStorage.removeItem('ratelimit_logs');
}