/**
 * Vérifie si une chaîne est un email valide
 * @param {string} email
 * @returns {boolean}
 */
export function isEmail(email) {
  return /^[\w-.]+@([\w-]+\.)+[\w-]{2,4}$/.test(email);
}

/**
 * Vérifie si une valeur est requise (non vide)
 * @param {any} value
 * @returns {boolean}
 */
export function isRequired(value) {
  return value !== undefined && value !== null && value !== '';
}

/**
 * Vérifie si un mot de passe est fort
 * @param {string} pwd
 * @returns {boolean}
 */
export function isStrongPassword(pwd) {
  return /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$/.test(pwd);
}
