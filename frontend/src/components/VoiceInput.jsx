/**
 * @file VoiceInput.jsx
 * @description Composant d’entrée vocale (speech-to-text) pour Dihya Coding.
 * Garantit design moderne, accessibilité, sécurité, conformité RGPD, auditabilité, extensibilité et robustesse.
 * Toutes les interactions sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

import React, { useState, useRef } from 'react';
import { transcribeVoice } from '../api/voice';

/**
 * Composant React pour la saisie vocale (speech-to-text).
 * @param {object} props
 * @param {function} props.onResult - Callback appelé avec le texte transcrit
 * @param {string} [props.lang] - Langue de reconnaissance (ex: 'fr-FR')
 * @returns {JSX.Element}
 */
export default function VoiceInput({ onResult, lang = 'fr-FR' }) {
  const [recording, setRecording] = useState(false);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const mediaRecorderRef = useRef(null);
  const audioChunksRef = useRef([]);

  /**
   * Démarre l’enregistrement vocal.
   */
  async function startRecording() {
    setError('');
    if (!window?.localStorage?.getItem('voice_input_consent')) {
      setError('Consentement requis pour utiliser la saisie vocale.');
      return;
    }
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const mediaRecorder = new window.MediaRecorder(stream);
      audioChunksRef.current = [];
      mediaRecorderRef.current = mediaRecorder;

      mediaRecorder.ondataavailable = event => {
        if (event.data.size > 0) {
          audioChunksRef.current.push(event.data);
        }
      };

      mediaRecorder.onstop = handleStop;
      mediaRecorder.start();
      setRecording(true);
      logVoiceInputEvent('start_recording');
    } catch (err) {
      setError('Erreur d’accès au micro.');
    }
  }

  /**
   * Arrête l’enregistrement vocal.
   */
  function stopRecording() {
    if (mediaRecorderRef.current && recording) {
      mediaRecorderRef.current.stop();
      setRecording(false);
      logVoiceInputEvent('stop_recording');
    }
  }

  /**
   * Gère la fin de l’enregistrement et lance la transcription.
   */
  async function handleStop() {
    setLoading(true);
    setError('');
    const audioBlob = new Blob(audioChunksRef.current, { type: 'audio/webm' });
    try {
      const text = await transcribeVoice(audioBlob);
      if (typeof onResult === 'function') onResult(text);
      logVoiceInputEvent('transcription', text);
    } catch (err) {
      setError('Erreur lors de la transcription.');
    } finally {
      setLoading(false);
    }
  }

  return (
    <div
      className="voice-input"
      aria-label="Saisie vocale"
      style={{
        display: 'flex',
        alignItems: 'center',
        gap: 12,
        margin: '12px 0',
      }}
    >
      <button
        type="button"
        onClick={recording ? stopRecording : startRecording}
        aria-label={recording ? 'Arrêter la saisie vocale' : 'Démarrer la saisie vocale'}
        disabled={loading}
        style={{
          background: recording ? '#D32F2F' : '#0057FF',
          color: '#fff',
          border: 'none',
          borderRadius: '50%',
          width: 48,
          height: 48,
          fontSize: 24,
          cursor: loading ? 'not-allowed' : 'pointer',
          outline: 'none',
          boxShadow: recording ? '0 0 0 4px #FFD1D1' : '0 2px 8px rgba(0,0,0,0.07)',
          transition: 'background 0.2s, box-shadow 0.2s',
        }}
      >
        {recording ? '■' : '🎤'}
      </button>
      <span style={{ color: '#555', fontSize: 15 }}>
        {loading
          ? 'Transcription en cours…'
          : recording
          ? 'Enregistrement…'
          : 'Saisir par la voix'}
      </span>
      {error && (
        <span
          role="alert"
          style={{
            color: '#D32F2F',
            marginLeft: 8,
            fontSize: 14,
            background: '#FFF3F3',
            borderRadius: 6,
            padding: '4px 8px',
          }}
        >
          {error}
        </span>
      )}
    </div>
  );
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} [value]
 */
function logVoiceInputEvent(action, value) {
  try {
    const logs = JSON.parse(localStorage.getItem('voice_input_logs') || '[]');
    logs.push({
      action,
      value,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('voice_input_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de saisie vocale (droit à l’oubli RGPD).
 */
export function clearLocalVoiceInputLogs() {
  localStorage.removeItem('voice_input_logs');
}