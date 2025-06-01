/**
 * @file backendApi.js
 * @description Générateur et gestionnaire d’API backend pour Dihya Coding (création de routes, contrôleurs, modèles, validation).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les interactions sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Génère une API backend à partir d’un schéma métier.
 * @param {object} params
 * @param {string} params.name - Nom de l’API (validé, anonymisé pour logs)
 * @param {Array<object>} params.endpoints - Liste des endpoints à générer
 * @param {object} [params.options] - Options avancées (auth, validation, stack)
 * @returns {Promise<{success: boolean, files: object, warnings?: string[]}>}
 */
export async function generateBackendApi({ name, endpoints, options = {} }) {
  validateApiName(name);
  validateEndpoints(endpoints);
  if (!window?.localStorage?.getItem('backend_api_feature_consent')) {
    throw new Error('Consentement requis pour générer une API backend.');
  }
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/blueprints/backendApi/generate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ name, endpoints, options }),
  });
  if (!res.ok) throw new Error('Erreur lors de la génération de l’API backend');
  const data = await res.json();
  logBackendApiEvent('generate_backend_api', anonymizeApiName(name));
  return data;
}

/**
 * Valide le nom de l’API.
 * @param {string} name
 */
function validateApiName(name) {
  if (!name || typeof name !== 'string' || name.length < 3 || name.length > 64) {
    throw new Error('Nom d’API invalide');
  }
}

/**
 * Valide la structure des endpoints.
 * @param {Array<object>} endpoints
 */
function validateEndpoints(endpoints) {
  if (
    !Array.isArray(endpoints) ||
    endpoints.length === 0 ||
    !endpoints.every(
      ep =>
        ep &&
        typeof ep === 'object' &&
        typeof ep.path === 'string' &&
        typeof ep.method === 'string' &&
        ['GET', 'POST', 'PUT', 'DELETE', 'PATCH'].includes(ep.method.toUpperCase())
    )
  ) {
    throw new Error('Endpoints API invalides');
  }
}

/**
 * Anonymise le nom de l’API pour les logs (pas de données personnelles).
 * @param {string} name
 * @returns {string}
 */
function anonymizeApiName(name) {
  return name.replace(/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/gi, '[email]');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} value
 */
function logBackendApiEvent(action, value) {
  try {
    const logs = JSON.parse(localStorage.getItem('backend_api_logs') || '[]');
    logs.push({
      action,
      value,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('backend_api_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de génération d’API backend (droit à l’oubli RGPD).
 */
export function clearLocalBackendApiLogs() {
  localStorage.removeItem('backend_api_logs');
}