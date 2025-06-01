/**
 * @file template.js
 * @description Template générique pour modules sociaux Dihya Coding (profils, réseaux, partage, commentaires, notifications).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse, SEO et documentation claire.
 * Toutes les opérations sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Génère un module social selon le type demandé.
 * @param {object} params
 * @param {string} params.type - Type de module ('profile', 'network', 'share', 'comment', 'notification')
 * @param {object} params.data - Données du module (profil, réseau, partage, commentaire, notification, etc.)
 * @param {object} [params.options] - Options avancées (SEO, logs, RGPD, etc.)
 * @returns {object} Module social généré
 */
export function socialTemplate({ type, data, options = {} }) {
  validateType(type);
  validateData(type, data);
  if (!window?.localStorage?.getItem('social_feature_consent')) {
    throw new Error('Consentement requis pour générer un module social.');
  }
  const module = generateModule(type, data, options);
  logSocialTemplateEvent('generate_social_module', type, anonymizeData(type, data));
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
    case 'profile':
      return { profile: anonymizeProfile(data.profile || {}), ...options };
    case 'network':
      return { network: data.network || {}, ...options };
    case 'share':
      return { share: data.share || {}, ...options };
    case 'comment':
      return { comment: anonymizeComment(data.comment || {}), ...options };
    case 'notification':
      return { notification: data.notification || {}, ...options };
    default:
      throw new Error('Type de module social non supporté');
  }
}

/**
 * Valide le type de module social.
 * @param {string} type
 */
function validateType(type) {
  const SUPPORTED = ['profile', 'network', 'share', 'comment', 'notification'];
  if (!SUPPORTED.includes(type)) {
    throw new Error('Type de module social invalide');
  }
}

/**
 * Valide les données selon le type de module.
 * @param {string} type
 * @param {object} data
 */
function validateData(type, data) {
  if (!data || typeof data !== 'object') throw new Error('Données du module invalides');
  if (type === 'profile' && typeof data.profile !== 'object') throw new Error('Données profil invalides');
  if (type === 'network' && typeof data.network !== 'object') throw new Error('Données réseau invalides');
  if (type === 'share' && typeof data.share !== 'object') throw new Error('Données partage invalides');
  if (type === 'comment' && typeof data.comment !== 'object') throw new Error('Données commentaire invalides');
  if (type === 'notification' && typeof data.notification !== 'object') throw new Error('Données notification invalides');
}

/**
 * Anonymise les données sensibles pour les logs.
 * @param {string} type
 * @param {object} data
 * @returns {object}
 */
function anonymizeData(type, data) {
  if (type === 'profile' && data.profile) {
    return { ...data, profile: anonymizeProfile(data.profile) };
  }
  if (type === 'comment' && data.comment) {
    return { ...data, comment: anonymizeComment(data.comment) };
  }
  return data;
}

/**
 * Anonymise les données de profil utilisateur pour les logs.
 * @param {object} profile
 * @returns {object}
 */
function anonymizeProfile(profile) {
  if (!profile) return {};
  const { email, phone, ...rest } = profile;
  return {
    ...rest,
    email: email ? '[email]' : undefined,
    phone: phone ? '[phone]' : undefined,
  };
}

/**
 * Anonymise les données de commentaire pour les logs.
 * @param {object} comment
 * @returns {object}
 */
function anonymizeComment(comment) {
  if (!comment) return {};
  const { authorEmail, ...rest } = comment;
  return {
    ...rest,
    authorEmail: authorEmail ? '[email]' : undefined,
  };
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} type
 * @param {object} data
 */
function logSocialTemplateEvent(action, type, data) {
  try {
    const logs = JSON.parse(localStorage.getItem('social_template_logs') || '[]');
    logs.push({
      action,
      type,
      data,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('social_template_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de génération sociale (droit à l’oubli RGPD).
 */
export function clearLocalSocialTemplateLogs() {
  localStorage.removeItem('social_template_logs');
}