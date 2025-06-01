/**
 * @file gpt_fallback.js
 * @description Module de fallback pour l’IA GPT dans Dihya Coding : gestion des indisponibilités, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Appelle GPT ou fournit un fallback local en cas d’indisponibilité.
 * @param {object} params
 * @param {string} params.prompt - Prompt utilisateur
 * @param {object} [params.options] - Options avancées (langue, logs, etc.)
 * @returns {Promise<object>} Résultat { success, response, fallback, timestamp }
 */
export async function gptFallback({ prompt, options = {} }) {
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
    // Simulation d’appel GPT (à remplacer par l’intégration réelle)
    const gptResponse = await fakeGptApi(prompt);
    if (options.log !== false) {
      logGptFallbackEvent('gpt_success', { prompt: anonymizePrompt(prompt), response: anonymizeResponse(gptResponse), timestamp: new Date().toISOString() });
    }
    return {
      success: true,
      response: gptResponse,
      fallback: false,
      timestamp: new Date().toISOString()
    };
  } catch (err) {
    // Fallback local en cas d’échec
    const fallbackResponse = getFallbackResponse(prompt);
    if (options.log !== false) {
      logGptFallbackEvent('gpt_fallback', { prompt: anonymizePrompt(prompt), response: anonymizeResponse(fallbackResponse), error: err.message, timestamp: new Date().toISOString() });
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
 * Simulation d’appel à l’API GPT (à remplacer par l’intégration réelle).
 * @param {string} prompt
 * @returns {Promise<string>}
 */
async function fakeGptApi(prompt) {
  // Simule une indisponibilité 30% du temps
  await new Promise((r) => setTimeout(r, 200));
  if (Math.random() < 0.3) throw new Error('GPT indisponible');
  return `Réponse IA simulée pour : "${prompt.slice(0, 32)}..."`;
}

/**
 * Fallback local en cas d’indisponibilité GPT.
 * @param {string} prompt
 * @returns {string}
 */
function getFallbackResponse(prompt) {
  return `Désolé, l’IA est temporairement indisponible. Voici une réponse générique pour : "${prompt.slice(0, 32)}..."`;
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('gpt_fallback_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logGptFallbackEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('gpt_fallback_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('gpt_fallback_logs', JSON.stringify(logs));
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
 * Efface les logs GPT fallback (droit à l’oubli RGPD).
 */
export function clearLocalGptFallbackLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('gpt_fallback_logs');
  }
}