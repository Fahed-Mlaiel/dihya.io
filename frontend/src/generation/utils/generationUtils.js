/**
 * @file generationUtils.js
 * @description Fonctions utilitaires pour la génération de code, templates et projets Dihya Coding (structure, sécurité, logs, auditabilité, RGPD).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Génère un identifiant unique pour chaque ressource générée.
 * @returns {string} UUID v4-like
 */
export function generateUniqueId() {
  if (!hasConsent()) throw new Error('Consentement requis pour générer un identifiant.');
  const uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, c => {
    const r = Math.random() * 16 | 0, v = c === 'x' ? r : (r & 0x3 | 0x8);
    return v.toString(16);
  });
  logGenerationEvent('generate_id', { uuid });
  return uuid;
}

/**
 * Génère un nom de fichier sécurisé et SEO-friendly.
 * @param {string} baseName
 * @param {string} [ext]
 * @returns {string}
 */
export function generateFileName(baseName, ext = 'js') {
  if (!hasConsent()) throw new Error('Consentement requis pour générer un nom de fichier.');
  if (typeof baseName !== 'string' || !baseName.trim()) throw new Error('Nom de base invalide');
  const slug = baseName
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
  const fileName = `${slug}.${ext}`;
  logGenerationEvent('generate_file_name', { fileName });
  return fileName;
}

/**
 * Génère un timestamp ISO pour l’auditabilité.
 * @returns {string}
 */
export function generateTimestamp() {
  if (!hasConsent()) throw new Error('Consentement requis pour générer un timestamp.');
  const timestamp = new Date().toISOString();
  logGenerationEvent('generate_timestamp', { timestamp });
  return timestamp;
}

/**
 * Valide la structure d’un objet de génération (ex: projet, module).
 * @param {object} obj
 * @param {string[]} requiredFields
 * @returns {boolean}
 */
export function validateGenerationObject(obj, requiredFields = []) {
  if (!hasConsent()) throw new Error('Consentement requis pour valider un objet.');
  if (typeof obj !== 'object' || !obj) throw new Error('Objet de génération invalide');
  for (const field of requiredFields) {
    if (!(field in obj)) return false;
  }
  logGenerationEvent('validate_object', { obj: anonymizeGenerationData(obj), requiredFields });
  return true;
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('generation_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logGenerationEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('generation_utils_logs') || '[]');
    logs.push({
      action,
      data: anonymizeGenerationData(data),
      timestamp: new Date().toISOString(),
    });
    window.localStorage.setItem('generation_utils_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise les données sensibles pour les logs.
 * @param {object} data
 * @returns {object}
 */
function anonymizeGenerationData(data) {
  // Exemple : masquer les emails, tokens, etc.
  if (!data || typeof data !== 'object') return data;
  const clone = JSON.parse(JSON.stringify(data));
  if (clone.email) clone.email = '[email]';
  if (clone.token) clone.token = '[protected]';
  return clone;
}

/**
 * Efface les logs de génération (droit à l’oubli RGPD).
 */
export function clearLocalGenerationUtilsLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('generation_utils_logs');
  }
}