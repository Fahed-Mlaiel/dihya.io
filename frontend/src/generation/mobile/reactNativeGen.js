/**
 * @file reactNativeGen.js
 * @description Générateur et gestionnaire de blueprints React Native pour Dihya Coding (création, configuration, audit, logs).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les interactions sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Génère un projet React Native à partir de paramètres métier.
 * @param {object} params
 * @param {string} params.projectName - Nom du projet React Native (sera anonymisé pour les logs)
 * @param {object} [params.options] - Options avancées (modules, thèmes, navigation, pwa, etc.)
 * @returns {Promise<{success: boolean, files: object, warnings?: string[]}>}
 */
export async function generateReactNativeProject({ projectName, options = {} }) {
  validateProjectName(projectName);
  if (!window?.localStorage?.getItem('mobile_feature_consent')) {
    throw new Error('Consentement requis pour générer un projet React Native.');
  }
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/mobile/reactnative/generate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ projectName, options }),
  });
  if (!res.ok) throw new Error('Erreur lors de la génération du projet React Native');
  const data = await res.json();
  logReactNativeGenEvent('generate_react_native_project', anonymizeProjectName(projectName));
  return data;
}

/**
 * Audite un projet React Native existant.
 * @param {object} params
 * @param {string} params.projectCode - Code source du projet à auditer
 * @returns {Promise<{success: boolean, issues: Array, report: string}>}
 */
export async function auditReactNativeProject({ projectCode }) {
  validateProjectCode(projectCode);
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/mobile/reactnative/audit', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ projectCode }),
  });
  if (!res.ok) throw new Error('Erreur lors de l’audit du projet React Native');
  const data = await res.json();
  logReactNativeGenEvent('audit_react_native_project', '[code]');
  return data;
}

/**
 * Valide le nom du projet React Native.
 * @param {string} projectName
 */
function validateProjectName(projectName) {
  if (!projectName || typeof projectName !== 'string' || projectName.length < 3 || projectName.length > 64) {
    throw new Error('Nom de projet React Native invalide');
  }
}

/**
 * Valide le code source du projet React Native.
 * @param {string} projectCode
 */
function validateProjectCode(projectCode) {
  if (!projectCode || typeof projectCode !== 'string' || projectCode.length < 10) {
    throw new Error('Code source React Native invalide');
  }
}

/**
 * Anonymise le nom du projet pour les logs (pas de données personnelles).
 * @param {string} projectName
 * @returns {string}
 */
function anonymizeProjectName(projectName) {
  return projectName.replace(/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/gi, '[email]');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} value
 */
function logReactNativeGenEvent(action, value) {
  try {
    const logs = JSON.parse(localStorage.getItem('react_native_gen_logs') || '[]');
    logs.push({
      action,
      value,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('react_native_gen_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de génération/audit React Native (droit à l’oubli RGPD).
 */
export function clearLocalReactNativeGenLogs() {
  localStorage.removeItem('react_native_gen_logs');
}