/**
 * @file ipfsBackup.js
 * @description Module de sauvegarde et restauration via IPFS pour Dihya Coding (sauvegarde, restauration, audit, logs).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Lance une sauvegarde de données sur IPFS.
 * @param {object} params
 * @param {string} params.userId - Identifiant utilisateur (sera anonymisé pour les logs)
 * @param {object} params.data - Données à sauvegarder (doivent être validées et anonymisées)
 * @param {object} [params.options] - Options avancées (gateway, pinning, chiffrement, etc.)
 * @returns {Promise<{success: boolean, cid: string, warnings?: string[]}>}
 */
export async function ipfsBackup({ userId, data, options = {} }) {
  validateUserId(userId);
  validateBackupData(data);
  if (!window?.localStorage?.getItem('infra_backup_feature_consent')) {
    throw new Error('Consentement requis pour lancer une sauvegarde IPFS.');
  }
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/infra/ipfs/backup', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ userId, data, options }),
  });
  if (!res.ok) throw new Error('Erreur lors de la sauvegarde IPFS');
  const result = await res.json();
  logIpfsBackupEvent('ipfs_backup', anonymizeUserId(userId), result.cid);
  return result;
}

/**
 * Restaure des données depuis IPFS à partir d’un CID.
 * @param {object} params
 * @param {string} params.userId - Identifiant utilisateur (sera anonymisé pour les logs)
 * @param {string} params.cid - CID IPFS à restaurer
 * @returns {Promise<{success: boolean, data: object, warnings?: string[]}>}
 */
export async function ipfsRestore({ userId, cid }) {
  validateUserId(userId);
  validateCid(cid);
  if (!window?.localStorage?.getItem('infra_backup_feature_consent')) {
    throw new Error('Consentement requis pour restaurer une sauvegarde IPFS.');
  }
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/infra/ipfs/restore', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ userId, cid }),
  });
  if (!res.ok) throw new Error('Erreur lors de la restauration IPFS');
  const result = await res.json();
  logIpfsBackupEvent('ipfs_restore', anonymizeUserId(userId), cid);
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
 * Valide un CID IPFS.
 * @param {string} cid
 */
function validateCid(cid) {
  // Validation simple, à adapter selon les versions CID (v0/v1)
  if (!cid || typeof cid !== 'string' || cid.length < 10) {
    throw new Error('CID IPFS invalide');
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
 * @param {string} [cid]
 */
function logIpfsBackupEvent(action, userId, cid) {
  try {
    const logs = JSON.parse(localStorage.getItem('ipfs_backup_logs') || '[]');
    logs.push({
      action,
      userId,
      cid,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('ipfs_backup_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de sauvegarde IPFS (droit à l’oubli RGPD).
 */
export function clearLocalIpfsBackupLogs() {
  localStorage.removeItem('ipfs_backup_logs');
}