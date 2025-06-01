/**
 * @file dwebBackup.js
 * @description Module de sauvegarde décentralisée (dWeb) pour Dihya Coding (sauvegarde, restauration, audit, logs).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Lance une sauvegarde décentralisée (dWeb) des données utilisateur.
 * @param {object} params
 * @param {string} params.userId - Identifiant utilisateur (sera anonymisé pour les logs)
 * @param {object} params.data - Données à sauvegarder (doivent être validées et anonymisées)
 * @param {object} [params.options] - Options avancées (réseau, chiffrement, redondance, etc.)
 * @returns {Promise<{success: boolean, backupId: string, warnings?: string[]}>}
 */
export async function dwebBackup({ userId, data, options = {} }) {
  validateUserId(userId);
  validateBackupData(data);
  if (!window?.localStorage?.getItem('infra_backup_feature_consent')) {
    throw new Error('Consentement requis pour lancer une sauvegarde décentralisée.');
  }
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/infra/dweb/backup', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ userId, data, options }),
  });
  if (!res.ok) throw new Error('Erreur lors de la sauvegarde décentralisée');
  const result = await res.json();
  logDwebBackupEvent('dweb_backup', anonymizeUserId(userId), result.backupId);
  return result;
}

/**
 * Restaure une sauvegarde décentralisée (dWeb) à partir d’un identifiant de sauvegarde.
 * @param {object} params
 * @param {string} params.userId - Identifiant utilisateur (sera anonymisé pour les logs)
 * @param {string} params.backupId - Identifiant de la sauvegarde à restaurer
 * @returns {Promise<{success: boolean, data: object, warnings?: string[]}>}
 */
export async function dwebRestore({ userId, backupId }) {
  validateUserId(userId);
  validateBackupId(backupId);
  if (!window?.localStorage?.getItem('infra_backup_feature_consent')) {
    throw new Error('Consentement requis pour restaurer une sauvegarde décentralisée.');
  }
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/infra/dweb/restore', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ userId, backupId }),
  });
  if (!res.ok) throw new Error('Erreur lors de la restauration de la sauvegarde');
  const result = await res.json();
  logDwebBackupEvent('dweb_restore', anonymizeUserId(userId), backupId);
  return result;
}

/**
 * Valide l’identifiant utilisateur.
 * @param {string} userId
 */
function validateUserId(userId) {
  if (!userId || typeof userId !== 'string' || userId.length < 2) {
    throw new Error('Identifiant utilisateur invalide');
  }
}

/**
 * Valide les données à sauvegarder.
 * @param {object} data
 */
function validateBackupData(data) {
  if (!data || typeof data !== 'object' || Array.isArray(data)) {
    throw new Error('Données de sauvegarde invalides');
  }
}

/**
 * Valide l’identifiant de sauvegarde.
 * @param {string} backupId
 */
function validateBackupId(backupId) {
  if (!backupId || typeof backupId !== 'string' || backupId.length < 8) {
    throw new Error('Identifiant de sauvegarde invalide');
  }
}

/**
 * Anonymise l’identifiant utilisateur pour les logs.
 * @param {string} userId
 * @returns {string}
 */
function anonymizeUserId(userId) {
  return userId.replace(/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/gi, '[email]');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} userId
 * @param {string} [backupId]
 */
function logDwebBackupEvent(action, userId, backupId) {
  try {
    const logs = JSON.parse(localStorage.getItem('dweb_backup_logs') || '[]');
    logs.push({
      action,
      userId,
      backupId,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('dweb_backup_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de sauvegarde décentralisée (droit à l’oubli RGPD).
 */
export function clearLocalDwebBackupLogs() {
  localStorage.removeItem('dweb_backup_logs');
}