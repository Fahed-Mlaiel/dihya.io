/**
 * @file quotaDetector.js
 * @description Module de détection de quota pour l’IA dans Dihya Coding : gestion des limites d’usage, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Vérifie si le quota d’utilisation de l’IA est atteint pour l’utilisateur courant.
 * @param {object} [options]
 * @param {number} [options.maxPerDay=100] - Nombre maximum d’appels autorisés par jour
 * @param {boolean} [options.log=true] - Active le log local pour auditabilité
 * @returns {object} Résultat { allowed, remaining, resetAt, timestamp }
 */
export function checkQuota(options = {}) {
  const maxPerDay = options.maxPerDay || 100;
  const log = options.log !== false;
  const now = Date.now();
  const today = new Date().toISOString().slice(0, 10);

  let quota = getQuotaData();
  if (!quota || quota.date !== today) {
    quota = { date: today, count: 0 };
  }

  const allowed = quota.count < maxPerDay;
  const remaining = Math.max(0, maxPerDay - quota.count);
  const resetAt = new Date(new Date(today).getTime() + 24 * 60 * 60 * 1000).toISOString();

  if (log && hasConsent()) {
    logQuotaEvent('quota_check', {
      date: today,
      count: quota.count,
      allowed,
      remaining,
      resetAt,
      timestamp: new Date().toISOString()
    });
  }

  return { allowed, remaining, resetAt, timestamp: new Date().toISOString() };
}

/**
 * Incrémente le compteur de quota pour l’utilisateur courant.
 * @param {object} [options]
 * @param {number} [options.maxPerDay=100]
 * @param {boolean} [options.log=true]
 * @returns {object} Résultat { allowed, remaining, resetAt, timestamp }
 */
export function incrementQuota(options = {}) {
  const maxPerDay = options.maxPerDay || 100;
  const log = options.log !== false;
  const now = Date.now();
  const today = new Date().toISOString().slice(0, 10);

  let quota = getQuotaData();
  if (!quota || quota.date !== today) {
    quota = { date: today, count: 0 };
  }

  quota.count += 1;
  setQuotaData(quota);

  const allowed = quota.count <= maxPerDay;
  const remaining = Math.max(0, maxPerDay - quota.count);
  const resetAt = new Date(new Date(today).getTime() + 24 * 60 * 60 * 1000).toISOString();

  if (log && hasConsent()) {
    logQuotaEvent('quota_increment', {
      date: today,
      count: quota.count,
      allowed,
      remaining,
      resetAt,
      timestamp: new Date().toISOString()
    });
  }

  return { allowed, remaining, resetAt, timestamp: new Date().toISOString() };
}

/**
 * Récupère les données de quota depuis le stockage local.
 * @returns {object|null}
 */
function getQuotaData() {
  if (typeof window !== 'undefined' && window.localStorage) {
    try {
      return JSON.parse(window.localStorage.getItem('ai_quota_data'));
    } catch {
      return null;
    }
  }
  return null;
}

/**
 * Enregistre les données de quota dans le stockage local.
 * @param {object} quota
 */
function setQuotaData(quota) {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.setItem('ai_quota_data', JSON.stringify(quota));
  }
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('ai_quota_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logQuotaEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('ai_quota_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('ai_quota_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de quota (droit à l’oubli RGPD).
 */
export function clearLocalQuotaLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('ai_quota_logs');
  }
}

/**
 * Réinitialise le quota local (droit à l’oubli RGPD).
 */
export function resetLocalQuota() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('ai_quota_data');
  }
}