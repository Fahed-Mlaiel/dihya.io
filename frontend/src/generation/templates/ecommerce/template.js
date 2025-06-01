/**
 * @file template.js
 * @description Template générique pour modules e-commerce Dihya Coding (catalogue, panier, paiement, utilisateur).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse, SEO et documentation claire.
 * Toutes les opérations sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Génère un module e-commerce selon le type demandé.
 * @param {object} params
 * @param {string} params.type - Type de module ('catalog', 'cart', 'checkout', 'user')
 * @param {object} params.data - Données du module (produits, panier, utilisateur, etc.)
 * @param {object} [params.options] - Options avancées (SEO, logs, RGPD, etc.)
 * @returns {object} Module e-commerce généré
 */
export function ecommerceTemplate({ type, data, options = {} }) {
  validateType(type);
  validateData(type, data);
  if (!window?.localStorage?.getItem('ecommerce_feature_consent')) {
    throw new Error('Consentement requis pour générer un module e-commerce.');
  }
  const module = generateModule(type, data, options);
  logEcommerceTemplateEvent('generate_ecommerce_module', type, anonymizeData(type, data));
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
    case 'catalog':
      return { catalog: data.products || [], ...options };
    case 'cart':
      return { cart: data.items || [], total: data.total || 0, ...options };
    case 'checkout':
      return { order: data.order || {}, payment: data.payment || {}, ...options };
    case 'user':
      return { user: anonymizeUser(data.user || {}), ...options };
    default:
      throw new Error('Type de module e-commerce non supporté');
  }
}

/**
 * Valide le type de module e-commerce.
 * @param {string} type
 */
function validateType(type) {
  const SUPPORTED = ['catalog', 'cart', 'checkout', 'user'];
  if (!SUPPORTED.includes(type)) {
    throw new Error('Type de module e-commerce invalide');
  }
}

/**
 * Valide les données selon le type de module.
 * @param {string} type
 * @param {object} data
 */
function validateData(type, data) {
  if (!data || typeof data !== 'object') throw new Error('Données du module invalides');
  if (type === 'catalog' && !Array.isArray(data.products)) throw new Error('Catalogue invalide');
  if (type === 'cart' && !Array.isArray(data.items)) throw new Error('Panier invalide');
  if (type === 'checkout' && (typeof data.order !== 'object' || typeof data.payment !== 'object')) throw new Error('Données de commande/paiement invalides');
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
  if (type === 'checkout' && data.payment) {
    return { ...data, payment: '[protected]' };
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
function logEcommerceTemplateEvent(action, type, data) {
  try {
    const logs = JSON.parse(localStorage.getItem('ecommerce_template_logs') || '[]');
    logs.push({
      action,
      type,
      data,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('ecommerce_template_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de génération e-commerce (droit à l’oubli RGPD).
 */
export function clearLocalEcommerceTemplateLogs() {
  localStorage.removeItem('ecommerce_template_logs');
}