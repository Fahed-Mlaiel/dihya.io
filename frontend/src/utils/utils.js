// utils.js - Utilitaires avancés pour Dihya Coding
// Internationalisation dynamique, sécurité, validation, audit, SEO, plugins, etc.
// Compatible Node.js, navigateur, Codespaces, CI/CD

/**
 * Traduction dynamique (i18n) multilingue
 * @param {string} key - Clé de traduction
 * @param {string} lang - Code langue (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, etc.)
 * @param {object} [params] - Paramètres dynamiques
 * @returns {string}
 */
export function t(key, lang = 'fr', params = {}) {
  const translations = {
    fr: { hello: 'Bonjour', project: 'Projet IA/VR/AR' },
    en: { hello: 'Hello', project: 'AI/VR/AR Project' },
    ar: { hello: 'مرحبا', project: 'مشروع الذكاء الاصطناعي/الواقع الافتراضي/المعزز' },
    de: { hello: 'Hallo', project: 'KI/VR/AR Projekt' },
    zh: { hello: '你好', project: '人工智能/虚拟现实/增强现实项目' },
    ja: { hello: 'こんにちは', project: 'AI/VR/ARプロジェクト' },
    ko: { hello: '안녕하세요', project: 'AI/VR/AR 프로젝트' },
    nl: { hello: 'Hallo', project: 'AI/VR/AR Project' },
    he: { hello: 'שלום', project: 'פרויקט בינה מלאכותית/VR/AR' },
    fa: { hello: 'سلام', project: 'پروژه هوش مصنوعی/واقعیت مجازی/افزوده' },
    hi: { hello: 'नमस्ते', project: 'एआई/वीआर/एआर परियोजना' },
    es: { hello: 'Hola', project: 'Proyecto IA/VR/AR' },
  };
  let str = (translations[lang] && translations[lang][key]) || key;
  Object.keys(params).forEach(k => {
    str = str.replace(`{${k}}`, params[k]);
  });
  return str;
}

/**
 * Validation d'entrée sécurisée (XSS, injection, etc.)
 * @param {string} input
 * @returns {string}
 */
export function sanitize(input) {
  return String(input).replace(/[<>"'`]/g, '');
}

/**
 * Génération de token JWT sécurisé
 * @param {object} payload
 * @param {string} secret
 * @returns {string}
 */
export function generateJWT(payload, secret) {
  // Utilise la lib jsonwebtoken côté Node.js
  if (typeof window === 'undefined') {
    const jwt = require('jsonwebtoken');
    return jwt.sign(payload, secret, { algorithm: 'HS512', expiresIn: '1h' });
  }
  throw new Error('JWT non supporté côté client');
}

/**
 * Audit log structuré (RGPD, conformité)
 * @param {string} action
 * @param {object} details
 */
export function auditLog(action, details = {}) {
  if (typeof window === 'undefined') {
    const fs = require('fs');
    const log = { timestamp: new Date().toISOString(), action, ...details };
    fs.appendFileSync('audit.log', JSON.stringify(log) + '\n');
  } else {
    // Envoi à un endpoint API si côté client
    fetch('/api/audit', { method: 'POST', body: JSON.stringify({ action, details }) });
  }
}

/**
 * Génération de sitemap dynamique (SEO)
 * @param {Array<string>} routes
 * @returns {string}
 */
export function generateSitemap(routes) {
  return `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n` +
    routes.map(route => `<url><loc>${route}</loc></url>`).join('\n') +
    '\n</urlset>';
}

/**
 * Génération de robots.txt (SEO)
 * @param {Array<string>} allow
 * @param {Array<string>} disallow
 * @returns {string}
 */
export function generateRobots(allow = ['*'], disallow = []) {
  return `User-agent: *\nAllow: ${allow.join(', ')}\nDisallow: ${disallow.join(', ')}\n`;
}

/**
 * Chargement dynamique de plugins (extensible)
 * @param {string} pluginName
 * @returns {Promise<any>}
 */
export async function loadPlugin(pluginName) {
  if (typeof window === 'undefined') {
    return import(`../../plugins/${pluginName}/index.js`);
  } else {
    return import(`/plugins/${pluginName}/index.js`);
  }
}

// ...autres utilitaires avancés (WAF, anti-DDOS, etc.) à intégrer selon besoin
