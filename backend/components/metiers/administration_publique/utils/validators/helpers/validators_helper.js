// validators_helper.js
// Helper validators JS pour Threed – exemple clé en main

/**
 * Vérifie si une chaîne est un email valide
 * @param {string} email
 * @returns {boolean}
 */
function isValidEmail(email) {
  return /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email);
}

module.exports = { isValidEmail };
