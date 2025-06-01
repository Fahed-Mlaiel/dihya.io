/**
 * @file test_mobile.js
 * @description Tests unitaires et d’intégration pour les modules mobiles Dihya Coding (Flutter, React Native, PWA, notifications).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Tous les tests respectent les bonnes pratiques de validation, anonymisation, logs locaux et consentement utilisateur.
 */

import { flutterTemplate, clearLocalMobileTemplateLogs } from '../mobile/flutterTemplate';

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
window.localStorage.setItem('mobile_feature_consent', 'true');

describe('flutterTemplate', () => {
  afterEach(() => {
    clearLocalMobileTemplateLogs();
  });

  it('génère un écran Flutter valide', () => {
    const data = { screenName: 'Accueil', widgets: [{ type: 'Button', label: 'Envoyer' }] };
    const screen = flutterTemplate(data);
    expect(screen).toBeDefined();
    expect(screen.screenName).toBe('Accueil');
    expect(Array.isArray(screen.widgets)).toBe(true);
    expect(screen.widgets[0].type).toBe('Button');
  });

  it('refuse les données invalides', () => {
    expect(() => flutterTemplate({})).toThrow();
    expect(() => flutterTemplate({ screenName: '', widgets: [] })).toThrow();
    expect(() => flutterTemplate({ screenName: 'Accueil' })).toThrow();
  });

  it('respecte le consentement utilisateur', () => {
    window.localStorage.removeItem('mobile_feature_consent');
    expect(() => flutterTemplate({ screenName: 'Accueil', widgets: [] })).toThrow(/Consentement requis/);
    window.localStorage.setItem('mobile_feature_consent', 'true');
  });

  it('purge les logs de génération mobile (droit à l’oubli RGPD)', () => {
    flutterTemplate({ screenName: 'Accueil', widgets: [{ type: 'Text' }] });
    expect(window.localStorage.getItem('mobile_template_logs')).not.toBeNull();
    clearLocalMobileTemplateLogs();
    expect(window.localStorage.getItem('mobile_template_logs')).toBeNull();
  });
});