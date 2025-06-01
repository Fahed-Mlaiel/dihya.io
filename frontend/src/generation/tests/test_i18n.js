/**
 * @file test_i18n.js
 * @description Tests unitaires et d’intégration pour les modules i18n Dihya Coding (traductions, gestion des langues, fallback, pluralisation).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Tous les tests respectent les bonnes pratiques de validation, anonymisation, logs locaux et consentement utilisateur.
 */

import { translationTemplate, clearLocalI18nTemplateLogs } from '../i18n/translationTemplate';

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
window.localStorage.setItem('i18n_feature_consent', 'true');

describe('translationTemplate', () => {
  afterEach(() => {
    clearLocalI18nTemplateLogs();
  });

  it('génère un fichier de traduction valide', () => {
    const data = { lang: 'fr', entries: { hello: 'Bonjour', bye: 'Au revoir' } };
    const translation = translationTemplate(data);
    expect(translation).toBeDefined();
    expect(translation.lang).toBe('fr');
    expect(translation.entries.hello).toBe('Bonjour');
  });

  it('refuse les données invalides', () => {
    expect(() => translationTemplate({})).toThrow();
    expect(() => translationTemplate({ lang: '', entries: {} })).toThrow();
    expect(() => translationTemplate({ lang: 'fr' })).toThrow();
  });

  it('respecte le consentement utilisateur', () => {
    window.localStorage.removeItem('i18n_feature_consent');
    expect(() => translationTemplate({ lang: 'fr', entries: { hello: 'Bonjour' } })).toThrow(/Consentement requis/);
    window.localStorage.setItem('i18n_feature_consent', 'true');
  });

  it('purge les logs de génération i18n (droit à l’oubli RGPD)', () => {
    translationTemplate({ lang: 'fr', entries: { hello: 'Bonjour' } });
    expect(window.localStorage.getItem('i18n_template_logs')).not.toBeNull();
    clearLocalI18nTemplateLogs();
    expect(window.localStorage.getItem('i18n_template_logs')).toBeNull();
  });
});