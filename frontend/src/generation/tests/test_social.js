/**
 * @file test_social.js
 * @description Tests unitaires et d’intégration pour les modules sociaux Dihya Coding (profils, réseaux, partage, commentaires, notifications).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Tous les tests respectent les bonnes pratiques de validation, anonymisation, logs locaux et consentement utilisateur.
 */

import { socialTemplate, clearLocalSocialTemplateLogs } from '../social/template';

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
window.localStorage.setItem('social_feature_consent', 'true');

describe('socialTemplate', () => {
  afterEach(() => {
    clearLocalSocialTemplateLogs();
  });

  it('génère un module profil valide avec anonymisation', () => {
    const data = { profile: { username: 'dihya', email: 'user@dihya.app', phone: '0600000000' } };
    const module = socialTemplate({ type: 'profile', data });
    expect(module.profile).toBeDefined();
    expect(module.profile.username).toBe('dihya');
    expect(module.profile.email).toBe('[email]');
    expect(module.profile.phone).toBe('[phone]');
  });

  it('génère un module réseau valide', () => {
    const data = { network: { friends: ['alice', 'bob'] } };
    const module = socialTemplate({ type: 'network', data });
    expect(module.network).toBeDefined();
    expect(Array.isArray(module.network.friends)).toBe(true);
    expect(module.network.friends).toContain('alice');
  });

  it('génère un module partage valide', () => {
    const data = { share: { url: 'https://dihya.app', title: 'Partage' } };
    const module = socialTemplate({ type: 'share', data });
    expect(module.share).toBeDefined();
    expect(module.share.url).toBe('https://dihya.app');
  });

  it('génère un module commentaire valide avec anonymisation', () => {
    const data = { comment: { text: 'Bravo', authorEmail: 'a@b.com' } };
    const module = socialTemplate({ type: 'comment', data });
    expect(module.comment).toBeDefined();
    expect(module.comment.text).toBe('Bravo');
    expect(module.comment.authorEmail).toBe('[email]');
  });

  it('génère un module notification valide', () => {
    const data = { notification: { message: 'Nouveau message' } };
    const module = socialTemplate({ type: 'notification', data });
    expect(module.notification).toBeDefined();
    expect(module.notification.message).toBe('Nouveau message');
  });

  it('refuse un type de module non supporté', () => {
    expect(() => socialTemplate({ type: 'unknown', data: {} })).toThrow();
  });

  it('refuse des données invalides', () => {
    expect(() => socialTemplate({ type: 'profile', data: {} })).toThrow();
    expect(() => socialTemplate({ type: 'network', data: {} })).toThrow();
    expect(() => socialTemplate({ type: 'share', data: {} })).toThrow();
    expect(() => socialTemplate({ type: 'comment', data: {} })).toThrow();
    expect(() => socialTemplate({ type: 'notification', data: {} })).toThrow();
  });

  it('respecte le consentement utilisateur', () => {
    window.localStorage.removeItem('social_feature_consent');
    expect(() => socialTemplate({ type: 'profile', data: { profile: {} } })).toThrow(/Consentement requis/);
    window.localStorage.setItem('social_feature_consent', 'true');
  });

  it('purge les logs de génération (droit à l’oubli RGPD)', () => {
    const data = { profile: { username: 'dihya', email: 'user@dihya.app' } };
    socialTemplate({ type: 'profile', data });
    expect(window.localStorage.getItem('social_template_logs')).not.toBeNull();
    clearLocalSocialTemplateLogs();
    expect(window.localStorage.getItem('social_template_logs')).toBeNull();
  });
});