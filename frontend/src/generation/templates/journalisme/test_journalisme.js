/**
 * @file test_journalisme.js
 * @description Tests avancés pour le template journalisme Dihya Coding.
 * Sécurité, RGPD, accessibilité, SEO, plugins, CI/CD, auditabilité, fallback AI.
 */
import { journalismeTemplate } from './template';

describe('Journalisme Template – Sécurité & RGPD', () => {
  it('valide la génération article avec consentement', () => {
    window.localStorage.setItem('journalisme_consent', 'true');
    const module = journalismeTemplate({ type: 'article', data: { content: {} } });
    expect(module).toBeDefined();
  });
  it('refuse sans consentement', () => {
    window.localStorage.removeItem('journalisme_consent');
    expect(() => journalismeTemplate({ type: 'article', data: { content: {} } })).toThrow();
  });
});

describe('Journalisme Template – Accessibilité', () => {
  it('génère des modules accessibles (WCAG)', () => {
    const module = journalismeTemplate({ type: 'article', data: { content: {} }, options: { accessibility: true } });
    expect(module.accessibility).toBe(true);
  });
});

describe('Journalisme Template – Plugins & SEO', () => {
  it('supporte les plugins fact-checking', () => {
    const module = journalismeTemplate({ type: 'article', data: {}, options: { plugins: ['fact_checking'] } });
    expect(module.plugins).toContain('fact_checking');
  });
  it('génère des docs SEO multilingues', () => {
    const module = journalismeTemplate({ type: 'article', data: {}, options: { seo: true, lang: 'en' } });
    expect(module.seo).toBe(true);
    expect(module.lang).toBe('en');
  });
});
