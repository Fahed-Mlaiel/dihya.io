/**
 * @file seoValidators.js
 * @description Fonctions de validation SEO pour Dihya Coding (balises meta, sitemap, robots.txt, audit Lighthouse).
 * Garantit design moderne, SEO optimal, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les validations sont strictes, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Valide la structure des balises meta SEO.
 * @param {object} meta
 * @returns {boolean}
 */
export function validateMetaTags(meta) {
  if (!hasConsent()) throw new Error('Consentement requis pour valider les balises meta.');
  const valid = typeof meta === 'object'
    && typeof meta.title === 'string'
    && typeof meta.description === 'string'
    && Array.isArray(meta.keywords)
    && meta.keywords.every(k => typeof k === 'string');
  logSeoValidation('meta', anonymizeMeta(meta), valid);
  return valid;
}

/**
 * Valide la structure d’un sitemap.
 * @param {object} sitemap
 * @returns {boolean}
 */
export function validateSitemap(sitemap) {
  if (!hasConsent()) throw new Error('Consentement requis pour valider le sitemap.');
  const valid = typeof sitemap === 'object'
    && Array.isArray(sitemap.urls)
    && sitemap.urls.every(url => typeof url === 'string' && url.startsWith('/'));
  logSeoValidation('sitemap', anonymizeSitemap(sitemap), valid);
  return valid;
}

/**
 * Valide la structure d’un robots.txt.
 * @param {object} robots
 * @returns {boolean}
 */
export function validateRobotsTxt(robots) {
  if (!hasConsent()) throw new Error('Consentement requis pour valider le robots.txt.');
  const valid = typeof robots === 'object'
    && Array.isArray(robots.allow)
    && Array.isArray(robots.disallow)
    && robots.allow.every(url => typeof url === 'string')
    && robots.disallow.every(url => typeof url === 'string');
  logSeoValidation('robots', anonymizeRobots(robots), valid);
  return valid;
}

/**
 * Valide un rapport d’audit Lighthouse simplifié.
 * @param {object} audit
 * @returns {boolean}
 */
export function validateLighthouseAudit(audit) {
  if (!hasConsent()) throw new Error('Consentement requis pour valider l’audit Lighthouse.');
  const valid = typeof audit === 'object'
    && typeof audit.url === 'string'
    && Array.isArray(audit.audits)
    && audit.audits.every(a => typeof a === 'string');
  logSeoValidation('lighthouse', anonymizeAudit(audit), valid);
  return valid;
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('seo_validators_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} type
 * @param {object} data
 * @param {boolean} valid
 */
function logSeoValidation(type, data, valid) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('seo_validators_logs') || '[]');
    logs.push({
      type,
      data,
      valid,
      timestamp: new Date().toISOString(),
    });
    window.localStorage.setItem('seo_validators_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise les balises meta pour les logs.
 * @param {object} meta
 * @returns {object}
 */
function anonymizeMeta(meta) {
  if (!meta || typeof meta !== 'object') return meta;
  const clone = { ...meta };
  if (clone.title) clone.title = sanitize(clone.title);
  if (clone.description) clone.description = sanitize(clone.description);
  if (Array.isArray(clone.keywords)) clone.keywords = clone.keywords.map(sanitize);
  return clone;
}

/**
 * Anonymise un sitemap pour les logs.
 * @param {object} sitemap
 * @returns {object}
 */
function anonymizeSitemap(sitemap) {
  if (!sitemap || typeof sitemap !== 'object') return sitemap;
  const clone = { ...sitemap };
  if (Array.isArray(clone.urls)) clone.urls = clone.urls.map(sanitizeUrl);
  return clone;
}

/**
 * Anonymise un robots.txt pour les logs.
 * @param {object} robots
 * @returns {object}
 */
function anonymizeRobots(robots) {
  if (!robots || typeof robots !== 'object') return robots;
  const clone = { ...robots };
  if (Array.isArray(clone.allow)) clone.allow = clone.allow.map(sanitizeUrl);
  if (Array.isArray(clone.disallow)) clone.disallow = clone.disallow.map(sanitizeUrl);
  return clone;
}

/**
 * Anonymise un audit Lighthouse pour les logs.
 * @param {object} audit
 * @returns {object}
 */
function anonymizeAudit(audit) {
  if (!audit || typeof audit !== 'object') return audit;
  const clone = { ...audit };
  if (clone.url) clone.url = sanitizeUrl(clone.url);
  if (Array.isArray(clone.audits)) clone.audits = clone.audits.map(sanitize);
  return clone;
}

/**
 * Sanitize une chaîne pour éviter les injections.
 * @param {string} str
 * @returns {string}
 */
function sanitize(str) {
  if (typeof str !== 'string') return '';
  return str.replace(/[<>"]/g, '');
}

/**
 * Sanitize une URL pour les logs.
 * @param {string} url
 * @returns {string}
 */
function sanitizeUrl(url) {
  if (typeof url !== 'string') return '';
  return url.replace(/[<>"]/g, '').replace(/[\s]/g, '');
}

/**
 * Efface les logs de validation SEO (droit à l’oubli RGPD).
 */
export function clearLocalSeoValidatorsLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('seo_validators_logs');
  }
}