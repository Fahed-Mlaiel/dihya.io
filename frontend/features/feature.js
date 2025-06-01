// src/features/feature.js
/**
 * Module de gestion des fonctionnalités avancées Dihya Coding (i18n, sécurité, plugins, audit, IA)
 * @module src/features/feature.js
 */
import { ROLES, SUPPORTED_LANGUAGES } from '../constants/constants';

/**
 * Vérifie si une fonctionnalité est activée pour un métier donné
 * @param {string} metierKey
 * @param {string} feature
 * @returns {boolean}
 */
export function isFeatureEnabled(metierKey, feature) {
  // ... logique avancée (exemple) ...
  if (metierKey === 'vr_ar' && feature === 'ai') return true;
  // ...
  return false;
}

/**
 * Retourne la liste des langues supportées
 * @returns {string[]}
 */
export function getSupportedLanguages() {
  return SUPPORTED_LANGUAGES;
}

/**
 * Vérifie le rôle utilisateur
 * @param {string} role
 * @returns {boolean}
 */
export function isValidRole(role) {
  return ROLES.includes(role);
}
