/**
 * @file test_infra.js
 * @description Tests unitaires et d’intégration pour les modules d’infrastructure Dihya Coding (sauvegardes, restauration, monitoring, haute disponibilité).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Tous les tests respectent les bonnes pratiques de validation, anonymisation, logs locaux et consentement utilisateur.
 */

import { infraTemplate, clearLocalInfraTemplateLogs } from '../infra/infraTemplate';

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
window.localStorage.setItem('infra_feature_consent', 'true');

describe('infraTemplate', () => {
  afterEach(() => {
    clearLocalInfraTemplateLogs();
  });

  it('génère un module sauvegarde valide', () => {
    const data = { backup: { frequency: 'daily', retention: 7 } };
    const module = infraTemplate({ type: 'backup', data });
    expect(module.backup).toBeDefined();
    expect(module.backup.frequency).toBe('daily');
    expect(module.backup.retention).toBe(7);
  });

  it('génère un module restauration valide', () => {
    const data = { restore: { point: '2024-01-01T00:00:00Z' } };
    const module = infraTemplate({ type: 'restore', data });
    expect(module.restore).toBeDefined();
    expect(module.restore.point).toBe('2024-01-01T00:00:00Z');
  });

  it('génère un module monitoring valide', () => {
    const data = { monitoring: { tool: 'Grafana', alerts: true } };
    const module = infraTemplate({ type: 'monitoring', data });
    expect(module.monitoring).toBeDefined();
    expect(module.monitoring.tool).toBe('Grafana');
    expect(module.monitoring.alerts).toBe(true);
  });

  it('génère un module haute disponibilité valide', () => {
    const data = { ha: { enabled: true, nodes: 3 } };
    const module = infraTemplate({ type: 'ha', data });
    expect(module.ha).toBeDefined();
    expect(module.ha.enabled).toBe(true);
    expect(module.ha.nodes).toBe(3);
  });

  it('refuse un type de module non supporté', () => {
    expect(() => infraTemplate({ type: 'unknown', data: {} })).toThrow();
  });

  it('refuse des données invalides', () => {
    expect(() => infraTemplate({ type: 'backup', data: {} })).toThrow();
    expect(() => infraTemplate({ type: 'restore', data: {} })).toThrow();
    expect(() => infraTemplate({ type: 'monitoring', data: {} })).toThrow();
    expect(() => infraTemplate({ type: 'ha', data: {} })).toThrow();
  });

  it('respecte le consentement utilisateur', () => {
    window.localStorage.removeItem('infra_feature_consent');
    expect(() => infraTemplate({ type: 'backup', data: { backup: {} } })).toThrow(/Consentement requis/);
    window.localStorage.setItem('infra_feature_consent', 'true');
  });

  it('purge les logs de génération infra (droit à l’oubli RGPD)', () => {
    infraTemplate({ type: 'backup', data: { backup: { frequency: 'daily' } } });
    expect(window.localStorage.getItem('infra_template_logs')).not.toBeNull();
    clearLocalInfraTemplateLogs();
    expect(window.localStorage.getItem('infra_template_logs')).toBeNull();
  });
});