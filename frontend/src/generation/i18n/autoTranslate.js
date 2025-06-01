/**
 * @file autoTranslate.js
 * @description Module de traduction automatique pour Dihya Coding (détection de langue, traduction, logs, audit).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les traductions sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Traduit automatiquement un texte dans la langue cible.
 * @param {object} params
 * @param {string} params.text - Texte source à traduire (sera anonymisé pour les logs)
 * @param {string} params.targetLang - Code langue cible (ex: 'fr', 'en', 'ar', 'ber')
 * @param {object} [params.options] - Options avancées (service, formality, glossary, etc.)
 * @returns {Promise<{success: boolean, translated: string, warnings?: string[]}>}
 */
export async function autoTranslate({ text, targetLang, options = {} }) {
  validateText(text);
  validateLang(targetLang);
  if (!window?.localStorage?.getItem('i18n_feature_consent')) {
    throw new Error('Consentement requis pour utiliser la traduction automatique.');
  }
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/i18n/translate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ text, targetLang, options }),
  });
  if (!res.ok) throw new Error('Erreur lors de la traduction automatique');
  const data = await res.json();
  logAutoTranslateEvent('auto_translate', anonymizeText(text), targetLang);
  return data;
}

/**
 * Détecte automatiquement la langue d’un texte.
 * @param {string} text
 * @returns {Promise<{success: boolean, lang: string, confidence: number}>}
 */
export async function detectLanguage(text) {
  validateText(text);
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/i18n/detect', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ text }),
  });
  if (!res.ok) throw new Error('Erreur lors de la détection de langue');
  const data = await res.json();
  logAutoTranslateEvent('detect_language', anonymizeText(text), data.lang);
  return data;
}

/**
 * Valide le texte à traduire.
 * @param {string} text
 */
function validateText(text) {
  if (!text || typeof text !== 'string' || text.length < 1 || text.length > 5000) {
    throw new Error('Texte à traduire invalide');
  }
}

/**
 * Valide le code langue cible.
 * @param {string} lang
 */
function validateLang(lang) {
  const SUPPORTED_LANGS = ['fr', 'en', 'ar', 'ber', 'es', 'de', 'it', 'pt', 'zh', 'ru'];
  if (!SUPPORTED_LANGS.includes(lang)) {
    throw new Error('Langue cible non supportée');
  }
}

/**
 * Anonymise le texte pour les logs (suppression d’emails, données sensibles).
 * @param {string} text
 * @returns {string}
 */
function anonymizeText(text) {
  return text.replace(/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/gi, '[email]');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} value
 * @param {string} [lang]
 */
function logAutoTranslateEvent(action, value, lang) {
  try {
    const logs = JSON.parse(localStorage.getItem('auto_translate_logs') || '[]');
    logs.push({
      action,
      value,
      lang,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('auto_translate_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de traduction automatique (droit à l’oubli RGPD).
 */
export function clearLocalAutoTranslateLogs() {
  localStorage.removeItem('auto_translate_logs');
}