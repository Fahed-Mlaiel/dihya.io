/**
 * @file test_branding.js
 * @description Tests unitaires et d’intégration pour les modules branding Dihya Coding (logos, palettes, guidelines, identité visuelle).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Tous les tests respectent les bonnes pratiques de validation, anonymisation, logs locaux et consentement utilisateur.
 */

import { brandingTemplate, clearLocalBrandingTemplateLogs } from '../branding/brandingTemplate';

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
window.localStorage.setItem('branding_feature_consent', 'true');

describe('brandingTemplate', () => {
  afterEach(() => {
    clearLocalBrandingTemplateLogs();
  });

  it('génère un module logo valide', () => {
    const data = { logo: { url: 'logo.svg', alt: 'Logo Dihya' } };
    const module = brandingTemplate({ type: 'logo', data });
    expect(module.logo).toBeDefined();
    expect(module.logo.url).toBe('logo.svg');
    expect(module.logo.alt).toBe('Logo Dihya');
  });

  it('génère un module palette valide', () => {
    const data = { palette: { primary: '#000', secondary: '#fff' } };
    const module = brandingTemplate({ type: 'palette', data });
    expect(module.palette).toBeDefined();
    expect(module.palette.primary).toBe('#000');
    expect(module.palette.secondary).toBe('#fff');
  });

  it('génère un module guidelines valide', () => {
    const data = { guidelines: { usage: 'Utiliser le logo sur fond clair.' } };
    const module = brandingTemplate({ type: 'guidelines', data });
    expect(module.guidelines).toBeDefined();
    expect(module.guidelines.usage).toContain('fond clair');
  });

  it('refuse un type de module non supporté', () => {
    expect(() => brandingTemplate({ type: 'unknown', data: {} })).toThrow();
  });

  it('refuse des données invalides', () => {
    expect(() => brandingTemplate({ type: 'logo', data: {} })).toThrow();
    expect(() => brandingTemplate({ type: 'palette', data: {} })).toThrow();
    expect(() => brandingTemplate({ type: 'guidelines', data: {} })).toThrow();
  });

  it('respecte le consentement utilisateur', () => {
    window.localStorage.removeItem('branding_feature_consent');
    expect(() => brandingTemplate({ type: 'logo', data: { logo: {} } })).toThrow(/Consentement requis/);
    window.localStorage.setItem('branding_feature_consent', 'true');
  });

  it('purge les logs de génération branding (droit à l’oubli RGPD)', () => {
    brandingTemplate({ type: 'logo', data: { logo: { url: 'logo.svg' } } });
    expect(window.localStorage.getItem('branding_template_logs')).not.toBeNull();
    clearLocalBrandingTemplateLogs();
    expect(window.localStorage.getItem('branding_template_logs')).toBeNull();
  });
});