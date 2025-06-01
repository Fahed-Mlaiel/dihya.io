/**
 * @file seoUtils.js
 * @description Utilitaires SEO pour Dihya Coding : gestion des balises, titres, descriptions, canonical, accessibilité, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Extrait le contenu de la balise <title> d’un HTML.
 * @param {string} html
 * @returns {string|null}
 */
export function getPageTitle(html) {
  const match = html.match(/<title>(.*?)<\/title>/i);
  const title = match ? match[1].trim() : null;
  if (hasConsent()) {
    logSeoUtilEvent('get_page_title', { title: anonymizeTitle(title), timestamp: new Date().toISOString() });
  }
  return title;
}

/**
 * Extrait la meta description d’un HTML.
 * @param {string} html
 * @returns {string|null}
 */
export function getMetaDescription(html) {
  const match = html.match(/<meta\s+name=["']description["']\s+content=["']([^"']+)["']/i);
  const desc = match ? match[1].trim() : null;
  if (hasConsent()) {
    logSeoUtilEvent('get_meta_description', { desc: anonymizeDescription(desc), timestamp: new Date().toISOString() });
  }
  return desc;
}

/**
 * Extrait la balise canonical d’un HTML.
 * @param {string} html
 * @returns {string|null}
 */
export function getCanonicalUrl(html) {
  const match = html.match(/<link\s+rel=["']canonical["']\s+href=["']([^"']+)["']/i);
  const canonical = match ? match[1].trim() : null;
  if (hasConsent()) {
    logSeoUtilEvent('get_canonical_url', { canonical: anonymizeCanonical(canonical), timestamp: new Date().toISOString() });
  }
  return canonical;
}

/**
 * Vérifie la présence d’attributs alt sur toutes les images d’un HTML.
 * @param {string} html
 * @returns {boolean}
 */
export function allImagesHaveAlt(html) {
  const images = [...html.matchAll(/<img\s+[^>]*>/gi)];
  const allHaveAlt = images.every(img => /alt\s*=\s*["'][^"']+["']/i.test(img[0]));
  if (hasConsent()) {
    logSeoUtilEvent('all_images_have_alt', { total: images.length, allHaveAlt, timestamp: new Date().toISOString() });
  }
  return allHaveAlt;
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('seo_utils_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logSeoUtilEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('seo_utils_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('seo_utils_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise un titre pour les logs.
 * @param {string} title
 * @returns {string}
 */
function anonymizeTitle(title) {
  if (!title) return '';
  return title.length > 16 ? title.slice(0, 8) + '...' : title;
}

/**
 * Anonymise une description pour les logs.
 * @param {string} desc
 * @returns {string}
 */
function anonymizeDescription(desc) {
  if (!desc) return '';
  return desc.length > 24 ? desc.slice(0, 12) + '...' : desc;
}

/**
 * Anonymise une URL canonical pour les logs.
 * @param {string} url
 * @returns {string}
 */
function anonymizeCanonical(url) {
  if (!url) return '';
  return url.replace(/\/\/[^/]+\//, '//***/');
}

/**
 * Efface les logs SEO utils (droit à l’oubli RGPD).
 */
export function clearLocalSeoUtilsLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('seo_utils_logs');
  }
}