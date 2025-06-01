/**
 * @file antiDDoS.js
 * @description Utilitaire anti-DDoS pour Dihya Coding : limite les requêtes abusives côté client, protège les endpoints critiques, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont anonymisées, loguées localement, respectent le consentement utilisateur et sont facilement extensibles.
 */

/**
 * Limiteur de requêtes simple (client-side) par clé (ex: endpoint ou action).
 * @param {string} key - Identifiant de l’action ou endpoint à protéger
 * @param {object} [options] - { windowMs: durée fenêtre ms, max: nombre max, log: bool }
 * @returns {boolean} true si la requête est autorisée, false si bloquée
 */
export function rateLimit(key, options = {}) {
  if (!hasConsent()) return false;
  const windowMs = options.windowMs || 60000; // 1 min par défaut
  const max = options.max || 10;
  const now = Date.now();
  const storageKey = `antiddos_${sanitizeKey(key)}`;
  let history = [];
  try {
    history = JSON.parse(window.localStorage.getItem(storageKey) || '[]');
  } catch {
    history = [];
  }
  // Nettoie les anciennes entrées
  history = history.filter(ts => now - ts < windowMs);
  if (history.length >= max) {
    if (options.log !== false) {
      logAntiDDoSEvent('blocked', { key: anonymizeKey(key), count: history.length, timestamp: new Date().toISOString() });
    }
    return false;
  }
  history.push(now);
  window.localStorage.setItem(storageKey, JSON.stringify(history));
  if (options.log !== false) {
    logAntiDDoSEvent('allowed', { key: anonymizeKey(key), count: history.length, timestamp: new Date().toISOString() });
  }
  return true;
}

/**
 * Réinitialise le compteur pour une clé donnée.
 * @param {string} key
 */
export function resetRateLimit(key) {
  if (!hasConsent()) return;
  const storageKey = `antiddos_${sanitizeKey(key)}`;
  window.localStorage.removeItem(storageKey);
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('antiddos_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logAntiDDoSEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('antiddos_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('antiddos_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Sanitize une clé pour éviter l’injection.
 * @param {string} key
 * @returns {string}
 */
function sanitizeKey(key) {
  return String(key).replace(/[^a-zA-Z0-9_\-:.]/g, '').slice(0, 48);
}

/**
 * Anonymise une clé pour les logs.
 * @param {string} key
 * @returns {string}
 */
function anonymizeKey(key) {
  if (!key) return '';
  return key.length > 8 ? key.slice(0, 2) + '***' + key.slice(-2) : '***';
}

/**
 * Efface les logs anti-DDoS (droit à l’oubli RGPD).
 */
export function clearLocalAntiDDoSLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('antiddos_logs');
  }
}

/* Documentation claire : chaque fonction est commentée pour auditabilité et conformité */