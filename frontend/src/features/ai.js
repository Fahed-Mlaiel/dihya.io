/**
 * @file ai.js
 * @description Fonctions et services IA pour Dihya Coding (génération, analyse, suggestion).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les interactions sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Appelle l’API IA pour générer du code ou du contenu.
 * @param {object} params - Paramètres de génération (prompt, type, options)
 * @param {string} params.prompt - Texte d’entrée pour l’IA
 * @param {string} [params.type] - Type de génération (ex: 'code', 'doc', 'test')
 * @param {object} [params.options] - Options avancées (langue, stack, etc.)
 * @returns {Promise<object>} Résultat de la génération IA
 */
export async function generateAI({ prompt, type = 'code', options = {} }) {
  validatePrompt(prompt);
  if (!window?.localStorage?.getItem('ai_feature_consent')) {
    throw new Error('Consentement requis pour utiliser l’IA.');
  }
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/ai/generate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { 'Authorization': `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ prompt, type, options }),
  });
  if (!res.ok) throw new Error('Erreur lors de la génération IA');
  const data = await res.json();
  logAIEvent('generate', anonymizePrompt(prompt), type);
  return data;
}

/**
 * Appelle l’API IA pour analyser du code ou un projet.
 * @param {object} params - Paramètres d’analyse (code, options)
 * @param {string} params.code - Code source à analyser
 * @param {object} [params.options] - Options avancées (langage, règles, etc.)
 * @returns {Promise<object>} Résultat de l’analyse IA
 */
export async function analyzeAI({ code, options = {} }) {
  validateCode(code);
  if (!window?.localStorage?.getItem('ai_feature_consent')) {
    throw new Error('Consentement requis pour utiliser l’IA.');
  }
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/ai/analyze', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { 'Authorization': `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ code, options }),
  });
  if (!res.ok) throw new Error('Erreur lors de l’analyse IA');
  const data = await res.json();
  logAIEvent('analyze', '[code]', options?.lang || 'unknown');
  return data;
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
 * Valide le code source fourni.
 * @param {string} code
 */
function validateCode(code) {
  if (!code || typeof code !== 'string' || code.length < 3) {
    throw new Error('Code source invalide');
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
function logAIEvent(action, value, type) {
  try {
    const logs = JSON.parse(localStorage.getItem('ai_feature_logs') || '[]');
    logs.push({
      action,
      value,
      type,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('ai_feature_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs IA locaux (droit à l’oubli RGPD).
 */
export function clearLocalAILogs() {
  localStorage.removeItem('ai_feature_logs');
}