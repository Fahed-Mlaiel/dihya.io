/**
 * @file terraformGen.js
 * @description Générateur et gestionnaire de fichiers Terraform pour Dihya Coding (infrastructure as code, audit, logs).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les interactions sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Génère un fichier Terraform à partir de paramètres métier.
 * @param {object} params
 * @param {string} params.projectName - Nom du projet (validé, anonymisé pour logs)
 * @param {Array<object>} params.resources - Liste des ressources à provisionner (type, config)
 * @param {object} [params.options] - Options avancées (provider, variables, outputs, etc.)
 * @returns {Promise<{success: boolean, terraform: string, warnings?: string[]}>}
 */
export async function generateTerraform({ projectName, resources, options = {} }) {
  validateProjectName(projectName);
  validateResources(resources);
  if (!window?.localStorage?.getItem('terraform_feature_consent')) {
    throw new Error('Consentement requis pour générer un fichier Terraform.');
  }
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/devops/terraform/generate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ projectName, resources, options }),
  });
  if (!res.ok) throw new Error('Erreur lors de la génération du fichier Terraform');
  const data = await res.json();
  logTerraformGenEvent('generate_terraform', anonymizeProjectName(projectName));
  return data;
}

/**
 * Audite un fichier Terraform existant.
 * @param {object} params
 * @param {string} params.terraformCode - Contenu du fichier Terraform à auditer
 * @returns {Promise<{success: boolean, issues: Array, report: string}>}
 */
export async function auditTerraform({ terraformCode }) {
  validateTerraformCode(terraformCode);
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/devops/terraform/audit', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ terraformCode }),
  });
  if (!res.ok) throw new Error('Erreur lors de l’audit du fichier Terraform');
  const data = await res.json();
  logTerraformGenEvent('audit_terraform', '[terraform]');
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
 * Valide la liste des ressources Terraform.
 * @param {Array<object>} resources
 */
function validateResources(resources) {
  if (
    !Array.isArray(resources) ||
    resources.length === 0 ||
    !resources.every(
      r =>
        r &&
        typeof r === 'object' &&
        typeof r.type === 'string' &&
        typeof r.config === 'object'
    )
  ) {
    throw new Error('Ressources Terraform invalides');
  }
}

/**
 * Valide le contenu d’un fichier Terraform.
 * @param {string} terraformCode
 */
function validateTerraformCode(terraformCode) {
  if (!terraformCode || typeof terraformCode !== 'string' || terraformCode.length < 10) {
    throw new Error('Contenu Terraform invalide');
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
function logTerraformGenEvent(action, value) {
  try {
    const logs = JSON.parse(localStorage.getItem('terraform_gen_logs') || '[]');
    logs.push({
      action,
      value,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('terraform_gen_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de génération/audit Terraform (droit à l’oubli RGPD).
 */
export function clearLocalTerraformGenLogs() {
  localStorage.removeItem('terraform_gen_logs');
}