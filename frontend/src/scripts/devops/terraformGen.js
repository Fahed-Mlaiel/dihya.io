/**
 * @file terraformGen.js
 * @description Générateur de fichiers Terraform pour Dihya Coding : génération sécurisée, validation, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Génère un fichier Terraform (main.tf) selon les paramètres fournis.
 * @param {object} params
 * @param {string} params.provider - Nom du provider (ex: 'aws', 'azurerm', 'google')
 * @param {object} params.config - Configuration du provider (clé/valeur)
 * @param {object[]} [params.resources] - Liste des ressources à créer (type, name, config)
 * @param {object} [params.options] - Options avancées (logs, labels, etc.)
 * @returns {object} Résultat { success, code, error, timestamp }
 */
export function generateTerraformFile({
  provider,
  config,
  resources = [],
  options = {}
}) {
  if (!hasConsent()) {
    return {
      success: false,
      code: null,
      error: 'Consentement requis',
      timestamp: new Date().toISOString()
    };
  }
  if (
    !provider ||
    typeof provider !== 'string' ||
    !/^[a-z][a-z0-9_]{1,32}$/i.test(provider)
  ) {
    return {
      success: false,
      code: null,
      error: 'Provider invalide',
      timestamp: new Date().toISOString()
    };
  }
  if (!config || typeof config !== 'object') {
    return {
      success: false,
      code: null,
      error: 'Configuration provider invalide',
      timestamp: new Date().toISOString()
    };
  }

  let code = `# Généré par Dihya Coding – ${new Date().toISOString()}
terraform {
  required_providers {
    ${provider} = {
      source = "${getProviderSource(provider)}"
      version = "~> ${options.version || '1.0'}"
    }
  }
}

provider "${provider}" {
${Object.entries(config)
  .map(([k, v]) => `  ${sanitizeKey(k)} = "${sanitizeValue(v)}"`)
  .join('\n')}
}
`;

  if (Array.isArray(resources)) {
    resources.forEach((res) => {
      if (
        res &&
        typeof res === 'object' &&
        res.type &&
        res.name &&
        /^[a-zA-Z0-9_]{2,32}$/.test(res.name)
      ) {
        code += `
resource "${sanitizeKey(res.type)}" "${sanitizeKey(res.name)}" {
${Object.entries(res.config || {})
  .map(([k, v]) => `  ${sanitizeKey(k)} = "${sanitizeValue(v)}"`)
  .join('\n')}
}
`;
      }
    });
  }

  if (options.log !== false) {
    logTerraformGenEvent('terraform_file_generated', {
      provider: anonymizeProvider(provider),
      resources: (resources || []).map((r) => r.type),
      timestamp: new Date().toISOString()
    });
  }

  return {
    success: true,
    code,
    error: null,
    timestamp: new Date().toISOString()
  };
}

/**
 * Retourne la source officielle du provider Terraform.
 * @param {string} provider
 * @returns {string}
 */
function getProviderSource(provider) {
  const sources = {
    aws: 'hashicorp/aws',
    azurerm: 'hashicorp/azurerm',
    google: 'hashicorp/google'
  };
  return sources[provider] || `hashicorp/${provider}`;
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('terraform_gen_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logTerraformGenEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('terraform_gen_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('terraform_gen_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise le nom du provider pour les logs.
 * @param {string} provider
 * @returns {string}
 */
function anonymizeProvider(provider) {
  if (!provider) return '';
  return provider.length > 4 ? provider.slice(0, 2) + '***' + provider.slice(-2) : '***';
}

/**
 * Sanitize une clé pour Terraform.
 * @param {string} key
 * @returns {string}
 */
function sanitizeKey(key) {
  return String(key).replace(/[^a-zA-Z0-9_]/g, '');
}

/**
 * Sanitize une valeur pour Terraform.
 * @param {string|number} value
 * @returns {string}
 */
function sanitizeValue(value) {
  return String(value).replace(/["\\]/g, '');
}

/**
 * Efface les logs de génération Terraform (droit à l’oubli RGPD).
 */
export function clearLocalTerraformGenLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('terraform_gen_logs');
  }
}