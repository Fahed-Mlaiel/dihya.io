// src/constants/constants.js
/**
 * Constantes globales Dihya Coding (sécurité, i18n, rôles, SEO, plugins)
 * @module src/constants/constants.js
 */
export const SUPPORTED_LANGUAGES = ['fr', 'en', 'ar', 'ber', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es'];
export const ROLES = ['admin', 'user', 'guest'];
export const JWT_SECRET = process.env.JWT_SECRET || 'CHANGE_ME_ULTRA_SECURE';
export const CORS_OPTIONS = {
  origin: process.env.CORS_ORIGIN || '*',
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowedHeaders: ['Authorization', 'Content-Type', 'Accept-Language'],
  credentials: true,
};
export const SEO_ROBOTS = 'User-agent: *\nDisallow:';
export const PLUGIN_PATH = '/plugins';
export const AUDIT_LOG_PATH = '/logs/audit.log';
export const WAF_CONFIG = {
  enabled: true,
  rules: ['anti-ddos', 'sql-injection', 'xss', 'csrf'],
};
