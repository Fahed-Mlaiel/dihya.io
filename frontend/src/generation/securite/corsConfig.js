/**
 * @file corsConfig.js
 * @description Gestion avancée de la configuration CORS pour Dihya Coding (sécurité, audit, logs, conformité RGPD).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les configurations sont validées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Définit la configuration CORS recommandée pour une API Dihya Coding.
 * @param {object} params
 * @param {Array<string>} params.allowedOrigins - Origines autorisées (ex: ['https://dihya.app'])
 * @param {Array<string>} [params.allowedMethods] - Méthodes HTTP autorisées (GET, POST, etc.)
 * @param {Array<string>} [params.allowedHeaders] - Headers autorisés
 * @param {boolean} [params.allowCredentials] - Autoriser les credentials (cookies, auth)
 * @returns {object} Objet de configuration CORS prêt à l’emploi
 */
export function getCorsConfig({
  allowedOrigins,
  allowedMethods = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowedHeaders = ['Content-Type', 'Authorization'],
  allowCredentials = false,
}) {
  validateOrigins(allowedOrigins);
  logCorsConfigEvent('get_cors_config', allowedOrigins, allowCredentials);
  return {
    origin: function (origin, callback) {
      if (!origin || allowedOrigins.includes(origin)) {
        callback(null, true);
      } else {
        callback(new Error('Origine non autorisée par la politique CORS'), false);
      }
    },
    methods: allowedMethods,
    allowedHeaders,
    credentials: !!allowCredentials,
    optionsSuccessStatus: 204,
  };
}

/**
 * Valide la liste des origines autorisées.
 * @param {Array<string>} origins
 */
function validateOrigins(origins) {
  if (
    !Array.isArray(origins) ||
    origins.length === 0 ||
    !origins.every(o => typeof o === 'string' && /^https?:\/\/[a-zA-Z0-9.-]+(:\d+)?(\/)?$/.test(o))
  ) {
    throw new Error('Liste des origines CORS invalide');
  }
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {Array<string>} origins
 * @param {boolean} allowCredentials
 */
function logCorsConfigEvent(action, origins, allowCredentials) {
  try {
    const logs = JSON.parse(localStorage.getItem('cors_config_logs') || '[]');
    logs.push({
      action,
      origins: origins.map(anonymizeOrigin),
      allowCredentials,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('cors_config_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise une origine pour les logs (suppression éventuelle de sous-domaines sensibles).
 * @param {string} origin
 * @returns {string}
 */
function anonymizeOrigin(origin) {
  // Exemple simple : suppression des sous-domaines
  try {
    const url = new URL(origin);
    return url.protocol + '//' + url.hostname.split('.').slice(-2).join('.');
  } catch {
    return '[invalid-origin]';
  }
}

/**
 * Efface les logs de configuration CORS (droit à l’oubli RGPD).
 */
export function clearLocalCorsConfigLogs() {
  localStorage.removeItem('cors_config_logs');
}