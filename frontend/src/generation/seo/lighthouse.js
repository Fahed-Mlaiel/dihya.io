/**
 * @file lighthouse.js
 * @description Intégration et gestion des audits Lighthouse pour Dihya Coding (SEO, performance, accessibilité, logs, auditabilité).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Lance un audit Lighthouse sur une URL cible.
 * @param {object} params
 * @param {string} params.url - URL à auditer (sera validée et anonymisée pour les logs)
 * @param {object} [params.options] - Options avancées (catégories, device, locale, etc.)
 * @returns {Promise<{success: boolean, report: object, warnings?: string[]}>}
 */
export async function runLighthouseAudit({ url, options = {} }) {
  validateUrl(url);
  if (!window?.localStorage?.getItem('seo_feature_consent')) {
    throw new Error('Consentement requis pour lancer un audit Lighthouse.');
  }
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/seo/lighthouse/audit', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ url, options }),
  });
  if (!res.ok) throw new Error('Erreur lors de l’audit Lighthouse');
  const result = await res.json();
  logLighthouseEvent('run_lighthouse_audit', anonymizeUrl(url));
  return result;
}

/**
 * Valide une URL cible pour l’audit.
 * @param {string} url
 */
function validateUrl(url) {
  try {
    const u = new URL(url);
    if (!['http:', 'https:'].includes(u.protocol)) throw new Error();
  } catch {
    throw new Error('URL cible invalide pour Lighthouse');
  }
}

/**
 * Anonymise une URL pour les logs (suppression des paramètres sensibles).
 * @param {string} url
 * @returns {string}
 */
function anonymizeUrl(url) {
  try {
    const u = new URL(url);
    u.search = '';
    u.hash = '';
    return u.toString();
  } catch {
    return '[invalid-url]';
  }
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} url
 */
function logLighthouseEvent(action, url) {
  try {
    const logs = JSON.parse(localStorage.getItem('lighthouse_logs') || '[]');
    logs.push({
      action,
      url,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('lighthouse_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs d’audit Lighthouse (droit à l’oubli RGPD).
 */
export function clearLocalLighthouseLogs() {
  localStorage.removeItem('lighthouse_logs');
}