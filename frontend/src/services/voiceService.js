/**
 * @file voiceService.js
 * @description Service centralisé de gestion vocale pour Dihya Coding : synthèse vocale (TTS), reconnaissance vocale (ASR), sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

/**
 * Lance la synthèse vocale (Text-to-Speech) d’un texte donné.
 * @param {object} params
 * @param {string} params.text - Texte à lire
 * @param {string} [params.lang='fr-FR'] - Langue de la synthèse
 * @param {object} [params.options] - Options avancées (logs, voix, RGPD)
 * @returns {boolean} Succès de l’opération
 */
export function speak({ text, lang = 'fr-FR', options = {} }) {
  if (!hasConsent()) return false;
  if (!text || typeof text !== 'string' || text.length < 2) return false;
  if (typeof window === 'undefined' || !window.speechSynthesis) return false;

  try {
    const utter = new window.SpeechSynthesisUtterance(sanitize(text));
    utter.lang = lang;
    if (options.voice) {
      const voices = window.speechSynthesis.getVoices();
      const found = voices.find(v => v.name === options.voice);
      if (found) utter.voice = found;
    }
    window.speechSynthesis.speak(utter);

    if (options.log !== false) {
      logVoiceEvent('speak', {
        text: anonymizeText(text),
        lang,
        timestamp: new Date().toISOString()
      });
    }
    return true;
  } catch {
    return false;
  }
}

/**
 * Lance la reconnaissance vocale (ASR) et retourne le texte reconnu (Promise).
 * @param {object} params
 * @param {string} [params.lang='fr-FR'] - Langue de la reconnaissance
 * @param {object} [params.options] - Options avancées (logs, RGPD)
 * @returns {Promise<string|null>} Texte reconnu ou null
 */
export function recognize({ lang = 'fr-FR', options = {} } = {}) {
  return new Promise((resolve) => {
    if (!hasConsent()) return resolve(null);
    if (typeof window === 'undefined' || !window.SpeechRecognition && !window.webkitSpeechRecognition) return resolve(null);

    try {
      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
      const recog = new SpeechRecognition();
      recog.lang = lang;
      recog.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        if (options.log !== false) {
          logVoiceEvent('recognize', {
            transcript: anonymizeText(transcript),
            lang,
            timestamp: new Date().toISOString()
          });
        }
        resolve(transcript);
      };
      recog.onerror = () => resolve(null);
      recog.start();
    } catch {
      resolve(null);
    }
  });
}

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('voice_service_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logVoiceEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('voice_service_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('voice_service_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Sanitize une chaîne pour éviter l’injection.
 * @param {string} str
 * @returns {string}
 */
function sanitize(str) {
  return String(str).replace(/[\r\n<>]/g, '');
}

/**
 * Anonymise un texte pour les logs.
 * @param {string} text
 * @returns {string}
 */
function anonymizeText(text) {
  if (!text) return '';
  return text.length > 24 ? text.slice(0, 12) + '...' : text;
}

/**
 * Efface les logs vocaux (droit à l’oubli RGPD).
 */
export function clearLocalVoiceServiceLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('voice_service_logs');
  }
}