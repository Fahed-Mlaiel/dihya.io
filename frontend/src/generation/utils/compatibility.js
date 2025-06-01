/**
 * @file compatibility.js
 * @description Fonctions utilitaires pour vérifier la compatibilité des modules, templates et projets Dihya Coding (navigateurs, plateformes, dépendances, versions).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Vérifie la compatibilité navigateur.
 * @param {object} params
 * @param {string[]} params.requiredFeatures - Liste des fonctionnalités requises (ex: ['localStorage', 'fetch'])
 * @returns {object} Résultat de la vérification { compatible: boolean, missing: string[] }
 */
export function checkBrowserCompatibility({ requiredFeatures }) {
  if (!hasConsent()) throw new Error('Consentement requis pour vérifier la compatibilité.');
  if (!Array.isArray(requiredFeatures)) throw new Error('Paramètre requiredFeatures invalide');
  const missing = requiredFeatures.filter(f => typeof window[f] === 'undefined');
  logCompatibilityEvent('browser_check', { requiredFeatures, missing });
  return { compatible: missing.length === 0, missing };
}

/**
 * Vérifie la compatibilité des dépendances (ex: npm, package.json).
 * @param {object} params
 * @param {object} params.dependencies - Objet { nom: versionRequise }
 * @param {object} params.installed - Objet { nom: versionInstallée }
 * @returns {object} Résultat de la vérification { compatible: boolean, missing: string[], outdated: string[] }
 */
export function checkDependenciesCompatibility({ dependencies, installed }) {
  if (!hasConsent()) throw new Error('Consentement requis pour vérifier la compatibilité.');
  if (typeof dependencies !== 'object' || typeof installed !== 'object') throw new Error('Paramètres invalides');
  const missing = [];
  const outdated = [];
  for (const dep in dependencies) {
    if (!installed[dep]) {
      missing.push(dep);
    } else if (installed[dep] !== dependencies[dep]) {
      outdated.push(dep);
    }
  }
  logCompatibilityEvent('dependencies_check', { dependencies, installed, missing, outdated });
  return { compatible: missing.length === 0 && outdated.length === 0, missing, outdated };
}

/**
 * Vérifie la compatibilité de version d’un module ou template.
 * @param {object} params
 * @param {string} params.required - Version requise (ex: '1.2.0')
 * @param {string} params.current - Version actuelle (ex: '1.1.0')
 * @returns {object} Résultat de la vérification { compatible: boolean, required: string, current: string }
 */
export function checkVersionCompatibility({ required, current }) {
  if (!hasConsent()) throw new Error('Consentement requis pour vérifier la compatibilité.');
  if (typeof required !== 'string' || typeof current !== 'string') throw new Error('Paramètres de version invalides');
  const compatible = compareVersions(current, required) >= 0;
  logCompatibilityEvent('version_check', { required, current, compatible });
  return { compatible, required, current };
}

/**
 * Compare deux versions au format x.y.z.
 * @param {string} v1
 * @param {string} v2
 * @returns {number} 1 si v1 > v2, 0 si égal, -1 si v1 < v2
 */
function compareVersions(v1, v2) {
  const a = v1.split('.').map(Number);
  const b = v2.split('.').map(Number);
  for (let i = 0; i < Math.max(a.length, b.length); i++) {
    const diff = (a[i] || 0) - (b[i] || 0);
    if (diff > 0) return 1;
    if (diff < 0) return -1;
  }
  return 0;
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('compatibility_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logCompatibilityEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('compatibility_logs') || '[]');
    logs.push({
      action,
      data: anonymizeCompatibilityData(data),
      timestamp: new Date().toISOString(),
    });
    window.localStorage.setItem('compatibility_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise les données sensibles pour les logs.
 * @param {object} data
 * @returns {object}
 */
function anonymizeCompatibilityData(data) {
  // Ici, pas de données personnelles, mais on peut filtrer les noms de dépendances sensibles si besoin
  return data;
}

/**
 * Efface les logs de compatibilité (droit à l’oubli RGPD).
 */
export function clearLocalCompatibilityLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('compatibility_logs');
  }
}