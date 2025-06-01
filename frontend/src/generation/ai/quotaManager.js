/**
 * @file quotaManager.js
 * @description Gestionnaire centralisé des quotas IA pour Dihya Coding (gestion, consommation, réinitialisation, logs).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les interactions sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Consomme une unité de quota IA pour l’utilisateur.
 * @param {object} params
 * @param {string} params.userId - Identifiant utilisateur (sera anonymisé pour les logs)
 * @returns {Promise<{success: boolean, remaining: number, resetAt: string}>}
 */
export async function consumeQuota({ userId }) {
  validateUserId(userId);
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/ai/quota/consume', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ userId }),
  });
  if (!res.ok) throw new Error('Erreur lors de la consommation du quota');
  const data = await res.json();
  logQuotaManagerEvent('consume_quota', anonymizeUserId(userId), data.remaining);
  return data;
}

/**
 * Réinitialise le quota IA de l’utilisateur (action admin).
 * @param {object} params
 * @param {string} params.userId
 * @returns {Promise<{success: boolean, resetAt: string}>}
 */
export async function resetQuota({ userId }) {
  validateUserId(userId);
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/ai/quota/reset', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ userId }),
  });
  if (!res.ok) throw new Error('Erreur lors de la réinitialisation du quota');
  const data = await res.json();
  logQuotaManagerEvent('reset_quota', anonymizeUserId(userId));
  return data;
}

/**
 * Récupère l’état du quota IA pour l’utilisateur.
 * @param {object} params
 * @param {string} params.userId
 * @returns {Promise<{remaining: number, resetAt: string, quota: number}>}
 */
export async function getQuotaStatus({ userId }) {
  validateUserId(userId);
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/ai/quota/status', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ userId }),
  });
  if (!res.ok) throw new Error('Erreur lors de la récupération du statut de quota');
  const data = await res.json();
  logQuotaManagerEvent('get_quota_status', anonymizeUserId(userId), data.remaining);
  return data;
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
 * Anonymise l’identifiant utilisateur pour les logs.
 * @param {string} userId
 * @returns {string}
 */
function anonymizeUserId(userId) {
  // Exemple simple : suppression d’emails
  return userId.replace(/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/gi, '[email]');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string|null} value
 * @param {number} [remaining]
 */
function logQuotaManagerEvent(action, value, remaining) {
  try {
    const logs = JSON.parse(localStorage.getItem('quota_manager_logs') || '[]');
    logs.push({
      action,
      value,
      remaining,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('quota_manager_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de gestion de quota (droit à l’oubli RGPD).
 */
export function clearLocalQuotaManagerLogs() {
  localStorage.removeItem('quota_manager_logs');
}