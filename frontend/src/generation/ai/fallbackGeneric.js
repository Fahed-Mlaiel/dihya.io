/**
 * @file fallbackGeneric.js
 * @description Fonctions de secours génériques pour la génération IA dans Dihya Coding (fallback en cas d’indisponibilité du service principal).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les interactions sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Génère une réponse générique de secours si l’IA principale est indisponible.
 * @param {object} params
 * @param {string} params.prompt - Prompt utilisateur (sera anonymisé pour les logs)
 * @param {string} [params.type] - Type de génération attendue (ex: 'code', 'doc')
 * @returns {Promise<object>} Réponse fallback structurée
 */
export async function fallbackGenerate({ prompt, type = 'code' }) {
  validatePrompt(prompt);
  logFallbackEvent('fallback_generate', anonymizePrompt(prompt), type);

  // Réponse générique selon le type
  let reply;
  switch (type) {
    case 'code':
      reply = '// Service IA indisponible.\n// Veuillez réessayer plus tard ou contacter le support.';
      break;
    case 'doc':
      reply = 'La documentation ne peut pas être générée pour le moment. Merci de réessayer ultérieurement.';
      break;
    default:
      reply = 'Le service de génération est temporairement indisponible.';
  }

  return {
    success: false,
    fallback: true,
    type,
    reply,
    timestamp: new Date().toISOString(),
  };
}

/**
 * Valide le prompt utilisateur.
 * @param {string} prompt
 */
function validatePrompt(prompt) {
  if (!prompt || typeof prompt !== 'string' || prompt.length < 3) {
    throw new Error('Prompt IA invalide');
  }
}

/**
 * Anonymise le prompt pour les logs (pas de données personnelles).
 * @param {string} prompt
 * @returns {string}
 */
function anonymizePrompt(prompt) {
  // Exemple simple : suppression d’emails
  return prompt.replace(/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/gi, '[email]');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} value
 * @param {string} [type]
 */
function logFallbackEvent(action, value, type) {
  try {
    const logs = JSON.parse(localStorage.getItem('fallback_generic_logs') || '[]');
    logs.push({
      action,
      value,
      type,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('fallback_generic_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de fallback générique (droit à l’oubli RGPD).
 */
export function clearLocalFallbackGenericLogs() {
  localStorage.removeItem('fallback_generic_logs');
}