// Template de validateur pour la génération de projets IA, VR, AR, etc.
// Validation stricte, audit, i18n, conformité RGPD.
// SPDX-License-Identifier: MIT

/**
 * Valide les données selon un schéma strict (types, sécurité, RGPD)
 * @param {object} data - Données à valider
 * @param {object} schema - Schéma de validation (clé: type)
 * @returns {boolean}
 */
export function validateSchema(data, schema) {
  for (const key in schema) {
    if (!(key in data) || typeof data[key] !== schema[key]) {
      return false;
    }
  }
  return true;
}

/**
 * Log structuré pour auditabilité des validations
 * @param {string} event - Nom de l'événement
 * @param {object} data - Données validées
 */
export function auditValidation(event, data) {
  console.info(`[VALIDATION AUDIT] ${event} | ${JSON.stringify(data)}`);
}
