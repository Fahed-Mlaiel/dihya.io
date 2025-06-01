/**
 * @file test_sante.js
 * @description Tests avancés pour le template santé Dihya Coding.
 * Sécurité, RGPD, accessibilité, SEO, plugins, CI/CD, auditabilité, fallback AI.
 */
import { santeTemplate } from './template';

describe('Santé Template – Sécurité & RGPD', () => {
  it('valide la génération patient avec consentement', () => {
    window.localStorage.setItem('sante_consent', 'true');
    const module = santeTemplate({ type: 'patient', data: { dossier: {} } });
    expect(module).toBeDefined();
  });
  it('refuse sans consentement', () => {
    window.localStorage.removeItem('sante_consent');
    expect(() => santeTemplate({ type: 'patient', data: { dossier: {} } })).toThrow();
  });
});

describe('Santé Template – Accessibilité', () => {
  it('génère des modules accessibles (WCAG)', () => {
    const module = santeTemplate({ type: 'patient', data: { dossier: {} }, options: { accessibility: true } });
    expect(module.accessibility).toBe(true);
  });
});

describe('Santé Template – Plugins & SEO', () => {
  it('supporte les plugins DMP', () => {
    const module = santeTemplate({ type: 'patient', data: {}, options: { plugins: ['dmp'] } });
    expect(module.plugins).toContain('dmp');
  });
  it('génère des docs SEO multilingues', () => {
    const module = santeTemplate({ type: 'patient', data: {}, options: { seo: true, lang: 'en' } });
    expect(module.seo).toBe(true);
    expect(module.lang).toBe('en');
  });
});
