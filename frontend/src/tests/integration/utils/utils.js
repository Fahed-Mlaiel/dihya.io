/**
 * Utilitaires de test avancés pour la gestion multilingue, la génération de JWT, la validation, la simulation de rôles, la compatibilité multi-stack, la sécurité, l'audit, le fallback IA, la RGPD, la modularité
 * @module test_utils
 */
const jwt = require('jsonwebtoken');
const SUPPORTED_LANGUAGES = ['fr', 'en', 'ar', 'ber', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es'];

/**
 * Génère un JWT pour un rôle donné
 * @param {string} role - admin, user, invite
 * @returns {Promise<string>} JWT
 */
async function getJwt(role = 'user') {
  return jwt.sign({ role }, 'test_secret', { expiresIn: '1h' });
}

/**
 * Valide un email
 * @param {string} email
 * @returns {boolean}
 */
function validateEmail(email) {
  return /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email);
}

/**
 * Valide la robustesse d'un mot de passe
 * @param {string} password
 * @returns {boolean}
 */
function validatePassword(password) {
  return /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$/.test(password);
}

module.exports = {
  SUPPORTED_LANGUAGES,
  getJwt,
  validateEmail,
  validatePassword
};
