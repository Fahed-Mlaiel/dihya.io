/**
 * @file backupService.js
 * @description Service centralisé de sauvegarde pour Dihya Coding : gestion des sauvegardes/restaurations, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Sauvegarde des données utilisateur dans le stockage local (chiffré/anonymisé).
 * @param {string} key - Clé de sauvegarde (ex: 'user_settings')
 * @param {object} data - Données à sauvegarder (anonymisées)
 * @param {object} [options] - Options avancées (logs, RGPD, chiffrement)
 * @returns {boolean} Succès de la sauvegarde
 */
export function backupData(key, data, options = {}) {
  if (!hasConsent()) return false;
  const safeKey = sanitizeKey(key);
  const safeData = anonymizeBackupData(data);

  try {
    const payload = options.encrypt ? encryptData(safeData) : JSON.stringify(safeData);
    window.localStorage.setItem('backup_' + safeKey, payload);
    if (options.log !== false) {
      logBackupEvent('backup_data', { key: safeKey, timestamp: new Date().toISOString() });
    }
    return true;
  } catch {
    return false;
  }
}

/**
 * Restaure des données utilisateur depuis le stockage local.
 * @param {string} key - Clé de sauvegarde
 * @param {object} [options] - Options avancées (logs, RGPD, déchiffrement)
 * @returns {object|null} Données restaurées ou null
 */
export function restoreData(key, options = {}) {
  if (!hasConsent()) return null;
  const safeKey = sanitizeKey(key);

  try {
    let payload = window.localStorage.getItem('backup_' + safeKey);
    if (!payload) return null;
    if (options.encrypt) {
      payload = decryptData(payload);
    }
    const data = JSON.parse(payload);
    if (options.log !== false) {
      logBackupEvent('restore_data', { key: safeKey, timestamp: new Date().toISOString() });
    }
    return data;
  } catch {
    return null;
  }
}

/**
 * Supprime une sauvegarde (droit à l’oubli RGPD).
 * @param {string} key
 * @param {object} [options]
 * @returns {boolean}
 */
export function deleteBackup(key, options = {}) {
  if (!hasConsent()) return false;
  const safeKey = sanitizeKey(key);
  try {
    window.localStorage.removeItem('backup_' + safeKey);
    if (options.log !== false) {
      logBackupEvent('delete_backup', { key: safeKey, timestamp: new Date().toISOString() });
    }
    return true;
  } catch {
    return false;
  }
}

/**
 * Liste toutes les clés de sauvegarde disponibles.
 * @returns {string[]} Liste des clés (anonymisées)
 */
export function listBackups() {
  if (!hasConsent()) return [];
  const keys = [];
  for (let i = 0; i < window.localStorage.length; i++) {
    const k = window.localStorage.key(i);
    if (k && k.startsWith('backup_')) {
      keys.push(k.replace('backup_', ''));
    }
  }
  return keys.map(anonymizeKey);
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('backup_service_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logBackupEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('backup_service_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('backup_service_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Sanitize une clé de sauvegarde.
 * @param {string} key
 * @returns {string}
 */
function sanitizeKey(key) {
  return String(key).replace(/[^a-zA-Z0-9_\-]/g, '').slice(0, 48);
}

/**
 * Anonymise une clé de sauvegarde pour les logs.
 * @param {string} key
 * @returns {string}
 */
function anonymizeKey(key) {
  if (!key) return '';
  return key.length > 8 ? key.slice(0, 2) + '***' + key.slice(-2) : '***';
}

/**
 * Anonymise les données de sauvegarde pour les logs.
 * @param {object} data
 * @returns {object}
 */
function anonymizeBackupData(data) {
  const anonymized = {};
  Object.entries(data || {}).forEach(([k, v]) => {
    if (typeof v === 'string' && k.match(/email|user|ip/i)) {
      anonymized[k] = v.length > 4 ? v.slice(0, 2) + '***' + v.slice(-2) : '***';
    } else if (typeof v === 'string' && v.length > 64) {
      anonymized[k] = v.slice(0, 32) + '...';
    } else {
      anonymized[k] = v;
    }
  });
  return anonymized;
}

/**
 * (Optionnel) Chiffre les données avant sauvegarde (simulation).
 * @param {object} data
 * @returns {string}
 */
function encryptData(data) {
  // À remplacer par un vrai chiffrement côté serveur si besoin
  return btoa(unescape(encodeURIComponent(JSON.stringify(data))));
}

/**
 * (Optionnel) Déchiffre les données après restauration (simulation).
 * @param {string} payload
 * @returns {string}
 */
function decryptData(payload) {
  // À remplacer par un vrai déchiffrement côté serveur si besoin
  return decodeURIComponent(escape(atob(payload)));
}

/**
 * Efface les logs de sauvegarde (droit à l’oubli RGPD).
 */
export function clearLocalBackupServiceLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('backup_service_logs');
  }
}