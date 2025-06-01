/**
 * @file test_validators.js
 * @description Tests unitaires et d’intégration pour les validateurs Dihya Coding (email, mot de passe, nombre, date, personnalisés).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Tous les tests respectent les bonnes pratiques de validation, anonymisation, logs locaux et consentement utilisateur.
 */

import { emailValidator } from '../validators/emailValidator';
import { passwordValidator } from '../validators/passwordValidator';
import { numberValidator } from '../validators/numberValidator';
import { dateValidator } from '../validators/dateValidator';
import { customValidator } from '../validators/customValidator';
import { clearLocalValidatorLogs } from '../validators/logValidatorUtils';

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
window.localStorage.setItem('validators_feature_consent', 'true');

describe('Validators Dihya Coding', () => {
  afterEach(() => {
    clearLocalValidatorLogs();
  });

  it('valide correctement un email', () => {
    expect(emailValidator('user@dihya.app')).toBe(true);
    expect(emailValidator('invalid-email')).toBe(false);
  });

  it('valide correctement un mot de passe', () => {
    expect(passwordValidator('StrongPassw0rd!')).toBe(true);
    expect(passwordValidator('weak')).toBe(false);
  });

  it('valide correctement un nombre', () => {
    expect(numberValidator(42)).toBe(true);
    expect(numberValidator('not-a-number')).toBe(false);
  });

  it('valide correctement une date', () => {
    expect(dateValidator('2024-01-01')).toBe(true);
    expect(dateValidator('invalid-date')).toBe(false);
  });

  it('valide une règle personnalisée', () => {
    const rule = value => value === 'ok';
    expect(customValidator('ok', rule)).toBe(true);
    expect(customValidator('ko', rule)).toBe(false);
  });

  it('respecte le consentement utilisateur', () => {
    window.localStorage.removeItem('validators_feature_consent');
    expect(() => emailValidator('user@dihya.app')).toThrow(/Consentement requis/);
    window.localStorage.setItem('validators_feature_consent', 'true');
  });

  it('purge les logs de validation (droit à l’oubli RGPD)', () => {
    emailValidator('user@dihya.app');
    expect(window.localStorage.getItem('validator_logs')).not.toBeNull();
    clearLocalValidatorLogs();
    expect(window.localStorage.getItem('validator_logs')).toBeNull();
  });
});