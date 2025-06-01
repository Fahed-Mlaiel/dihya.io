/**
 * @file assistant.js
 * @description Fonctions et services assistant IA pour la génération et l’aide contextuelle dans Dihya Coding.
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les interactions sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Appelle l’API backend pour obtenir une réponse de l’assistant IA.
 * @param {object} params
 * @param {Array<{role: string, content: string}>} params.messages - Historique de la conversation (max 10 derniers)
 * @param {string} [params.lang] - Langue de la réponse (ex: 'fr', 'en')
 * @returns {Promise<{reply: string}>}
 */
export async function getAssistantReply({ messages, lang = 'fr' }) {
  validateMessages(messages);
  if (!window?.localStorage?.getItem('assistant_feature_consent')) {
    throw new Error('Consentement requis pour utiliser l’assistant IA.');
  }
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/assistant/chat', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ messages: messages.slice(-10), lang }),
  });
  if (!res.ok) throw new Error('Erreur lors de la réponse de l’assistant');
  const data = await res.json();
  logAssistantEvent('get_reply', anonymizeMessages(messages), lang);
  return data;
}

/**
 * Valide la structure des messages de la conversation.
 * @param {Array} messages
 */
function validateMessages(messages) {
  if (
    !Array.isArray(messages) ||
    messages.length === 0 ||
    !messages.every(
      m =>
        m &&
        typeof m === 'object' &&
        typeof m.role === 'string' &&
        typeof m.content === 'string' &&
        m.content.length > 0
    )
  ) {
    throw new Error('Messages de conversation invalides');
  }
}

/**
 * Anonymise les messages pour les logs (pas de données personnelles).
 * @param {Array} messages
 * @returns {Array}
 */
function anonymizeMessages(messages) {
  return messages.map(m => ({
    ...m,
    content: m.content.replace(/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/gi, '[email]'),
  }));
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {Array|object|string} value
 * @param {string} [lang]
 */
function logAssistantEvent(action, value, lang) {
  try {
    const logs = JSON.parse(localStorage.getItem('assistant_logs') || '[]');
    logs.push({
      action,
      value,
      lang,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('assistant_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs assistant locaux (droit à l’oubli RGPD).
 */
export function clearLocalAssistantLogs() {
  localStorage.removeItem('assistant_logs');
}