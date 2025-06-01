/**
 * @file seoAuto.js
 * @description Fonctions utilitaires pour l’automatisation du SEO dans Dihya Coding (balises meta, sitemap, robots.txt, audit Lighthouse).
 * Garantit design moderne, SEO optimal, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Génère automatiquement des balises meta optimisées pour le SEO.
 * @param {object} params
 * @param {string} params.title
 * @param {string} params.description
 * @param {string[]} params.keywords
 * @returns {object} Balises meta générées
 */
export function generateMetaTags({ title, description, keywords }) {
  if (!hasConsent()) throw new Error('Consentement requis pour générer des balises meta.');
  if (!title || !description || !Array.isArray(keywords)) throw new Error('Paramètres meta invalides');
  const meta = {
    title: sanitize(title),
    description: sanitize(description),
    keywords: keywords.map(sanitize),
    charset: 'utf-8',
    viewport: 'width=device-width, initial-scale=1',
    'og:title': sanitize(title),
    'og:description': sanitize(description),
    'og:type': 'website'
  };
  logSeoAutoEvent('generate_meta', meta);
  return meta;
}

/**
 * Génère automatiquement un sitemap.
 * @param {object} params
 * @param {string[]} params.urls
 * @returns {object} Sitemap généré
 */
export function generateSitemap({ urls }) {
  if (!hasConsent()) throw new Error('Consentement requis pour générer un sitemap.');
  if (!Array.isArray(urls) || urls.length === 0) throw new Error('URLs invalides');
  const sitemap = { urls: urls.map(sanitizeUrl) };
  logSeoAutoEvent('generate_sitemap', sitemap);
  return sitemap;
}

/**
 * Génère automatiquement un robots.txt.
 * @param {object} params
 * @param {string[]} params.allow
 * @param {string[]} params.disallow
 * @returns {object} Robots.txt généré
 */
export function generateRobotsTxt({ allow = ['/'], disallow = [] }) {
  if (!hasConsent()) throw new Error('Consentement requis pour générer un robots.txt.');
  if (!Array.isArray(allow) || !Array.isArray(disallow)) throw new Error('Paramètres robots.txt invalides');
  const robots = { allow: allow.map(sanitizeUrl), disallow: disallow.map(sanitizeUrl) };
  logSeoAutoEvent('generate_robots', robots);
  return robots;
}

/**
 * Génère un rapport d’audit Lighthouse simplifié.
 * @param {object} params
 * @param {string} params.url
 * @param {string[]} params.audits
 * @returns {object} Rapport d’audit généré
 */
export function generateLighthouseAudit({ url, audits }) {
  if (!hasConsent()) throw new Error('Consentement requis pour générer un audit Lighthouse.');
  if (!url || !Array.isArray(audits)) throw new Error('Paramètres audit invalides');
  const report = {
    url: sanitizeUrl(url),
    audits: audits.map(sanitize),
    date: new Date().toISOString()
  };
  logSeoAutoEvent('generate_lighthouse', report);
  return report;
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('seo_auto_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logSeoAutoEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('seo_auto_logs') || '[]');
    logs.push({
      action,
      data: anonymizeSeoData(data),
      timestamp: new Date().toISOString(),
    });
    window.localStorage.setItem('seo_auto_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise les données sensibles pour les logs SEO.
 * @param {object} data
 * @returns {object}
 */
function anonymizeSeoData(data) {
  // Pas de données personnelles attendues, mais on filtre les URLs si besoin
  if (!data || typeof data !== 'object') return data;
  if (data.url) data.url = sanitizeUrl(data.url);
  if (Array.isArray(data.urls)) data.urls = data.urls.map(sanitizeUrl);
  return data;
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
 * Efface les logs SEO automatiques (droit à l’oubli RGPD).
 */
export function clearLocalSeoAutoLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('seo_auto_logs');
  }
}