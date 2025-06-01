/**
 * @file devops.js
 * @description Générateur et gestionnaire de blueprints DevOps pour Dihya Coding (CI/CD, Docker, pipelines, monitoring, sécurité).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les interactions sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Génère un blueprint DevOps (CI/CD, Docker, monitoring, etc.) à partir de paramètres métier.
 * @param {object} params
 * @param {string} params.projectName - Nom du projet (validé, anonymisé pour logs)
 * @param {Array<string>} params.features - Fonctions DevOps à inclure (ex: ['ci', 'docker', 'monitoring'])
 * @param {object} [params.options] - Options avancées (stack, cloud, sécurité, notifications)
 * @returns {Promise<{success: boolean, files: object, warnings?: string[]}>}
 */
export async function generateDevOpsBlueprint({ projectName, features, options = {} }) {
  validateProjectName(projectName);
  validateFeatures(features);
  if (!window?.localStorage?.getItem('devops_feature_consent')) {
    throw new Error('Consentement requis pour générer un blueprint DevOps.');
  }
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/blueprints/devops/generate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ projectName, features, options }),
  });
  if (!res.ok) throw new Error('Erreur lors de la génération du blueprint DevOps');
  const data = await res.json();
  logDevOpsEvent('generate_devops_blueprint', anonymizeProjectName(projectName), features);
  return data;
}

/**
 * Valide le nom du projet.
 * @param {string} projectName
 */
function validateProjectName(projectName) {
  if (!projectName || typeof projectName !== 'string' || projectName.length < 3 || projectName.length > 64) {
    throw new Error('Nom de projet invalide');
  }
}

/**
 * Valide la liste des features DevOps.
 * @param {Array<string>} features
 */
function validateFeatures(features) {
  const SUPPORTED_FEATURES = ['ci', 'cd', 'docker', 'monitoring', 'security', 'cloud', 'notifications'];
  if (
    !Array.isArray(features) ||
    features.length === 0 ||
    !features.every(f => typeof f === 'string' && SUPPORTED_FEATURES.includes(f))
  ) {
    throw new Error('Fonctions DevOps invalides');
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
 * @param {Array<string>} [features]
 */
function logDevOpsEvent(action, value, features) {
  try {
    const logs = JSON.parse(localStorage.getItem('devops_blueprint_logs') || '[]');
    logs.push({
      action,
      value,
      features,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('devops_blueprint_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de génération DevOps (droit à l’oubli RGPD).
 */
export function clearLocalDevOpsBlueprintLogs() {
  localStorage.removeItem('devops_blueprint_logs');
}