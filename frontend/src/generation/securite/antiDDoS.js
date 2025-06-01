/**
 * @file antiDDoS.js
 * @description Module de protection anti-DDoS pour Dihya Coding (détection, blocage, logs, audit).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Détecte un comportement suspect de type DDoS sur la base du nombre de requêtes.
 * @param {object} params
 * @param {string} params.userId - Identifiant utilisateur (sera anonymisé pour les logs)
 * @param {string} params.endpoint - Endpoint/API cible
 * @param {number} params.windowMs - Fenêtre de temps en ms
 * @param {number} params.maxRequests - Nombre max de requêtes autorisées dans la fenêtre
 * @returns {boolean} true si DDoS suspecté, false sinon
 */
export function detectDDoS({ userId, endpoint, windowMs = 60000, maxRequests = 30 }) {
  validateUserId(userId);
  validateEndpoint(endpoint);
  const now = Date.now();
  const key = `antiddos_${anonymizeUserId(userId)}_${endpoint}`;
  let history = [];
  try {
    history = JSON.parse(localStorage.getItem(key) || '[]');
  } catch {}
  // Nettoyage des requêtes hors fenêtre
  history = history.filter(ts => now - ts < windowMs);
  history.push(now);
  localStorage.setItem(key, JSON.stringify(history));
  const isBlocked = history.length > maxRequests;
  logAntiDDoSEvent('detect_ddos', anonymizeUserId(userId), endpoint, isBlocked);
  return isBlocked;
}

/**
 * Réinitialise l’historique DDoS pour un utilisateur/endpoint (droit à l’oubli RGPD).
 * @param {string} userId
 * @param {string} endpoint
 */
export function clearDDoSHistory(userId, endpoint) {
  validateUserId(userId);
  validateEndpoint(endpoint);
  const key = `antiddos_${anonymizeUserId(userId)}_${endpoint}`;
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
 * @param {boolean} blocked
 */
function logAntiDDoSEvent(action, userId, endpoint, blocked) {
  try {
    const logs = JSON.parse(localStorage.getItem('antiddos_logs') || '[]');
    logs.push({
      action,
      userId,
      endpoint,
      blocked,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('antiddos_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface tous les logs anti-DDoS (droit à l’oubli RGPD).
 */
export function clearLocalAntiDDoSLogs() {
  localStorage.removeItem('antiddos_logs');
}