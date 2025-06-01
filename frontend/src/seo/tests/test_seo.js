/**
 * @file test_seo.js
 * @description Tests SEO pour Dihya Coding : validation des balises, titres, descriptions, accessibilité, indexabilité, robustesse, conformité RGPD, auditabilité, extensibilité et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Teste la présence et la validité de la balise <title>.
 * @param {string} html
 * @returns {object} Résultat { name, success, error, timestamp }
 */
export function testTitleTag(html) {
  const match = html.match(/<title>(.*?)<\/title>/i);
  const valid = !!match && match[1].trim().length > 0;
  if (hasConsent()) {
    logSeoTestEvent('test_title_tag', { valid, title: anonymizeTitle(match ? match[1] : ''), timestamp: new Date().toISOString() });
  }
  return {
    name: 'Balise <title>',
    success: valid,
    error: valid ? null : 'Balise <title> absente ou vide',
    timestamp: new Date().toISOString()
  };
}

/**
 * Teste la présence et la validité de la meta description.
 * @param {string} html
 * @returns {object} Résultat { name, success, error, timestamp }
 */
export function testMetaDescription(html) {
  const match = html.match(/<meta\s+name=["']description["']\s+content=["']([^"']+)["']/i);
  const valid = !!match && match[1].trim().length > 0;
  if (hasConsent()) {
    logSeoTestEvent('test_meta_description', { valid, description: anonymizeDescription(match ? match[1] : ''), timestamp: new Date().toISOString() });
  }
  return {
    name: 'Meta description',
    success: valid,
    error: valid ? null : 'Meta description absente ou vide',
    timestamp: new Date().toISOString()
  };
}

/**
 * Teste la présence d’une balise canonical.
 * @param {string} html
 * @returns {object} Résultat { name, success, error, timestamp }
 */
export function testCanonicalTag(html) {
  const match = html.match(/<link\s+rel=["']canonical["']\s+href=["']([^"']+)["']/i);
  const valid = !!match && match[1].startsWith('https://');
  if (hasConsent()) {
    logSeoTestEvent('test_canonical_tag', { valid, canonical: anonymizeCanonical(match ? match[1] : ''), timestamp: new Date().toISOString() });
  }
  return {
    name: 'Balise canonical',
    success: valid,
    error: valid ? null : 'Balise canonical absente ou invalide',
    timestamp: new Date().toISOString()
  };
}

/**
 * Teste la présence d’attributs alt sur les images.
 * @param {string} html
 * @returns {object} Résultat { name, success, error, timestamp }
 */
export function testImagesAlt(html) {
  const images = [...html.matchAll(/<img\s+[^>]*>/gi)];
  const allHaveAlt = images.every(img => /alt\s*=\s*["'][^"']+["']/i.test(img[0]));
  if (hasConsent()) {
    logSeoTestEvent('test_images_alt', { total: images.length, allHaveAlt, timestamp: new Date().toISOString() });
  }
  return {
    name: 'Attribut alt sur images',
    success: allHaveAlt,
    error: allHaveAlt ? null : 'Certaines images sans attribut alt',
    timestamp: new Date().toISOString()
  };
}

/**
 * Teste la présence d’un fichier robots.txt (simulation).
 * @param {string[]} files - Liste des fichiers du projet
 * @returns {object} Résultat { name, success, error, timestamp }
 */
export function testRobotsTxt(files) {
  const found = files.includes('robots.txt');
  if (hasConsent()) {
    logSeoTestEvent('test_robots_txt', { found, timestamp: new Date().toISOString() });
  }
  return {
    name: 'robots.txt',
    success: found,
    error: found ? null : 'robots.txt absent',
    timestamp: new Date().toISOString()
  };
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('test_seo_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logSeoTestEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('test_seo_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('test_seo_logs', JSON.stringify(logs));
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
 * Efface les logs SEO (droit à l’oubli RGPD).
 */
export function clearLocalSeoTestLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('test_seo_logs');
  }
}

/**
 * Lance tous les tests SEO de base sur un HTML donné.
 * @param {string} html
 * @param {string[]} files
 * @returns {object} Rapport { total, passed, failed, results, timestamp }
 */
export function runSeoTests(html, files = []) {
  const tests = [
    testTitleTag,
    testMetaDescription,
    testCanonicalTag,
    testImagesAlt
  ];
  const results = tests.map(fn => fn(html));
  results.push(testRobotsTxt(files));
  const passed = results.filter(r => r.success).length;
  const failed = results.length - passed;
  return {
    total: results.length,
    passed,
    failed,
    results,
    timestamp: new Date().toISOString()
  };
}

// Exécution automatique si appelé directement (pour Node.js ou navigateur)
if (typeof window === 'undefined' && require.main === module) {
  // eslint-disable-next-line no-console
  console.log(JSON.stringify(runSeoTests('<title>Dihya Coding</title><meta name="description" content="Plateforme Dihya"><link rel="canonical" href="https://dihya.app/"><img src="logo.png" alt="Logo Dihya">', ['robots.txt']), null, 2));
}