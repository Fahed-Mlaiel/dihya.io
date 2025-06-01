/**
 * @file dataExport.js
 * @description Utilitaire d’export de données pour Dihya Coding : export JSON, CSV, TXT, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Exporte des données au format JSON.
 * @param {object|Array} data - Données à exporter
 * @param {string} filename - Nom du fichier (sans extension)
 * @param {object} [options] - { log: bool }
 * @returns {boolean} Succès de l’export
 */
export function exportJSON(data, filename, options = {}) {
  if (!hasConsent()) return false;
  try {
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
    triggerDownload(blob, `${sanitizeFilename(filename)}.json`);
    if (options.log !== false) {
      logDataExportEvent('export_json', { filename: anonymizeFilename(filename), timestamp: new Date().toISOString() });
    }
    return true;
  } catch {
    return false;
  }
}

/**
 * Exporte des données au format CSV.
 * @param {Array<object>} data - Données à exporter (tableau d’objets)
 * @param {string} filename - Nom du fichier (sans extension)
 * @param {object} [options] - { log: bool }
 * @returns {boolean} Succès de l’export
 */
export function exportCSV(data, filename, options = {}) {
  if (!hasConsent()) return false;
  try {
    if (!Array.isArray(data) || data.length === 0) return false;
    const keys = Object.keys(data[0]);
    const csv = [
      keys.join(','),
      ...data.map(row => keys.map(k => `"${String(row[k]).replace(/"/g, '""')}"`).join(','))
    ].join('\r\n');
    const blob = new Blob([csv], { type: 'text/csv' });
    triggerDownload(blob, `${sanitizeFilename(filename)}.csv`);
    if (options.log !== false) {
      logDataExportEvent('export_csv', { filename: anonymizeFilename(filename), timestamp: new Date().toISOString() });
    }
    return true;
  } catch {
    return false;
  }
}

/**
 * Exporte des données au format texte brut.
 * @param {string} text - Texte à exporter
 * @param {string} filename - Nom du fichier (sans extension)
 * @param {object} [options] - { log: bool }
 * @returns {boolean} Succès de l’export
 */
export function exportTXT(text, filename, options = {}) {
  if (!hasConsent()) return false;
  try {
    const blob = new Blob([String(text)], { type: 'text/plain' });
    triggerDownload(blob, `${sanitizeFilename(filename)}.txt`);
    if (options.log !== false) {
      logDataExportEvent('export_txt', { filename: anonymizeFilename(filename), timestamp: new Date().toISOString() });
    }
    return true;
  } catch {
    return false;
  }
}

/**
 * Déclenche le téléchargement d’un blob.
 * @param {Blob} blob
 * @param {string} filename
 */
function triggerDownload(blob, filename) {
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  setTimeout(() => {
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }, 100);
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('data_export_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logDataExportEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('data_export_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('data_export_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Sanitize un nom de fichier pour éviter l’injection.
 * @param {string} filename
 * @returns {string}
 */
function sanitizeFilename(filename) {
  return String(filename).replace(/[^a-zA-Z0-9_\-]/g, '').slice(0, 48) || 'export';
}

/**
 * Anonymise un nom de fichier pour les logs.
 * @param {string} filename
 * @returns {string}
 */
function anonymizeFilename(filename) {
  if (!filename) return '';
  return filename.length > 8 ? filename.slice(0, 2) + '***' + filename.slice(-2) : '***';
}

/**
 * Efface les logs d’export (droit à l’oubli RGPD).
 */
export function clearLocalDataExportLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('data_export_logs');
  }
}

/* Documentation claire : chaque fonction est commentée pour auditabilité et conformité */