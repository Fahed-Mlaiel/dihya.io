/**
 * @file corsConfig.js
 * @description Configuration CORS pour Dihya Coding : sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Génère une configuration CORS sécurisée selon les besoins métier.
 * @param {object} params
 * @param {string[]} [params.allowedOrigins] - Liste blanche des origines autorisées
 * @param {string[]} [params.allowedMethods] - Méthodes HTTP autorisées
 * @param {string[]} [params.allowedHeaders] - En-têtes autorisés
 * @param {boolean} [params.credentials=false] - Autoriser les credentials
 * @param {object} [params.options] - Options avancées (logs, RGPD, etc.)
 * @returns {object} Objet de configuration CORS
 */
export function getCorsConfig({
  allowedOrigins = ['https://dihya.app'],
  allowedMethods = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowedHeaders = ['Content-Type', 'Authorization'],
  credentials = false,
  options = {}
} = {}) {
  const config = {
    origin: function (origin, callback) {
      if (!origin || allowedOrigins.includes(origin)) {
        callback(null, true);
      } else {
        callback(new Error('Not allowed by CORS'));
      }
    },
    methods: allowedMethods.join(','),
    allowedHeaders: allowedHeaders.join(','),
    credentials
  };

  if (options.log !== false && hasConsent()) {
    logCorsConfigEvent('cors_config_generated', {
      allowedOrigins: anonymizeOrigins(allowedOrigins),
      allowedMethods,
      allowedHeaders,
      credentials,
      timestamp: new Date().toISOString()
    });
  }

  return config;
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('cors_config_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logCorsConfigEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('cors_config_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('cors_config_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise la liste des origines pour les logs.
 * @param {string[]} origins
 * @returns {string[]}
 */
function anonymizeOrigins(origins) {
  return (origins || []).map(origin =>
    origin.replace(/^(https?:\/\/)?([^/]+)(\/.*)?$/, (m, proto, host) => {
      if (!host) return '***';
      const parts = host.split('.');
      if (parts.length < 2) return '***';
      return (proto || '') + '***.' + parts.slice(-2).join('.');
    })
  );
}

/**
 * Efface les logs CORS (droit à l’oubli RGPD).
 */
export function clearLocalCorsConfigLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('cors_config_logs');
  }
}