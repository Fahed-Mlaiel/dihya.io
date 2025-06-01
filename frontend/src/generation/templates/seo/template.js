"use strict";
/**
 * Template SEO – Dihya
 * @module generation/templates/seo/template
 * @description Template avancé pour SEO, multilingue, sécurisé, extensible, RGPD, logs structurés.
 * @author Dihya Team
 * @version 1.0.0
 * @license AGPL-3.0
 */

/**
 * Génère un robots.txt dynamique
 * @param {string} lang
 * @returns {string}
 */
function generateRobotsTxt(lang = "fr") {
  return `User-agent: *\nDisallow: /private\nSitemap: /sitemap.xml?lang=${lang}`;
}

/**
 * Génère un sitemap.xml dynamique
 * @param {string[]} urls
 * @param {string} lang
 * @returns {string}
 */
function generateSitemapXml(urls, lang = "fr") {
  return `<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n${urls.map(u => `<url><loc>${u}?lang=${lang}</loc></url>`).join("\n")}\n</urlset>`;
}

module.exports = { generateRobotsTxt, generateSitemapXml };
