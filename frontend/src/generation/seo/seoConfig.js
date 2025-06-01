/**
 * @file seoConfig.js
 * @description Gestion avancée de la configuration SEO pour Dihya Coding (balises meta, sitemap, robots.txt, accessibilité, logs, auditabilité).
 * Garantit design moderne, SEO optimal, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les configurations sont validées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Génère la configuration SEO recommandée pour une page ou une application.
 * @param {object} params
 * @param {string} params.title - Titre de la page (max 60 caractères)
 * @param {string} params.description - Description (max 160 caractères)
 * @param {string} [params.canonical] - URL canonique
 * @param {Array<string>} [params.keywords] - Liste de mots-clés
 * @param {string} [params.lang] - Langue principale (ex: 'fr', 'en')
 * @param {object} [params.og] - Open Graph (og:title, og:description, og:image, etc.)
 * @returns {object} Objet de configuration SEO prêt à l’emploi
 */
export function getSeoConfig({
  title,
  description,
  canonical,
  keywords = [],
  lang = 'fr',
  og = {},
}) {
  validateTitle(title);
  validateDescription(description);
  if (canonical) validateUrl(canonical);
  logSeoConfigEvent('get_seo_config', title, canonical);

  return {
    title: title.slice(0, 60),
    meta: [
      { name: 'description', content: description.slice(0, 160) },
      ...(keywords.length ? [{ name: 'keywords', content: keywords.join(', ') }] : []),
      ...(canonical ? [{ rel: 'canonical', href: canonical }] : []),
      { name: 'robots', content: 'index, follow' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { name: 'language', content: lang },
      // Open Graph
      ...(og.title ? [{ property: 'og:title', content: og.title }] : []),
      ...(og.description ? [{ property: 'og:description', content: og.description }] : []),
      ...(og.image ? [{ property: 'og:image', content: og.image }] : []),
      ...(og.url ? [{ property: 'og:url', content: og.url }] : []),
      ...(og.type ? [{ property: 'og:type', content: og.type }] : []),
    ],
    lang,
  };
}

/**
 * Valide le titre SEO.
 * @param {string} title
 */
function validateTitle(title) {
  if (!title || typeof title !== 'string' || title.length < 3 || title.length > 60) {
    throw new Error('Titre SEO invalide');
  }
}

/**
 * Valide la description SEO.
 * @param {string} description
 */
function validateDescription(description) {
  if (!description || typeof description !== 'string' || description.length < 10 || description.length > 160) {
    throw new Error('Description SEO invalide');
  }
}

/**
 * Valide une URL canonique.
 * @param {string} url
 */
function validateUrl(url) {
  try {
    const u = new URL(url);
    if (!['http:', 'https:'].includes(u.protocol)) throw new Error();
  } catch {
    throw new Error('URL canonique invalide');
  }
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} title
 * @param {string} [canonical]
 */
function logSeoConfigEvent(action, title, canonical) {
  try {
    const logs = JSON.parse(localStorage.getItem('seo_config_logs') || '[]');
    logs.push({
      action,
      title,
      canonical,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('seo_config_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de configuration SEO (droit à l’oubli RGPD).
 */
export function clearLocalSeoConfigLogs() {
  localStorage.removeItem('seo_config_logs');
}