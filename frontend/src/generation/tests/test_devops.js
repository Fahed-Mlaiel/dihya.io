/**
 * @file test_devops.js
 * @description Tests unitaires et d’intégration pour les modules DevOps Dihya Coding (CI/CD, Docker, monitoring, IaC).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Tous les tests respectent les bonnes pratiques de validation, anonymisation, logs locaux et consentement utilisateur.
 */

import { devopsTemplate, clearLocalDevopsTemplateLogs } from '../devops/devopsTemplate';

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
window.localStorage.setItem('devops_feature_consent', 'true');

describe('devopsTemplate', () => {
  afterEach(() => {
    clearLocalDevopsTemplateLogs();
  });

  it('génère un module CI/CD valide', () => {
    const data = { cicd: { provider: 'GitHub Actions', steps: 5 } };
    const module = devopsTemplate({ type: 'cicd', data });
    expect(module.cicd).toBeDefined();
    expect(module.cicd.provider).toBe('GitHub Actions');
    expect(module.cicd.steps).toBe(5);
  });

  it('génère un module Docker valide', () => {
    const data = { docker: { image: 'node:18', ports: [3000] } };
    const module = devopsTemplate({ type: 'docker', data });
    expect(module.docker).toBeDefined();
    expect(module.docker.image).toBe('node:18');
    expect(Array.isArray(module.docker.ports)).toBe(true);
  });

  it('génère un module monitoring valide', () => {
    const data = { monitoring: { tool: 'Prometheus', alerts: true } };
    const module = devopsTemplate({ type: 'monitoring', data });
    expect(module.monitoring).toBeDefined();
    expect(module.monitoring.tool).toBe('Prometheus');
    expect(module.monitoring.alerts).toBe(true);
  });

  it('génère un module IaC valide', () => {
    const data = { iac: { provider: 'Terraform', resources: 3 } };
    const module = devopsTemplate({ type: 'iac', data });
    expect(module.iac).toBeDefined();
    expect(module.iac.provider).toBe('Terraform');
    expect(module.iac.resources).toBe(3);
  });

  it('refuse un type de module non supporté', () => {
    expect(() => devopsTemplate({ type: 'unknown', data: {} })).toThrow();
  });

  it('refuse des données invalides', () => {
    expect(() => devopsTemplate({ type: 'cicd', data: {} })).toThrow();
    expect(() => devopsTemplate({ type: 'docker', data: {} })).toThrow();
    expect(() => devopsTemplate({ type: 'monitoring', data: {} })).toThrow();
    expect(() => devopsTemplate({ type: 'iac', data: {} })).toThrow();
  });

  it('respecte le consentement utilisateur', () => {
    window.localStorage.removeItem('devops_feature_consent');
    expect(() => devopsTemplate({ type: 'cicd', data: { cicd: {} } })).toThrow(/Consentement requis/);
    window.localStorage.setItem('devops_feature_consent', 'true');
  });

  it('purge les logs de génération DevOps (droit à l’oubli RGPD)', () => {
    devopsTemplate({ type: 'cicd', data: { cicd: { provider: 'GitHub Actions' } } });
    expect(window.localStorage.getItem('devops_template_logs')).not.toBeNull();
    clearLocalDevopsTemplateLogs();
    expect(window.localStorage.getItem('devops_template_logs')).toBeNull();
  });
});