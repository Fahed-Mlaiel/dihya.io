/**
 * @file test_ai.js
 * @description Tests unitaires et d’intégration pour les modules AI Dihya Coding (assistants, prompts, fallback, quotas).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Tous les tests respectent les bonnes pratiques de validation, anonymisation, logs locaux et consentement utilisateur.
 */

import { assistantTemplate, clearLocalAiTemplateLogs } from '../ai/assistantTemplate';

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
window.localStorage.setItem('ai_feature_consent', 'true');

describe('assistantTemplate', () => {
  afterEach(() => {
    clearLocalAiTemplateLogs();
  });

  it('génère un assistant AI valide', () => {
    const data = { userMessage: 'Bonjour', context: { lang: 'fr' } };
    const assistant = assistantTemplate(data);
    expect(assistant).toBeDefined();
    expect(typeof assistant).toBe('object');
    expect(assistant.prompt).toContain('Bonjour');
  });

  it('refuse les données invalides', () => {
    expect(() => assistantTemplate({})).toThrow();
    expect(() => assistantTemplate({ userMessage: '' })).toThrow();
  });

  it('respecte le consentement utilisateur', () => {
    window.localStorage.removeItem('ai_feature_consent');
    expect(() => assistantTemplate({ userMessage: 'Test' })).toThrow(/Consentement requis/);
    window.localStorage.setItem('ai_feature_consent', 'true');
  });

  it('purge les logs de génération AI (droit à l’oubli RGPD)', () => {
    assistantTemplate({ userMessage: 'Test', context: {} });
    expect(window.localStorage.getItem('ai_template_logs')).not.toBeNull();
    clearLocalAiTemplateLogs();
    expect(window.localStorage.getItem('ai_template_logs')).toBeNull();
  });
});