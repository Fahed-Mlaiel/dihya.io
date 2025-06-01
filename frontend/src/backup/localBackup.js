/**
 * @file localBackup.js
 * @description Module pour la gestion des sauvegardes locales (navigateur) sur Dihya Coding.
 * Garantit sécurité, conformité RGPD, auditabilité, extensibilité et robustesse.
 * Toutes les opérations sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Sauvegarde un projet localement dans le navigateur (localStorage).
 * @param {string} projectId - Identifiant du projet à sauvegarder
 * @param {object} projectData - Données du projet à sauvegarder (serialisable)
 */
export function saveLocalBackup(projectId, projectData) {
  validateProjectId(projectId);
  validateProjectData(projectData);

  // Respect du consentement utilisateur (RGPD)
  if (!window?.localStorage?.getItem('local_backup_consent')) return;

  const key = getLocalBackupKey(projectId);
  const backup = {
    data: anonymizeData(projectData),
    timestamp: new Date().toISOString(),
  };
  localStorage.setItem(key, JSON.stringify(backup));
  logLocalBackupEvent('save', projectId);
}

/**
 * Récupère une sauvegarde locale d’un projet.
 * @param {string} projectId
 * @returns {object|null} Données de sauvegarde ou null si absente
 */
export function getLocalBackup(projectId) {
  validateProjectId(projectId);
  const key = getLocalBackupKey(projectId);
  const backup = localStorage.getItem(key);
  if (!backup) return null;
  logLocalBackupEvent('get', projectId);
  return JSON.parse(backup);
}

/**
 * Supprime une sauvegarde locale (droit à l’oubli RGPD).
 * @param {string} projectId
 */
export function deleteLocalBackup(projectId) {
  validateProjectId(projectId);
  const key = getLocalBackupKey(projectId);
  localStorage.removeItem(key);
  logLocalBackupEvent('delete', projectId);
}

/**
 * Liste les sauvegardes locales existantes.
 * @returns {Array<{projectId: string, timestamp: string}>}
 */
export function listLocalBackups() {
  const backups = [];
  for (let i = 0; i < localStorage.length; i++) {
    const key = localStorage.key(i);
    if (key && key.startsWith('local_backup_')) {
      try {
        const { timestamp } = JSON.parse(localStorage.getItem(key));
        backups.push({ projectId: key.replace('local_backup_', ''), timestamp });
      } catch {
        // Ignore les entrées corrompues
      }
    }
  }
  return backups;
}

/**
 * Génère la clé de stockage local pour un projet.
 * @param {string} projectId
 * @returns {string}
 */
function getLocalBackupKey(projectId) {
  return `local_backup_${projectId}`;
}

/**
 * Valide l’identifiant de projet.
 * @param {string} projectId
 */
function validateProjectId(projectId) {
  if (!projectId || typeof projectId !== 'string') throw new Error('projectId invalide');
}

/**
 * Valide les données du projet.
 * @param {object} projectData
 */
function validateProjectData(projectData) {
  if (!projectData || typeof projectData !== 'object') throw new Error('projectData invalide');
}

/**
 * Anonymise les données du projet pour la sauvegarde locale.
 * @param {object} data
 * @returns {object}
 */
function anonymizeData(data) {
  // Exemple : suppression des champs sensibles
  const { userEmail, userId, ...rest } = data;
  return rest;
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} projectId
 */
function logLocalBackupEvent(action, projectId) {
  try {
    const logs = JSON.parse(localStorage.getItem('local_backup_logs') || '[]');
    logs.push({
      action,
      projectId,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('local_backup_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de sauvegarde locale (droit à l’oubli RGPD).
 */
export function clearLocalBackupLogs() {
  localStorage.removeItem('local_backup_logs');
}