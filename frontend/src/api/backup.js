/**
 * @file backup.js
 * @description API centralisée pour la gestion des sauvegardes côté frontend Dihya Coding.
 * Sécurité, conformité RGPD, auditabilité, extensibilité.
 * Toutes les requêtes sont validées, sécurisées, et loguées localement pour audit.
 * Ne jamais exposer de données sensibles sans consentement explicite.
 */

const API_BASE = '/api/backup';

/**
 * Télécharge une sauvegarde du projet.
 * @param {string} projectId - Identifiant du projet à sauvegarder
 * @returns {Promise<Blob>} Fichier de sauvegarde (zip/json)
 */
export async function downloadBackup(projectId) {
  validateProjectId(projectId);
  const token = localStorage.getItem('jwt_token');
  const res = await fetch(`${API_BASE}/download?projectId=${encodeURIComponent(projectId)}`, {
    headers: {
      'Authorization': `Bearer ${token}`,
    },
  });
  if (!res.ok) throw new Error('Erreur lors du téléchargement de la sauvegarde');
  logBackupEvent('download', projectId);
  return await res.blob();
}

/**
 * Liste les sauvegardes disponibles pour l’utilisateur.
 * @returns {Promise<Array>} Liste des sauvegardes
 */
export async function listBackups() {
  const token = localStorage.getItem('jwt_token');
  const res = await fetch(`${API_BASE}/list`, {
    headers: {
      'Authorization': `Bearer ${token}`,
    },
  });
  if (!res.ok) throw new Error('Erreur lors de la récupération des sauvegardes');
  return await res.json();
}

/**
 * Supprime une sauvegarde (droit à l’oubli RGPD).
 * @param {string} backupId
 * @returns {Promise<object>} Résultat de la suppression
 */
export async function deleteBackup(backupId) {
  validateBackupId(backupId);
  const token = localStorage.getItem('jwt_token');
  const res = await fetch(`${API_BASE}/delete`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`,
    },
    body: JSON.stringify({ backupId }),
  });
  if (!res.ok) throw new Error('Erreur lors de la suppression de la sauvegarde');
  logBackupEvent('delete', backupId);
  return await res.json();
}

/**
 * Valide l’identifiant de projet.
 * @param {string} projectId
 */
function validateProjectId(projectId) {
  if (!projectId || typeof projectId !== 'string') throw new Error('projectId invalide');
}

/**
 * Valide l’identifiant de sauvegarde.
 * @param {string} backupId
 */
function validateBackupId(backupId) {
  if (!backupId || typeof backupId !== 'string') throw new Error('backupId invalide');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} id
 */
function logBackupEvent(action, id) {
  try {
    const logs = JSON.parse(localStorage.getItem('backup_logs') || '[]');
    logs.push({
      action,
      id,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('backup_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de sauvegarde locaux (droit à l’oubli RGPD).
 */
export function clearLocalBackupLogs() {
  localStorage.removeItem('backup_logs');
}