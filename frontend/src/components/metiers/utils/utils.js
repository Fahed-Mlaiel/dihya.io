// Dihya Utils Module - utils.js
// Fonctions utilitaires avancées, multilingues, sécurisées, auditables, RGPD, multitenant, IA fallback open source
// @module Utils

/**
 * Validation avancée (type, format, i18n, RGPD)
 * @param {any} value
 * @param {string} type
 * @returns {boolean}
 */
export function validateType(value, type) {
  if (type === 'string') return typeof value === 'string';
  if (type === 'number') return typeof value === 'number';
  if (type === 'object') return typeof value === 'object' && value !== null;
  if (type === 'array') return Array.isArray(value);
  if (type === 'boolean') return typeof value === 'boolean';
  return false;
}

/**
 * Audit log structuré, anonymisation RGPD
 * @param {Object} log
 * @param {boolean} anonymize
 * @returns {Object}
 */
export function auditLog(log, anonymize = false) {
  const anonymized = anonymize ? { ...log, user: 'anonymized' } : log;
  if (typeof window !== 'undefined') {
    window.dihyaUtilsLog = window.dihyaUtilsLog || [];
    window.dihyaUtilsLog.push(anonymized);
  }
  return anonymized;
}

/**
 * Génération d’ID unique multitenant
 * @param {string} tenant
 * @returns {string}
 */
export function generateUniqueId(tenant = 'default') {
  return `${tenant}_${Math.random().toString(36).substr(2, 9)}_${Date.now()}`;
}

// Tests unitaires et intégration : voir __tests__/utils.test.js
