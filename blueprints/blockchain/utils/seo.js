/**
 * Génère les balises meta principales pour le SEO
 * @param {Object} param0
 * @param {string} param0.title
 * @param {string} param0.description
 * @param {string} param0.lang
 * @returns {string}
 */
export function generateMeta({ title, description, lang }) {
  return '<title>' + title + '</title>\n<meta name="description" content="' + description + '" />\n<html lang="' + lang + '" />';
}

/**
 * Génère un sitemap XML à partir d'une liste d'URLs
 * @param {string[]} urls
 * @returns {string}
 */
export function generateSitemap(urls) {
  return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset>' + urls.map(u => '<url><loc>' + u + '</loc></url>').join('') + '</urlset>';
}

/**
 * Génère un fichier robots.txt
 * @param {boolean} allow
 * @returns {string}
 */
export function generateRobotsTxt(allow = true) {
  return allow ? 'User-agent: *\nAllow: /' : 'User-agent: *\nDisallow: /';
}

module.exports = { seo };
