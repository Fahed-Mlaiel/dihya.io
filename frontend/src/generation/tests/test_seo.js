/**
 * @file test_seo.js
 * @description Tests unitaires et d’intégration pour les modules SEO Dihya Coding (balises meta, sitemap, robots.txt, audits Lighthouse).
 * Garantit design moderne, SEO optimal, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Tous les tests respectent les bonnes pratiques de validation, anonymisation, logs locaux et consentement utilisateur.
 */

import { metaTemplate, sitemapTemplate, robotsTemplate, lighthouseTemplate, clearLocalSeoTemplateLogs } from '../seo/metaTemplate';

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
window.localStorage.setItem('seo_feature_consent', 'true');

describe('seoTemplates', () => {
  afterEach(() => {
    clearLocalSeoTemplateLogs();
  });

  it('génère des balises meta valides', () => {
    const data = {
      title: 'Accueil – Dihya Coding',
      description: 'Plateforme moderne, sécurisée et conforme RGPD pour la génération de code.',
      keywords: ['génération', 'code', 'sécurité', 'RGPD']
    };
    const meta = metaTemplate(data);
    expect(meta).toBeDefined();
    expect(meta.title).toBe('Accueil – Dihya Coding');
    expect(meta.description).toContain('moderne');
    expect(Array.isArray(meta.keywords)).toBe(true);
  });

  it('génère un sitemap valide', () => {
    const data = { urls: ['/', '/about', '/contact'] };
    const sitemap = sitemapTemplate(data);
    expect(sitemap).toBeDefined();
    expect(Array.isArray(sitemap.urls)).toBe(true);
    expect(sitemap.urls).toContain('/about');
  });

  it('génère un robots.txt valide', () => {
    const data = { allow: ['/', '/public'], disallow: ['/admin'] };
    const robots = robotsTemplate(data);
    expect(robots).toBeDefined();
    expect(Array.isArray(robots.allow)).toBe(true);
    expect(robots.disallow).toContain('/admin');
  });

  it('génère un audit Lighthouse valide', () => {
    const data = { url: 'https://dihya.app', audits: ['performance', 'accessibility'] };
    const audit = lighthouseTemplate(data);
    expect(audit).toBeDefined();
    expect(audit.url).toBe('https://dihya.app');
    expect(audit.audits).toContain('performance');
  });

  it('refuse des données invalides', () => {
    expect(() => metaTemplate({})).toThrow();
    expect(() => sitemapTemplate({})).toThrow();
    expect(() => robotsTemplate({})).toThrow();
    expect(() => lighthouseTemplate({})).toThrow();
  });

  it('respecte le consentement utilisateur', () => {
    window.localStorage.removeItem('seo_feature_consent');
    expect(() => metaTemplate({ title: 'Test', description: 'desc', keywords: [] })).toThrow(/Consentement requis/);
    window.localStorage.setItem('seo_feature_consent', 'true');
  });

  it('purge les logs de génération SEO (droit à l’oubli RGPD)', () => {
    metaTemplate({ title: 'Test', description: 'desc', keywords: ['a'] });
    expect(window.localStorage.getItem('seo_template_logs')).not.toBeNull();
    clearLocalSeoTemplateLogs();
    expect(window.localStorage.getItem('seo_template_logs')).toBeNull();
  });
});