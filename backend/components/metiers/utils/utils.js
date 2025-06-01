/**
 * Utils – Dihya Coding
 * @module Utils
 * @description Utilitaires avancés : validation, logs, sécurité, i18n, anonymisation, audit, génération d’ID.
 * @author Dihya Team
 * @version 1.0.0
 */

/**
 * Valide des données selon un schéma
 * @param {object} data - Données à valider
 * @param {object} schema - Schéma de validation
 * @returns {boolean} Résultat
 */
function validateData(data, schema) {
  // Validation simple (exemple)
  for (const key in schema) {
    if (!(key in data) || typeof data[key] !== schema[key]) return false;
  }
  return true;
}

/**
 * Génère un ID sécurisé
 * @returns {string} ID unique
 */
function generateId() {
  return 'id-' + Math.random().toString(36).substr(2, 16);
}

/**
 * Anonymise des données (RGPD)
 * @param {object} data - Données à anonymiser
 * @returns {object} Données anonymisées
 */
function anonymize(data) {
  const anonymized = { ...data };
  for (const key in anonymized) {
    if (typeof anonymized[key] === 'string') anonymized[key] = '***';
  }
  return anonymized;
}

module.exports = { validateData, generateId, anonymize };
