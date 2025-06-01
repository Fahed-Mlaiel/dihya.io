/**
 * @file test_voice.js
 * @description Tests unitaires et d’intégration pour les modules vocaux Dihya Coding (synthèse vocale, reconnaissance, commandes, accessibilité).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Tous les tests respectent les bonnes pratiques de validation, anonymisation, logs locaux et consentement utilisateur.
 */

import { speechSynthesisTemplate } from '../voice/speechSynthesisTemplate';
import { speechRecognitionTemplate } from '../voice/speechRecognitionTemplate';
import { voiceCommandTemplate } from '../voice/voiceCommandTemplate';
import { accessibilityVoiceTemplate } from '../voice/accessibilityVoiceTemplate';
import { clearLocalVoiceTemplateLogs } from '../voice/voiceLogUtils';

// Mock localStorage pour tests (si non disponible)
if (typeof window === 'undefined') {
  global.window = {};
}
if (!window.localStorage) {
  window.localStorage = {
    store: {},
    getItem(key) { return this.store[key] || null; },
    setItem(key, value) { this.store[key] = value; },
    removeItem(key) { delete this.store[key]; }
  };
}

// Consentement simulé pour les tests
window.localStorage.setItem('voice_feature_consent', 'true');

describe('Voice Templates Dihya Coding', () => {
  afterEach(() => {
    clearLocalVoiceTemplateLogs();
  });

  it('génère un module de synthèse vocale valide', () => {
    const data = { text: 'Bienvenue sur Dihya Coding', lang: 'fr-FR' };
    const synth = speechSynthesisTemplate(data);
    expect(synth).toBeDefined();
    expect(synth.text).toBe('Bienvenue sur Dihya Coding');
    expect(synth.lang).toBe('fr-FR');
  });

  it('génère un module de reconnaissance vocale valide', () => {
    const data = { lang: 'en-US', grammar: ['hello', 'world'] };
    const recog = speechRecognitionTemplate(data);
    expect(recog).toBeDefined();
    expect(recog.lang).toBe('en-US');
    expect(Array.isArray(recog.grammar)).toBe(true);
  });

  it('génère un module de commande vocale valide', () => {
    const data = { commands: ['start', 'stop'], secure: true };
    const cmd = voiceCommandTemplate(data);
    expect(cmd).toBeDefined();
    expect(Array.isArray(cmd.commands)).toBe(true);
    expect(cmd.secure).toBe(true);
  });

  it('génère un module d’accessibilité vocale valide', () => {
    const data = { enabled: true, options: { volume: 0.8 } };
    const acc = accessibilityVoiceTemplate(data);
    expect(acc).toBeDefined();
    expect(acc.enabled).toBe(true);
    expect(acc.options.volume).toBe(0.8);
  });

  it('refuse des données invalides', () => {
    expect(() => speechSynthesisTemplate({})).toThrow();
    expect(() => speechRecognitionTemplate({})).toThrow();
    expect(() => voiceCommandTemplate({})).toThrow();
    expect(() => accessibilityVoiceTemplate({})).toThrow();
  });

  it('respecte le consentement utilisateur', () => {
    window.localStorage.removeItem('voice_feature_consent');
    expect(() => speechSynthesisTemplate({ text: 'Test', lang: 'fr-FR' })).toThrow(/Consentement requis/);
    window.localStorage.setItem('voice_feature_consent', 'true');
  });

  it('purge les logs de génération vocale (droit à l’oubli RGPD)', () => {
    speechSynthesisTemplate({ text: 'Test', lang: 'fr-FR' });
    expect(window.localStorage.getItem('voice_template_logs')).not.toBeNull();
    clearLocalVoiceTemplateLogs();
    expect(window.localStorage.getItem('voice_template_logs')).toBeNull();
  });
});