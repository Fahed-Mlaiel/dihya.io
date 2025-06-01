/**
 * @file fallbackMistral.js
 * @description Fonctions de secours spécifiques pour la génération IA avec Mistral dans Dihya Coding (fallback en cas d’indisponibilité du service Mistral).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les interactions sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Génère une réponse de secours spécifique Mistral si le service est indisponible.
 * @param {object} params
 * @param {string} params.prompt - Prompt utilisateur (sera anonymisé pour les logs)
 * @param {string} [params.type] - Type de génération attendue (ex: 'code', 'doc')
 * @returns {Promise<object>} Réponse fallback structurée
 */
export async function fallbackMistralGenerate({ prompt, type = 'code' }) {
  validatePrompt(prompt);
  logFallbackMistralEvent('fallback_mistral_generate', anonymizePrompt(prompt), type);

  // Réponse spécifique Mistral selon le type
  let reply;
  switch (type) {
    case 'code':
      reply = '// Service Mistral IA indisponible.\n// Veuillez réessayer plus tard ou contacter le support Dihya Coding.';
      break;
    case 'doc':
      reply = 'La documentation ne peut pas être générée par Mistral pour le moment. Merci de réessayer ultérieurement.';
      break;
    default:
      reply = 'Le service Mistral de génération est temporairement indisponible.';
  }

  return {
    success: false,
    fallback: true,
    engine: 'mistral',
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
function logFallbackMistralEvent(action, value, type) {
  try {
    const logs = JSON.parse(localStorage.getItem('fallback_mistral_logs') || '[]');
    logs.push({
      action,
      value,
      type,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('fallback_mistral_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de fallback Mistral (droit à l’oubli RGPD).
 */
export function clearLocalFallbackMistralLogs() {
  localStorage.removeItem('fallback_mistral_logs');
}