/**
 * @file speechToText.js
 * @description Module de reconnaissance vocale (speech-to-text) pour Dihya Coding : conversion voix en texte, accessibilité, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Démarre la reconnaissance vocale (speech-to-text) avec options.
 * @param {object} [options] - { lang, interimResults, onResult, onError, log }
 * @returns {object|null} Instance de reconnaissance ou null si non supporté
 */
export function startSpeechToText(options = {}) {
  if (!hasConsent()) return null;
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRecognition) {
    if (options.onError) options.onError('SpeechRecognition non supporté');
    return null;
  }
  const recognition = new SpeechRecognition();
  recognition.lang = options.lang || 'fr-FR';
  recognition.interimResults = !!options.interimResults;
  recognition.maxAlternatives = 1;

  recognition.onresult = (event) => {
    const text = event.results[0][0].transcript;
    if (options.log !== false) {
      logSpeechToTextEvent('result', { text: anonymizeText(text), lang: recognition.lang, timestamp: new Date().toISOString() });
    }
    if (typeof options.onResult === 'function') {
      options.onResult(text);
    }
  };

  recognition.onerror = (event) => {
    if (options.log !== false) {
      logSpeechToTextEvent('error', { error: event.error, timestamp: new Date().toISOString() });
    }
    if (typeof options.onError === 'function') {
      options.onError(event.error);
    }
  };

  recognition.onstart = () => {
    if (options.log !== false) {
      logSpeechToTextEvent('start', { lang: recognition.lang, timestamp: new Date().toISOString() });
    }
  };

  recognition.onend = () => {
    if (options.log !== false) {
      logSpeechToTextEvent('end', { timestamp: new Date().toISOString() });
    }
  };

  recognition.start();
  return recognition;
}

/**
 * Arrête une instance de reconnaissance vocale.
 * @param {object} recognition - Instance de SpeechRecognition
 */
export function stopSpeechToText(recognition) {
  if (recognition && typeof recognition.stop === 'function') {
    recognition.stop();
  }
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('voice_speechToText_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logSpeechToTextEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('voice_speechToText_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('voice_speechToText_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise un texte pour les logs (ne conserve que la longueur).
 * @param {string} text
 * @returns {string}
 */
function anonymizeText(text) {
  if (!text) return '';
  return `[texte:${text.length} caractères]`;
}

/**
 * Efface les logs speech-to-text (droit à l’oubli RGPD).
 */
export function clearLocalSpeechToTextLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('voice_speechToText_logs');
  }
}

/* Documentation claire : chaque fonction est commentée pour auditabilité et conformité */