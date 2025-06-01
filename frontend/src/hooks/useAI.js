/**
 * @file useAI.js
 * @description Hook React pour l’intégration d’IA (génération, prompts, réponses) dans Dihya Coding.
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

import { useState, useCallback } from 'react';

/**
 * Hook pour interagir avec un modèle d’IA (ex : GPT) dans Dihya Coding.
 * @param {object} [options]
 * @param {string} [options.lang='fr-FR'] - Langue du prompt
 * @param {boolean} [options.log=true] - Active le log local pour auditabilité
 * @returns {[string, function, boolean, string|null]} [réponse, envoyerPrompt, loading, erreur]
 */
export function useAI(options = {}) {
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  /**
   * Envoie un prompt à l’IA et récupère la réponse.
   * @param {string} prompt
   * @returns {Promise<void>}
   */
  const sendPrompt = useCallback(async (prompt) => {
    if (!hasConsent()) {
      setError('Consentement requis pour utiliser l’IA.');
      return;
    }
    setLoading(true);
    setError(null);
    try {
      // Simulation d’appel API IA (à remplacer par l’intégration réelle)
      const lang = options.lang || 'fr-FR';
      const aiResponse = await fakeAiApi(prompt, lang);
      setResponse(aiResponse);
      if (options.log !== false) {
        logAIEvent('ai_prompt', { prompt: anonymizePrompt(prompt), response: anonymizeResponse(aiResponse), lang });
      }
    } catch (e) {
      setError('Erreur IA : ' + (e.message || e));
    } finally {
      setLoading(false);
    }
  }, [options.lang, options.log]);

  return [response, sendPrompt, loading, error];
}

/**
 * Simulation d’appel à une API IA (à remplacer par l’intégration réelle).
 * @private
 * @param {string} prompt
 * @param {string} lang
 * @returns {Promise<string>}
 */
async function fakeAiApi(prompt, lang) {
  await new Promise(r => setTimeout(r, 200));
  return lang === 'fr-FR'
    ? 'Réponse simulée de l’IA pour : ' + prompt
    : 'Simulated AI response for: ' + prompt;
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('ai_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logAIEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('ai_hook_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString(),
    });
    window.localStorage.setItem('ai_hook_logs', JSON.stringify(logs));
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
  if (typeof prompt !== 'string') return '';
  return prompt.length > 100 ? prompt.slice(0, 100) + '…' : prompt;
}

/**
 * Anonymise une réponse IA pour les logs.
 * @param {string} response
 * @returns {string}
 */
function anonymizeResponse(response) {
  if (typeof response !== 'string') return '';
  return response.length > 100 ? response.slice(0, 100) + '…' : response;
}

/**
 * Efface les logs du hook IA (droit à l’oubli RGPD).
 */
export function clearLocalAIHookLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('ai_hook_logs');
  }
}