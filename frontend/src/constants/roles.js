/**
 * @file roles.js
 * @description Constantes des rôles utilisateurs pour Dihya Coding.
 * Garantit sécurité, conformité RGPD, auditabilité, extensibilité et documentation claire.
 * Aucun secret, donnée personnelle ou sensible n’est stocké ici.
 */

/**
 * Liste des rôles métiers disponibles dans l’application.
 * @readonly
 * @enum {string}
 */
export const USER_ROLES = Object.freeze({
  ADMIN: 'admin',           // Accès total, gestion des utilisateurs et paramètres
  EDITOR: 'editor',         // Peut créer, modifier, supprimer des projets
  VIEWER: 'viewer',         // Accès en lecture seule aux projets
  AUDITOR: 'auditor',       // Accès aux logs, auditabilité, conformité
  GUEST: 'guest',           // Accès limité, pas de modification
});

/**
 * Description des rôles pour affichage UI et documentation.
 * @type {Object.<string, string>}
 */
export const USER_ROLES_DESCRIPTIONS = {
  admin: 'Administrateur – gestion complète de la plateforme.',
  editor: 'Éditeur – création et modification de projets.',
  viewer: 'Lecteur – consultation des projets.',
  auditor: 'Auditeur – accès aux journaux et à la conformité.',
  guest: 'Invité – accès limité, consultation restreinte.',
};

/**
 * Liste des rôles autorisés à effectuer des actions sensibles.
 * @type {string[]}
 */
export const SENSITIVE_ACTION_ROLES = ['admin', 'auditor'];

/**
 * Vérifie si un rôle est valide.
 * @param {string} role
 * @returns {boolean}
 */
export function isValidRole(role) {
  return Object.values(USER_ROLES).includes(role);
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} role
 */
export function logRoleEvent(action, role) {
  try {
    const logs = JSON.parse(localStorage.getItem('role_logs') || '[]');
    logs.push({
      action,
      role,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('role_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de rôles locaux (droit à l’oubli RGPD).
 */
export function clearLocalRoleLogs() {
  localStorage.removeItem('role_logs');
}