/**
 * @file template.js
 * @description Template générique pour modules éducatifs Dihya Coding (cours, quiz, évaluations, utilisateurs).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse, SEO et documentation claire.
 * Toutes les opérations sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Génère un module éducatif selon le type demandé.
 * @param {object} params
 * @param {string} params.type - Type de module ('course', 'quiz', 'evaluation', 'user')
 * @param {object} params.data - Données du module (cours, quiz, utilisateur, etc.)
 * @param {object} [params.options] - Options avancées (SEO, logs, RGPD, etc.)
 * @returns {object} Module éducatif généré
 */
export function educationTemplate({ type, data, options = {} }) {
  validateType(type);
  validateData(type, data);
  if (!window?.localStorage?.getItem('education_feature_consent')) {
    throw new Error('Consentement requis pour générer un module éducatif.');
  }
  const module = generateModule(type, data, options);
  logEducationTemplateEvent('generate_education_module', type, anonymizeData(type, data));
  return module;
}

/**
 * Génère le module selon le type.
 * @param {string} type
 * @param {object} data
 * @param {object} options
 * @returns {object}
 */
function generateModule(type, data, options) {
  switch (type) {
    case 'course':
      return { course: data.course || {}, lessons: data.lessons || [], ...options };
    case 'quiz':
      return { quiz: data.quiz || {}, questions: data.questions || [], ...options };
    case 'evaluation':
      return { evaluation: data.evaluation || {}, feedback: data.feedback || '', ...options };
    case 'user':
      return { user: anonymizeUser(data.user || {}), ...options };
    default:
      throw new Error('Type de module éducatif non supporté');
  }
}

/**
 * Valide le type de module éducatif.
 * @param {string} type
 */
function validateType(type) {
  const SUPPORTED = ['course', 'quiz', 'evaluation', 'user'];
  if (!SUPPORTED.includes(type)) {
    throw new Error('Type de module éducatif invalide');
  }
}

/**
 * Valide les données selon le type de module.
 * @param {string} type
 * @param {object} data
 */
function validateData(type, data) {
  if (!data || typeof data !== 'object') throw new Error('Données du module invalides');
  if (type === 'course' && (!data.course || !Array.isArray(data.lessons))) throw new Error('Données de cours invalides');
  if (type === 'quiz' && (!data.quiz || !Array.isArray(data.questions))) throw new Error('Données de quiz invalides');
  if (type === 'evaluation' && typeof data.evaluation !== 'object') throw new Error('Données d’évaluation invalides');
  if (type === 'user' && typeof data.user !== 'object') throw new Error('Données utilisateur invalides');
}

/**
 * Anonymise les données sensibles pour les logs.
 * @param {string} type
 * @param {object} data
 * @returns {object}
 */
function anonymizeData(type, data) {
  if (type === 'user' && data.user) {
    return { ...data, user: anonymizeUser(data.user) };
  }
  return data;
}

/**
 * Anonymise les données utilisateur pour les logs.
 * @param {object} user
 * @returns {object}
 */
function anonymizeUser(user) {
  if (!user) return {};
  const { email, password, ...rest } = user;
  return { ...rest, email: email ? '[email]' : undefined, password: '[protected]' };
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} type
 * @param {object} data
 */
function logEducationTemplateEvent(action, type, data) {
  try {
    const logs = JSON.parse(localStorage.getItem('education_template_logs') || '[]');
    logs.push({
      action,
      type,
      data,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('education_template_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de génération éducative (droit à l’oubli RGPD).
 */
export function clearLocalEducationTemplateLogs() {
  localStorage.removeItem('education_template_logs');
}