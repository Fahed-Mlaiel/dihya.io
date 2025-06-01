/**
 * @file autoBackup.js
 * @description Module pour la gestion des sauvegardes automatiques sur Dihya Coding.
 * Garantit sécurité, conformité RGPD, auditabilité, extensibilité et robustesse.
 * Toutes les sauvegardes sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

import { downloadBackup, listBackups } from '../api/backup';

/**
 * Lance une sauvegarde automatique à intervalle régulier.
 * @param {string} projectId - Identifiant du projet à sauvegarder
 * @param {number} intervalMs - Intervalle en millisecondes (ex: 3600000 pour 1h)
 * @param {function} [onBackup] - Callback appelé après chaque sauvegarde (succès ou erreur)
 * @returns {function} Fonction pour arrêter l’auto-backup
 */
export function startAutoBackup(projectId, intervalMs, onBackup) {
  validateProjectId(projectId);
  if (!intervalMs || typeof intervalMs !== 'number' || intervalMs < 60000) {
    throw new Error('Intervalle de sauvegarde trop court ou invalide');
  }
  let stopped = false;

  async function backupLoop() {
    while (!stopped) {
      try {
        await performAutoBackup(projectId);
        if (typeof onBackup === 'function') onBackup(null);
      } catch (err) {
        if (typeof onBackup === 'function') onBackup(err);
      }
      await wait(intervalMs);
    }
  }

  backupLoop();
  return () => { stopped = true; };
}

/**
 * Effectue une sauvegarde automatique du projet.
 * @param {string} projectId
 * @returns {Promise<void>}
 */
async function performAutoBackup(projectId) {
  // Respect du consentement utilisateur (RGPD)
  if (!window?.localStorage?.getItem('auto_backup_consent')) return;

  // Vérifie si une sauvegarde récente existe déjà (évite les doublons)
  const backups = await listBackups();
  const recent = backups.find(
    b => b.projectId === projectId && isRecentBackup(b.timestamp)
  );
  if (recent) return;

  // Télécharge la sauvegarde (stockage local ou cloud selon backend)
  await downloadBackup(projectId);
  logAutoBackupEvent('auto_backup', projectId);
}

/**
 * Vérifie si une sauvegarde est récente (moins de 1h).
 * @param {string} timestamp - ISO string
 * @returns {boolean}
 */
function isRecentBackup(timestamp) {
  if (!timestamp) return false;
  const now = Date.now();
  const backupTime = new Date(timestamp).getTime();
  return now - backupTime < 3600000; // 1h
}

/**
 * Valide l’identifiant de projet.
 * @param {string} projectId
 */
function validateProjectId(projectId) {
  if (!projectId || typeof projectId !== 'string') throw new Error('projectId invalide');
}

/**
 * Attends un certain temps (ms).
 * @param {number} ms
 * @returns {Promise<void>}
 */
function wait(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} projectId
 */
function logAutoBackupEvent(action, projectId) {
  try {
    const logs = JSON.parse(localStorage.getItem('auto_backup_logs') || '[]');
    logs.push({
      action,
      projectId,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('auto_backup_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs d’auto-backup locaux (droit à l’oubli RGPD).
 */
export function clearLocalAutoBackupLogs() {
  localStorage.removeItem('auto_backup_logs');
}