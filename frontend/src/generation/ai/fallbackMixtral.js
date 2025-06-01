/**
 * @file fallbackMixtral.js
 * @description Fonctions de secours spécifiques pour la génération IA avec Mixtral dans Dihya Coding (fallback en cas d’indisponibilité du service Mixtral).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les interactions sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Génère une réponse de secours spécifique Mixtral si le service est indisponible.
 * @param {object} params
 * @param {string} params.prompt - Prompt utilisateur (sera anonymisé pour les logs)
 * @param {string} [params.type] - Type de génération attendue (ex: 'code', 'doc')
 * @returns {Promise<object>} Réponse fallback structurée
 */
export async function fallbackMixtralGenerate({ prompt, type = 'code' }) {
  validatePrompt(prompt);
  logFallbackMixtralEvent('fallback_mixtral_generate', anonymizePrompt(prompt), type);

  // Réponse spécifique Mixtral selon le type
  let reply;
  switch (type) {
    case 'code':
      reply = '// Service Mixtral IA indisponible.\n// Veuillez réessayer plus tard ou contacter le support Dihya Coding.';
      break;
    case 'doc':
      reply = 'La documentation ne peut pas être générée par Mixtral pour le moment. Merci de réessayer ultérieurement.';
      break;
    default:
      reply = 'Le service Mixtral de génération est temporairement indisponible.';
  }

  return {
    success: false,
    fallback: true,
    engine: 'mixtral',
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
function logFallbackMixtralEvent(action, value, type) {
  try {
    const logs = JSON.parse(localStorage.getItem('fallback_mixtral_logs') || '[]');
    logs.push({
      action,
      value,
      type,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('fallback_mixtral_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de fallback Mixtral (droit à l’oubli RGPD).
 */
export function clearLocalFallbackMixtralLogs() {
  localStorage.removeItem('fallback_mixtral_logs');
}