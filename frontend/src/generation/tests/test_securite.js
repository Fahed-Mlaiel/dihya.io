/**
 * @file test_security.js
 * @description Tests unitaires et d’intégration pour les modules de sécurité Dihya Coding (anti-DDoS, rate limiting, CORS, headers, validation, audit).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Tous les tests respectent les bonnes pratiques de validation, anonymisation, logs locaux et consentement utilisateur.
 */

import { antiDDoSTemplate, rateLimitTemplate, corsTemplate, headersTemplate, validationTemplate, auditTemplate, clearLocalSecurityTemplateLogs } from '../security/antiDDoSTemplate';

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
window.localStorage.setItem('security_feature_consent', 'true');

describe('securityTemplates', () => {
  afterEach(() => {
    clearLocalSecurityTemplateLogs();
  });

  it('génère une protection anti-DDoS valide', () => {
    const data = { userId: 'user1', endpoint: '/api/data' };
    const protection = antiDDoSTemplate(data);
    expect(protection).toBeDefined();
    expect(protection.userId).toBe('user1');
    expect(protection.endpoint).toBe('/api/data');
  });

  it('génère une règle de rate limiting valide', () => {
    const data = { userId: 'user2', limit: 100, window: 60 };
    const rateLimit = rateLimitTemplate(data);
    expect(rateLimit).toBeDefined();
    expect(rateLimit.limit).toBe(100);
    expect(rateLimit.window).toBe(60);
  });

  it('génère une configuration CORS valide', () => {
    const data = { origin: 'https://dihya.app', methods: ['GET', 'POST'] };
    const cors = corsTemplate(data);
    expect(cors).toBeDefined();
    expect(cors.origin).toBe('https://dihya.app');
    expect(cors.methods).toContain('GET');
  });

  it('génère des headers de sécurité valides', () => {
    const data = { csp: "default-src 'self'", hsts: true };
    const headers = headersTemplate(data);
    expect(headers).toBeDefined();
    expect(headers.csp).toContain('self');
    expect(headers.hsts).toBe(true);
  });

  it('génère une validation d’entrée valide', () => {
    const data = { value: 'test@example.com', type: 'email' };
    const validation = validationTemplate(data);
    expect(validation).toBeDefined();
    expect(validation.type).toBe('email');
    expect(validation.isValid).toBe(true);
  });

  it('génère un audit de sécurité valide', () => {
    const data = { action: 'login', userId: 'user3', status: 'success' };
    const audit = auditTemplate(data);
    expect(audit).toBeDefined();
    expect(audit.action).toBe('login');
    expect(audit.status).toBe('success');
  });

  it('refuse des données invalides', () => {
    expect(() => antiDDoSTemplate({})).toThrow();
    expect(() => rateLimitTemplate({})).toThrow();
    expect(() => corsTemplate({})).toThrow();
    expect(() => headersTemplate({})).toThrow();
    expect(() => validationTemplate({})).toThrow();
    expect(() => auditTemplate({})).toThrow();
  });

  it('respecte le consentement utilisateur', () => {
    window.localStorage.removeItem('security_feature_consent');
    expect(() => antiDDoSTemplate({ userId: 'user1', endpoint: '/api/data' })).toThrow(/Consentement requis/);
    window.localStorage.setItem('security_feature_consent', 'true');
  });

  it('purge les logs de génération sécurité (droit à l’oubli RGPD)', () => {
    antiDDoSTemplate({ userId: 'user1', endpoint: '/api/data' });
    expect(window.localStorage.getItem('security_template_logs')).not.toBeNull();
    clearLocalSecurityTemplateLogs();
    expect(window.localStorage.getItem('security_template_logs')).toBeNull();
  });
});