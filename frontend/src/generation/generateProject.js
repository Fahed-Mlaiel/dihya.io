/**
 * @file generateProject.js
 * @description Générateur principal de projets Dihya Coding (structure, sécurité, compatibilité, auditabilité, SEO, RGPD).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Génère un projet Dihya Coding selon les spécifications fournies.
 * @param {object} params
 * @param {string} params.name - Nom du projet
 * @param {string[]} params.modules - Modules à inclure (ex: ['ai', 'ecommerce'])
 * @param {string} [params.author] - Auteur du projet
 * @param {object} [params.options] - Options avancées (seo, rgpd, sécurité, etc.)
 * @returns {object} Projet généré
 */
export function generateProject(params) {
  if (!hasConsent()) throw new Error('Consentement requis pour générer un projet.');
  validateProjectParams(params);

  const { name, modules, author, options = {} } = params;
  const project = {
    name: sanitize(name),
    modules: modules.map(sanitizeModule),
    author: author ? sanitize(author) : undefined,
    options: { ...options },
    createdAt: new Date().toISOString(),
    id: generateUniqueId(),
  };

  logProjectEvent('generate_project', anonymizeProject(project));
  return project;
}

/**
 * Valide les paramètres de génération de projet.
 * @param {object} params
 */
function validateProjectParams(params) {
  if (!params || typeof params !== 'object') throw new Error('Paramètres projet manquants ou invalides.');
  if (!params.name || typeof params.name !== 'string' || !params.name.trim()) throw new Error('Nom de projet invalide.');
  if (!Array.isArray(params.modules) || params.modules.length === 0) throw new Error('Modules projet manquants.');
  for (const mod of params.modules) {
    if (!isSupportedModule(mod)) throw new Error(`Module non supporté : ${mod}`);
  }
}

/**
 * Vérifie si un module est supporté.
 * @param {string} moduleName
 * @returns {boolean}
 */
function isSupportedModule(moduleName) {
  const supported = [
    'ai', 'blockchain', 'branding', 'devops', 'docs', 'ecommerce', 'education',
    'fields', 'health', 'i18n', 'infra', 'legal', 'mobile', 'preview', 'security',
    'seo', 'social', 'tests', 'utils', 'validators', 'voice'
  ];
  return supported.includes(moduleName);
}

/**
 * Génère un identifiant unique pour le projet.
 * @returns {string}
 */
function generateUniqueId() {
  return 'proj_' + Math.random().toString(36).slice(2, 10) + Date.now().toString(36);
}

/**
 * Sanitize une chaîne pour éviter les injections.
 * @param {string} str
 * @returns {string}
 */
function sanitize(str) {
  if (typeof str !== 'string') return '';
  return str.replace(/[<>"]/g, '').trim();
}

/**
 * Sanitize un nom de module.
 * @param {string} mod
 * @returns {string}
 */
function sanitizeModule(mod) {
  return sanitize(mod).toLowerCase();
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('project_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logProjectEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('project_template_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString(),
    });
    window.localStorage.setItem('project_template_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise les données sensibles du projet pour les logs.
 * @param {object} project
 * @returns {object}
 */
function anonymizeProject(project) {
  if (!project || typeof project !== 'object') return project;
  const clone = { ...project };
  if (clone.author) clone.author = '[anonymized]';
  return clone;
}

/**
 * Efface les logs de génération de projet (droit à l’oubli RGPD).
 */
export function clearLocalProjectLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('project_template_logs');
  }
}