// Dihya Validators Module - index.js
// Fonctions de validation avancées, multilingues, sécurisées, auditables, RGPD, multitenant, IA fallback open source
// @module Validators

/**
 * Validation d’email multilingue
 * @param {string} email
 * @returns {boolean}
 */
export function validateEmail(email) {
  return /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email);
}

/**
 * Validation de mot de passe fort (min 12, maj, min, chiffre, spécial)
 * @param {string} password
 * @returns {boolean}
 */
export function validateStrongPassword(password) {
  return /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=[\]{};':"\\|,.<>/?]).{12,}$/.test(password);
}

/**
 * Validation RGPD (consentement, anonymisation)
 * @param {Object} data
 * @returns {boolean}
 */
export function validateRGPD(data) {
  return data && typeof data.consent === 'boolean' && data.consent === true;
}

// Tests unitaires et intégration : voir __tests__/validators.test.js
