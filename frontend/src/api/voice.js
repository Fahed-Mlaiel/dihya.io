/**
 * @file voice.js
 * @description API centralisée pour la gestion de la saisie et génération vocale sur Dihya Coding.
 * Respecte la sécurité, la conformité RGPD, l’auditabilité et l’extensibilité.
 * Toutes les requêtes sont validées, sécurisées, et loguées localement pour audit.
 * Ne jamais exposer de données sensibles ou personnelles sans consentement explicite.
 */

const API_BASE = '/api/voice';

/**
 * Transcrit un message vocal en texte (speech-to-text).
 * @param {Blob|File} audioBlob - Fichier audio à transcrire
 * @returns {Promise<string>} Texte transcrit
 */
export async function transcribeVoice(audioBlob) {
  validateAudioBlob(audioBlob);
  const token = localStorage.getItem('jwt_token');
  const formData = new FormData();
  formData.append('audio', audioBlob);

  const res = await fetch(`${API_BASE}/transcribe`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${token}`,
    },
    body: formData,
  });
  if (!res.ok) throw new Error('Erreur lors de la transcription vocale');
  const data = await res.json();
  logVoiceEvent('transcribe');
  return data.text;
}

/**
 * Génère une synthèse vocale à partir d’un texte (text-to-speech).
 * @param {string} text - Texte à synthétiser
 * @param {object} [options] - { lang, voice }
 * @returns {Promise<Blob>} Fichier audio généré
 */
export async function synthesizeVoice(text, options = {}) {
  validateText(text);
  const token = localStorage.getItem('jwt_token');
  const res = await fetch(`${API_BASE}/synthesize`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`,
    },
    body: JSON.stringify({ text, ...options }),
  });
  if (!res.ok) throw new Error('Erreur lors de la synthèse vocale');
  logVoiceEvent('synthesize');
  return await res.blob();
}

/**
 * Valide un fichier audio.
 * @param {Blob|File} audioBlob
 */
function validateAudioBlob(audioBlob) {
  if (!audioBlob || !(audioBlob instanceof Blob)) throw new Error('Audio invalide');
}

/**
 * Valide un texte à synthétiser.
 * @param {string} text
 */
function validateText(text) {
  if (!text || typeof text !== 'string') throw new Error('Texte invalide');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 */
function logVoiceEvent(action) {
  try {
    const logs = JSON.parse(localStorage.getItem('voice_logs') || '[]');
    logs.push({
      action,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('voice_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs vocaux locaux (droit à l’oubli RGPD).
 */
export function clearLocalVoiceLogs() {
  localStorage.removeItem('voice_logs');
}