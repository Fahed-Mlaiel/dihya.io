/**
 * @file seoService.js
 * @description Service centralisé SEO pour Dihya Coding : gestion dynamique des balises meta, titres, descriptions, canonical, robots, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Définit dynamiquement les balises meta SEO sur la page.
 * @param {object} params
 * @param {string} params.title - Titre de la page
 * @param {string} params.description - Description meta
 * @param {string} [params.canonical] - URL canonical
 * @param {string} [params.robots] - Valeur robots (ex: 'index, follow')
 * @param {object} [params.og] - Open Graph (type, title, description, url, image)
 * @param {object} [params.twitter] - Twitter Card (card, site, title, description, image)
 * @param {object} [params.options] - Options avancées (logs, RGPD)
 * @returns {boolean} Succès de l’opération
 */
export function setMetaTags({
  title,
  description,
  canonical,
  robots,
  og = {},
  twitter = {},
  options = {}
}) {
  if (!hasConsent()) return false;
  if (typeof document === 'undefined') return false;

  try {
    if (title) setOrUpdateTag('title', title);
    if (description) setOrUpdateMeta('description', description);
    if (canonical) setOrUpdateLink('canonical', canonical);
    if (robots) setOrUpdateMeta('robots', robots);

    // Open Graph
    Object.entries(og).forEach(([k, v]) => {
      if (v) setOrUpdateMeta('og:' + k, v, 'property');
    });

    // Twitter Card
    Object.entries(twitter).forEach(([k, v]) => {
      if (v) setOrUpdateMeta('twitter:' + k, v, 'name');
    });

    if (options.log !== false) {
      logSeoServiceEvent('set_meta_tags', {
        title: anonymizeTitle(title),
        canonical: anonymizeCanonical(canonical),
        timestamp: new Date().toISOString()
      });
    }
    return true;
  } catch {
    return false;
  }
}

/**
 * Ajoute ou met à jour une balise <title>.
 * @param {string} tagName
 * @param {string} value
 */
function setOrUpdateTag(tagName, value) {
  let tag = document.querySelector(tagName);
  if (!tag) {
    tag = document.createElement(tagName);
    document.head.appendChild(tag);
  }
  tag.textContent = sanitize(value);
}

/**
 * Ajoute ou met à jour une balise <meta>.
 * @param {string} name
 * @param {string} value
 * @param {string} [attr='name'] - Attribut à utiliser ('name' ou 'property')
 */
function setOrUpdateMeta(name, value, attr = 'name') {
  let meta = document.head.querySelector(`meta[${attr}="${name}"]`);
  if (!meta) {
    meta = document.createElement('meta');
    meta.setAttribute(attr, name);
    document.head.appendChild(meta);
  }
  meta.setAttribute('content', sanitize(value));
}

/**
 * Ajoute ou met à jour une balise <link rel="canonical">.
 * @param {string} rel
 * @param {string} href
 */
function setOrUpdateLink(rel, href) {
  let link = document.head.querySelector(`link[rel="${rel}"]`);
  if (!link) {
    link = document.createElement('link');
    link.setAttribute('rel', rel);
    document.head.appendChild(link);
  }
  link.setAttribute('href', sanitize(href));
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('seo_service_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logSeoServiceEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('seo_service_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('seo_service_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Sanitize une chaîne pour éviter l’injection.
 * @param {string} str
 * @returns {string}
 */
function sanitize(str) {
  return String(str).replace(/[\r\n<>]/g, '');
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
 * Anonymise une URL canonical pour les logs.
 * @param {string} url
 * @returns {string}
 */
function anonymizeCanonical(url) {
  if (!url) return '';
  return url.replace(/\/\/[^/]+\//, '//***/');
}

/**
 * Efface les logs SEO service (droit à l’oubli RGPD).
 */
export function clearLocalSeoServiceLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('seo_service_logs');
  }
}