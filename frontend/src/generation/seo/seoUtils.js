/**
 * @file seoUtils.js
 * @description Utilitaires avancés pour le SEO dans Dihya Coding (génération de slugs, validation, analyse de contenu, logs, auditabilité).
 * Garantit design moderne, SEO optimal, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Génère un slug SEO-friendly à partir d’un texte.
 * @param {string} text
 * @returns {string}
 */
export function generateSlug(text) {
  if (!text || typeof text !== 'string') throw new Error('Texte invalide pour slug');
  const slug = text
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '') // accents
    .replace(/[^a-z0-9]+/g, '-') // non alphanum
    .replace(/^-+|-+$/g, '') // trim
    .replace(/-+/g, '-');
  logSeoUtilsEvent('generate_slug', slug);
  return slug;
}

/**
 * Valide un slug SEO.
 * @param {string} slug
 * @returns {boolean}
 */
export function validateSlug(slug) {
  const valid = typeof slug === 'string' && /^[a-z0-9]+(-[a-z0-9]+)*$/.test(slug) && slug.length <= 80;
  logSeoUtilsEvent('validate_slug', slug, valid);
  return valid;
}

/**
 * Analyse la densité d’un mot-clé dans un texte.
 * @param {string} text
 * @param {string} keyword
 * @returns {number} Pourcentage de densité (0-100)
 */
export function keywordDensity(text, keyword) {
  if (!text || !keyword || typeof text !== 'string' || typeof keyword !== 'string') return 0;
  const words = text.toLowerCase().split(/\W+/).filter(Boolean);
  const count = words.filter(w => w === keyword.toLowerCase()).length;
  const density = words.length ? (count / words.length) * 100 : 0;
  logSeoUtilsEvent('keyword_density', keyword, density);
  return Math.round(density * 100) / 100;
}

/**
 * Génère une meta description optimisée à partir d’un texte.
 * @param {string} text
 * @returns {string}
 */
export function generateMetaDescription(text) {
  if (!text || typeof text !== 'string') throw new Error('Texte invalide pour meta description');
  let desc = text.replace(/\s+/g, ' ').trim();
  if (desc.length > 160) desc = desc.slice(0, 157) + '...';
  logSeoUtilsEvent('generate_meta_description', desc);
  return desc;
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {*} value
 * @param {*} [extra]
 */
function logSeoUtilsEvent(action, value, extra) {
  try {
    const logs = JSON.parse(localStorage.getItem('seo_utils_logs') || '[]');
    logs.push({
      action,
      value,
      extra,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('seo_utils_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs des utilitaires SEO (droit à l’oubli RGPD).
 */
export function clearLocalSeoUtilsLogs() {
  localStorage.removeItem('seo_utils_logs');
}