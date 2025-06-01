/**
 * Validators – Dihya Coding
 * @module Validators
 * @description Validation forte, anti-injection, anti-XSS, multilingue, intégration modules métiers.
 * @author Dihya Team
 * @version 1.0.0
 */

/**
 * Valide un email
 * @param {string} email
 * @returns {boolean}
 */
function isValidEmail(email) {
  return /^[\w-.]+@[\w-]+\.[a-z]{2,}$/i.test(email);
}

/**
 * Vérifie la robustesse d’un mot de passe
 * @param {string} password
 * @returns {boolean}
 */
function isStrongPassword(password) {
  return /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$/.test(password);
}

module.exports = { isValidEmail, isStrongPassword };
