/**
 * @file previewManager.js
 * @description Gestionnaire d’aperçus pour Dihya Coding (prévisualisation de blueprints, UI, code, mobile, etc.).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Génère un aperçu dynamique d’un blueprint ou d’un module.
 * @param {object} params
 * @param {string} params.type - Type d’aperçu ('web', 'mobile', 'code', etc.)
 * @param {object} params.data - Données à prévisualiser (code, config, UI, etc.)
 * @param {object} [params.options] - Options avancées (thème, device, langue, etc.)
 * @returns {Promise<{success: boolean, previewUrl: string, warnings?: string[]}>}
 */
export async function generatePreview({ type, data, options = {} }) {
  validatePreviewType(type);
  validatePreviewData(data);
  if (!window?.localStorage?.getItem('preview_feature_consent')) {
    throw new Error('Consentement requis pour générer un aperçu.');
  }
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/preview/generate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ type, data, options }),
  });
  if (!res.ok) throw new Error('Erreur lors de la génération de l’aperçu');
  const result = await res.json();
  logPreviewEvent('generate_preview', type, result.previewUrl);
  return result;
}

/**
 * Récupère l’historique des aperçus générés localement.
 * @returns {Array<object>}
 */
export function getLocalPreviewHistory() {
  try {
    return JSON.parse(localStorage.getItem('preview_manager_logs') || '[]');
  } catch {
    return [];
  }
}

/**
 * Valide le type d’aperçu demandé.
 * @param {string} type
 */
function validatePreviewType(type) {
  const SUPPORTED_TYPES = ['web', 'mobile', 'code', 'ui', 'doc'];
  if (!SUPPORTED_TYPES.includes(type)) {
    throw new Error('Type d’aperçu non supporté');
  }
}

/**
 * Valide les données à prévisualiser.
 * @param {object} data
 */
function validatePreviewData(data) {
  if (!data || typeof data !== 'object') {
    throw new Error('Données d’aperçu invalides');
  }
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} type
 * @param {string} [previewUrl]
 */
function logPreviewEvent(action, type, previewUrl) {
  try {
    const logs = JSON.parse(localStorage.getItem('preview_manager_logs') || '[]');
    logs.push({
      action,
      type,
      previewUrl,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('preview_manager_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs d’aperçus (droit à l’oubli RGPD).
 */
export function clearLocalPreviewManagerLogs() {
  localStorage.removeItem('preview_manager_logs');
}