// constants.js - Constantes globales Dihya Coding
/**
 * @fileoverview Constantes globales pour l’application Dihya Coding (sécurité, i18n, rôles, audit, SEO)
 * @author Dihya Coding
 * @version 1.0.0
 * @license MIT
 */

export const SUPPORTED_LANGUAGES = [
  'fr', 'en', 'ar', 'amazigh', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es'
];

export const ROLES = ['admin', 'user', 'invite'];

export const AUDIT_EVENTS = {
  ACCESS: 'access',
  LOGIN: 'login',
  LOGOUT: 'logout',
  CREATE: 'create',
  UPDATE: 'update',
  DELETE: 'delete',
  EXPORT: 'export',
};

export const SECURITY = {
  CORS: true,
  JWT: true,
  WAF: true,
  ANTI_DDOS: true,
};

export const SEO = {
  ENABLED: true,
  ROBOTS: '/robots.txt',
  SITEMAP: '/sitemap.xml',
};
