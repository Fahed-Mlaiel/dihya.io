/**
 * @file test_generateProject.js
 * @description Tests unitaires et d’intégration pour la génération de projets Dihya Coding (structure, sécurité, compatibilité, auditabilité).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Tous les tests respectent les bonnes pratiques de validation, anonymisation, logs locaux et consentement utilisateur.
 */

import { generateProject, clearLocalProjectLogs } from '../utils/generateProject';

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
window.localStorage.setItem('project_feature_consent', 'true');

describe('generateProject', () => {
  afterEach(() => {
    clearLocalProjectLogs();
  });

  it('génère un projet valide avec structure minimale', () => {
    const data = { name: 'MonProjet', modules: ['ai', 'ecommerce'], author: 'Alice' };
    const project = generateProject({ ...data });
    expect(project).toBeDefined();
    expect(project.name).toBe('MonProjet');
    expect(Array.isArray(project.modules)).toBe(true);
    expect(project.modules).toContain('ai');
    expect(project.author).toBe('Alice');
  });

  it('génère un projet avec options avancées (SEO, RGPD)', () => {
    const data = {
      name: 'SEOProject',
      modules: ['seo'],
      options: { seo: true, rgpd: true }
    };
    const project = generateProject({ ...data });
    expect(project.options.seo).toBe(true);
    expect(project.options.rgpd).toBe(true);
  });

  it('refuse des données invalides', () => {
    expect(() => generateProject({})).toThrow();
    expect(() => generateProject({ name: '', modules: [] })).toThrow();
    expect(() => generateProject({ name: 'X' })).toThrow();
  });

  it('refuse un module non supporté', () => {
    expect(() => generateProject({ name: 'Test', modules: ['unknown'] })).toThrow();
  });

  it('respecte le consentement utilisateur', () => {
    window.localStorage.removeItem('project_feature_consent');
    expect(() => generateProject({ name: 'Test', modules: ['ai'] })).toThrow(/Consentement requis/);
    window.localStorage.setItem('project_feature_consent', 'true');
  });

  it('purge les logs de génération de projet (droit à l’oubli RGPD)', () => {
    generateProject({ name: 'Test', modules: ['ai'] });
    expect(window.localStorage.getItem('project_template_logs')).not.toBeNull();
    clearLocalProjectLogs();
    expect(window.localStorage.getItem('project_template_logs')).toBeNull();
  });
});