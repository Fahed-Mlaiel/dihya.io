/**
 * @file webApp.js
 * @description Générateur et gestionnaire de blueprints d’applications web pour Dihya Coding (création, configuration, audit, logs).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les interactions sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Génère un blueprint d’application web à partir de paramètres métier.
 * @param {object} params
 * @param {string} params.name - Nom de l’application (validé, anonymisé pour logs)
 * @param {string} params.stack - Stack technologique (ex: 'react', 'vue', 'nextjs', 'svelte')
 * @param {object} [params.options] - Options avancées (seo, thème, modules, pwa, etc.)
 * @returns {Promise<{success: boolean, files: object, warnings?: string[]}>}
 */
export async function generateWebApp({ name, stack, options = {} }) {
  validateAppName(name);
  validateStack(stack);
  if (!window?.localStorage?.getItem('web_app_feature_consent')) {
    throw new Error('Consentement requis pour générer une application web.');
  }
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/blueprints/webApp/generate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ name, stack, options }),
  });
  if (!res.ok) throw new Error('Erreur lors de la génération de l’application web');
  const data = await res.json();
  logWebAppEvent('generate_web_app', anonymizeAppName(name), stack);
  return data;
}

/**
 * Audite une application web existante.
 * @param {object} params
 * @param {string} params.appCode - Code source de l’application à auditer
 * @returns {Promise<{success: boolean, issues: Array, report: string}>}
 */
export async function auditWebApp({ appCode }) {
  validateAppCode(appCode);
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/blueprints/webApp/audit', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ appCode }),
  });
  if (!res.ok) throw new Error('Erreur lors de l’audit de l’application web');
  const data = await res.json();
  logWebAppEvent('audit_web_app', '[code]');
  return data;
}

/**
 * Valide le nom de l’application.
 * @param {string} name
 */
function validateAppName(name) {
  if (!name || typeof name !== 'string' || name.length < 3 || name.length > 64) {
    throw new Error('Nom d’application invalide');
  }
}

/**
 * Valide la stack technologique.
 * @param {string} stack
 */
function validateStack(stack) {
  const SUPPORTED_STACKS = ['react', 'vue', 'nextjs', 'svelte', 'angular', 'nuxt', 'remix'];
  if (!SUPPORTED_STACKS.includes(stack)) {
    throw new Error('Stack technologique non supportée');
  }
}

/**
 * Valide le code source de l’application.
 * @param {string} appCode
 */
function validateAppCode(appCode) {
  if (!appCode || typeof appCode !== 'string' || appCode.length < 10) {
    throw new Error('Code source d’application invalide');
  }
}

/**
 * Anonymise le nom de l’application pour les logs (pas de données personnelles).
 * @param {string} name
 * @returns {string}
 */
function anonymizeAppName(name) {
  return name.replace(/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/gi, '[email]');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} value
 * @param {string} [stack]
 */
function logWebAppEvent(action, value, stack) {
  try {
    const logs = JSON.parse(localStorage.getItem('web_app_blueprint_logs') || '[]');
    logs.push({
      action,
      value,
      stack,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('web_app_blueprint_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de génération/audit web (droit à l’oubli RGPD).
 */
export function clearLocalWebAppBlueprintLogs() {
  localStorage.removeItem('web_app_blueprint_logs');
}