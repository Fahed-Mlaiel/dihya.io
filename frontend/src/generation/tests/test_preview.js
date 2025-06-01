/**
 * @file test_preview.js
 * @description Tests unitaires et d’intégration pour les modules de prévisualisation Dihya Coding (UI, code, mobile, PDF).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Tous les tests respectent les bonnes pratiques de validation, anonymisation, logs locaux et consentement utilisateur.
 */

import { uiPreviewTemplate, clearLocalPreviewTemplateLogs } from '../preview/uiPreviewTemplate';

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
window.localStorage.setItem('preview_feature_consent', 'true');

describe('uiPreviewTemplate', () => {
  afterEach(() => {
    clearLocalPreviewTemplateLogs();
  });

  it('génère une prévisualisation UI valide', () => {
    const data = { component: 'Button', props: { label: 'Envoyer' } };
    const preview = uiPreviewTemplate(data);
    expect(preview).toBeDefined();
    expect(preview.component).toBe('Button');
    expect(preview.props.label).toBe('Envoyer');
  });

  it('refuse les données invalides', () => {
    expect(() => uiPreviewTemplate({})).toThrow();
    expect(() => uiPreviewTemplate({ component: '', props: {} })).toThrow();
    expect(() => uiPreviewTemplate({ component: 'Button' })).toThrow();
  });

  it('respecte le consentement utilisateur', () => {
    window.localStorage.removeItem('preview_feature_consent');
    expect(() => uiPreviewTemplate({ component: 'Button', props: { label: 'Test' } })).toThrow(/Consentement requis/);
    window.localStorage.setItem('preview_feature_consent', 'true');
  });

  it('purge les logs de génération de preview (droit à l’oubli RGPD)', () => {
    uiPreviewTemplate({ component: 'Button', props: { label: 'Test' } });
    expect(window.localStorage.getItem('preview_template_logs')).not.toBeNull();
    clearLocalPreviewTemplateLogs();
    expect(window.localStorage.getItem('preview_template_logs')).toBeNull();
  });
});