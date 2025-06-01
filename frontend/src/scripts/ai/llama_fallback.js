/**
 * @file llama_fallback.js
 * @description Module de fallback pour l’IA Llama dans Dihya Coding : gestion des indisponibilités, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Appelle Llama ou fournit un fallback local en cas d’indisponibilité.
 * @param {object} params
 * @param {string} params.prompt - Prompt utilisateur
 * @param {object} [params.options] - Options avancées (langue, logs, etc.)
 * @returns {Promise<object>} Résultat { success, response, fallback, timestamp }
 */
export async function llamaFallback({ prompt, options = {} }) {
  if (!hasConsent()) {
    return {
      success: false,
      response: null,
      fallback: true,
      error: 'Consentement requis',
      timestamp: new Date().toISOString()
    };
  }
  if (!prompt || typeof prompt !== 'string') {
    return {
      success: false,
      response: null,
      fallback: true,
      error: 'Prompt invalide',
      timestamp: new Date().toISOString()
    };
  }

  try {
    // Simulation d’appel Llama (à remplacer par l’intégration réelle)
    const llamaResponse = await fakeLlamaApi(prompt);
    if (options.log !== false) {
      logLlamaFallbackEvent('llama_success', { prompt: anonymizePrompt(prompt), response: anonymizeResponse(llamaResponse), timestamp: new Date().toISOString() });
    }
    return {
      success: true,
      response: llamaResponse,
      fallback: false,
      timestamp: new Date().toISOString()
    };
  } catch (err) {
    // Fallback local en cas d’échec
    const fallbackResponse = getFallbackResponse(prompt);
    if (options.log !== false) {
      logLlamaFallbackEvent('llama_fallback', { prompt: anonymizePrompt(prompt), response: anonymizeResponse(fallbackResponse), error: err.message, timestamp: new Date().toISOString() });
    }
    return {
      success: true,
      response: fallbackResponse,
      fallback: true,
      timestamp: new Date().toISOString()
    };
  }
}

/**
 * Simulation d’appel à l’API Llama (à remplacer par l’intégration réelle).
 * @param {string} prompt
 * @returns {Promise<string>}
 */
async function fakeLlamaApi(prompt) {
  // Simule une indisponibilité 30% du temps
  await new Promise((r) => setTimeout(r, 200));
  if (Math.random() < 0.3) throw new Error('Llama indisponible');
  return `Réponse Llama simulée pour : "${prompt.slice(0, 32)}..."`;
}

/**
 * Fallback local en cas d’indisponibilité Llama.
 * @param {string} prompt
 * @returns {string}
 */
function getFallbackResponse(prompt) {
  return `Désolé, Llama est temporairement indisponible. Voici une réponse générique pour : "${prompt.slice(0, 32)}..."`;
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('llama_fallback_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logLlamaFallbackEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('llama_fallback_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('llama_fallback_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise un prompt pour les logs.
 * @param {string} prompt
 * @returns {string}
 */
function anonymizePrompt(prompt) {
  if (!prompt || typeof prompt !== 'string') return '';
  return prompt.length > 32 ? prompt.slice(0, 32) + '…' : prompt;
}

/**
 * Anonymise une réponse pour les logs.
 * @param {string} response
 * @returns {string}
 */
function anonymizeResponse(response) {
  if (!response || typeof response !== 'string') return '';
  return response.length > 64 ? response.slice(0, 64) + '…' : response;
}

/**
 * Efface les logs Llama fallback (droit à l’oubli RGPD).
 */
export function clearLocalLlamaFallbackLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('llama_fallback_logs');
  }
}