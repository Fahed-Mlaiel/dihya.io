/**
 * @file test_utils.js
 * @description Tests unitaires et d’intégration pour les utilitaires Dihya Coding (validation, formatage, anonymisation, logs, SEO).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Tous les tests respectent les bonnes pratiques de validation, anonymisation, logs locaux et consentement utilisateur.
 */

import { validateEmail } from '../utils/validationUtils';
import { anonymizeUser } from '../utils/anonymizeUtils';
import { formatDate } from '../utils/formatUtils';
import { logEvent, clearLocalLogUtils } from '../utils/logUtils';
import { slugify } from '../utils/seoUtils';

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
window.localStorage.setItem('utils_feature_consent', 'true');

describe('Utils Dihya Coding', () => {
  afterEach(() => {
    clearLocalLogUtils();
  });

  it('valide correctement un email', () => {
    expect(validateEmail('user@dihya.app')).toBe(true);
    expect(validateEmail('invalid-email')).toBe(false);
  });

  it('anonymise correctement un utilisateur', () => {
    const user = { email: 'user@dihya.app', name: 'Alice', phone: '0600000000' };
    const anon = anonymizeUser(user);
    expect(anon.email).toBe('[email]');
    expect(anon.phone).toBe('[phone]');
    expect(anon.name).toBe('Alice');
  });

  it('formate correctement une date', () => {
    const date = new Date('2024-01-01T12:00:00Z');
    const formatted = formatDate(date, 'fr-FR');
    expect(typeof formatted).toBe('string');
    expect(formatted).toContain('2024');
  });

  it('génère un slug SEO valide', () => {
    const slug = slugify('Accueil Dihya Coding !');
    expect(slug).toBe('accueil-dihya-coding');
  });

  it('loggue un événement localement (auditabilité)', () => {
    logEvent('test_action', { foo: 'bar' });
    const logs = JSON.parse(window.localStorage.getItem('log_utils_logs') || '[]');
    expect(logs.length).toBeGreaterThan(0);
    expect(logs[0].action).toBe('test_action');
  });

  it('respecte le consentement utilisateur', () => {
    window.localStorage.removeItem('utils_feature_consent');
    expect(() => validateEmail('user@dihya.app')).toThrow(/Consentement requis/);
    window.localStorage.setItem('utils_feature_consent', 'true');
  });

  it('purge les logs utilitaires (droit à l’oubli RGPD)', () => {
    logEvent('test_action', { foo: 'bar' });
    expect(window.localStorage.getItem('log_utils_logs')).not.toBeNull();
    clearLocalLogUtils();
    expect(window.localStorage.getItem('log_utils_logs')).toBeNull();
  });
});