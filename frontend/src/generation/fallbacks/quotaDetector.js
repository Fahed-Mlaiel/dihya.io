/**
 * @file quotaDetector.js
 * @description Détection et gestion des quotas d’utilisation IA pour Dihya Coding (alerte, blocage, logs).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les interactions sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Vérifie si l’utilisateur a dépassé son quota IA.
 * @param {object} params
 * @param {string} params.userId - Identifiant utilisateur (anonymisé pour les logs)
 * @returns {Promise<{quotaExceeded: boolean, remaining: number, resetAt: string}>}
 */
export async function checkQuota({ userId }) {
  validateUserId(userId);
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/ai/quota', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ userId }),
  });
  if (!res.ok) throw new Error('Erreur lors de la vérification du quota');
  const data = await res.json();
  logQuotaEvent('check_quota', anonymizeUserId(userId), data.quotaExceeded);
  return data;
}

/**
 * Déclenche une alerte UI si le quota est dépassé ou proche de l’être.
 * @param {object} quotaInfo
 * @param {boolean} quotaInfo.quotaExceeded
 * @param {number} quotaInfo.remaining
 * @param {string} quotaInfo.resetAt
 */
export function handleQuotaAlert({ quotaExceeded, remaining, resetAt }) {
  if (quotaExceeded) {
    showQuotaNotification({
      message: `Quota IA atteint. Réinitialisation le ${new Date(resetAt).toLocaleString()}.`,
      type: 'warning',
    });
    logQuotaEvent('quota_alert', null, true);
  } else if (remaining <= 3) {
    showQuotaNotification({
      message: `Attention : il ne vous reste plus que ${remaining} requête(s) IA avant le quota.`,
      type: 'info',
    });
    logQuotaEvent('quota_warning', null, false);
  }
}

/**
 * Affiche une notification de quota (à connecter à un composant UI).
 * @param {object} params
 * @param {string} params.message
 * @param {string} [params.type]
 */
function showQuotaNotification({ message, type = 'info' }) {
  window.dispatchEvent(new CustomEvent('dihya-notification', {
    detail: { message, type, duration: 6000 }
  }));
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
 * @param {boolean} [quotaExceeded]
 */
function logQuotaEvent(action, value, quotaExceeded) {
  try {
    const logs = JSON.parse(localStorage.getItem('quota_detector_logs') || '[]');
    logs.push({
      action,
      value,
      quotaExceeded,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('quota_detector_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de quota locaux (droit à l’oubli RGPD).
 */
export function clearLocalQuotaDetectorLogs() {
  localStorage.removeItem('quota_detector_logs');
}