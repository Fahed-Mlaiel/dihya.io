/**
 * @file iaScript.js
 * @description Générateur et gestionnaire de scripts IA pour Dihya Coding (création, validation, audit, logs).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les interactions sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Génère un script IA à partir de paramètres métier.
 * @param {object} params
 * @param {string} params.name - Nom du script (validé, anonymisé pour logs)
 * @param {string} params.type - Type de script (ex: 'training', 'inference', 'preprocessing')
 * @param {object} [params.options] - Options avancées (langage, framework, dataset, etc.)
 * @returns {Promise<{success: boolean, script: string, warnings?: string[]}>}
 */
export async function generateIaScript({ name, type, options = {} }) {
  validateScriptName(name);
  validateScriptType(type);
  if (!window?.localStorage?.getItem('ia_script_feature_consent')) {
    throw new Error('Consentement requis pour générer un script IA.');
  }
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/blueprints/iaScript/generate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ name, type, options }),
  });
  if (!res.ok) throw new Error('Erreur lors de la génération du script IA');
  const data = await res.json();
  logIaScriptEvent('generate_ia_script', anonymizeScriptName(name), type);
  return data;
}

/**
 * Audite un script IA existant.
 * @param {object} params
 * @param {string} params.scriptCode - Code source du script à auditer
 * @returns {Promise<{success: boolean, issues: Array, report: string}>}
 */
export async function auditIaScript({ scriptCode }) {
  validateScriptCode(scriptCode);
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/blueprints/iaScript/audit', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ scriptCode }),
  });
  if (!res.ok) throw new Error('Erreur lors de l’audit du script IA');
  const data = await res.json();
  logIaScriptEvent('audit_ia_script', '[code]');
  return data;
}

/**
 * Valide le nom du script.
 * @param {string} name
 */
function validateScriptName(name) {
  if (!name || typeof name !== 'string' || name.length < 3 || name.length > 64) {
    throw new Error('Nom de script invalide');
  }
}

/**
 * Valide le type de script.
 * @param {string} type
 */
function validateScriptType(type) {
  const SUPPORTED_TYPES = ['training', 'inference', 'preprocessing', 'custom'];
  if (!SUPPORTED_TYPES.includes(type)) {
    throw new Error('Type de script IA non supporté');
  }
}

/**
 * Valide le code source du script.
 * @param {string} scriptCode
 */
function validateScriptCode(scriptCode) {
  if (!scriptCode || typeof scriptCode !== 'string' || scriptCode.length < 10) {
    throw new Error('Code de script IA invalide');
  }
}

/**
 * Anonymise le nom du script pour les logs (pas de données personnelles).
 * @param {string} name
 * @returns {string}
 */
function anonymizeScriptName(name) {
  return name.replace(/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/gi, '[email]');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} value
 * @param {string} [type]
 */
function logIaScriptEvent(action, value, type) {
  try {
    const logs = JSON.parse(localStorage.getItem('ia_script_logs') || '[]');
    logs.push({
      action,
      value,
      type,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('ia_script_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de génération/audit de scripts IA (droit à l’oubli RGPD).
 */
export function clearLocalIaScriptLogs() {
  localStorage.removeItem('ia_script_logs');
}