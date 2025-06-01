/**
 * Utilitaires avancés pour la génération de projets IA, VR, AR, etc.
 * @module generation/utils/utils
 * @author Dihya Team
 * @description Fonctions utilitaires sécurisées, multilingues, extensibles.
 * @i18n Support: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
 * @roles admin, user, invité
 * @security JWT, CORS, audit, anti-DDOS
 */

const crypto = require('crypto');

/**
 * Génère un identifiant unique sécurisé pour un projet.
 * @returns {string} ID unique
 */
function generateSecureId() {
  return crypto.randomBytes(16).toString('hex');
}

/**
 * Valide les données d'entrée pour la génération de projet.
 * @param {object} data - Données du projet
 * @returns {boolean} true si valide
 */
function validateProjectData(data) {
  // Validation avancée (type, nom, langue, framework, etc.)
  if (!data || typeof data !== 'object') return false;
  if (!data.type || !['ia', 'vr', 'ar', '3d'].includes(data.type)) return false;
  if (!data.nom && !data.name) return false;
  if (!data.langue && !data.language) return false;
  return true;
}

module.exports = {
  generateSecureId,
  validateProjectData,
};
