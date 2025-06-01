/**
 * @file test_blueprints.js
 * @description Tests unitaires et d’intégration pour les blueprints Dihya Coding (génération de structures, compatibilité, sécurité, auditabilité).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Tous les tests respectent les bonnes pratiques de validation, anonymisation, logs locaux et consentement utilisateur.
 */

import { generateBlueprint, clearLocalBlueprintLogs } from '../docs/blueprintTemplate';

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
window.localStorage.setItem('blueprint_feature_consent', 'true');

describe('generateBlueprint', () => {
  afterEach(() => {
    clearLocalBlueprintLogs();
  });

  it('génère un blueprint valide pour un module AI', () => {
    const data = { type: 'ai', name: 'Assistant', config: { lang: 'fr' } };
    const blueprint = generateBlueprint({ ...data });
    expect(blueprint).toBeDefined();
    expect(blueprint.type).toBe('ai');
    expect(blueprint.name).toBe('Assistant');
    expect(blueprint.config.lang).toBe('fr');
  });

  it('génère un blueprint valide pour un module e-commerce', () => {
    const data = { type: 'ecommerce', name: 'Shop', config: { products: 10 } };
    const blueprint = generateBlueprint({ ...data });
    expect(blueprint.type).toBe('ecommerce');
    expect(blueprint.name).toBe('Shop');
    expect(blueprint.config.products).toBe(10);
  });

  it('refuse un type de blueprint non supporté', () => {
    expect(() => generateBlueprint({ type: 'unknown', name: 'X', config: {} })).toThrow();
  });

  it('refuse des données invalides', () => {
    expect(() => generateBlueprint({})).toThrow();
    expect(() => generateBlueprint({ type: 'ai' })).toThrow();
  });

  it('respecte le consentement utilisateur', () => {
    window.localStorage.removeItem('blueprint_feature_consent');
    expect(() => generateBlueprint({ type: 'ai', name: 'Test', config: {} })).toThrow(/Consentement requis/);
    window.localStorage.setItem('blueprint_feature_consent', 'true');
  });

  it('purge les logs de génération de blueprint (droit à l’oubli RGPD)', () => {
    generateBlueprint({ type: 'ai', name: 'Test', config: {} });
    expect(window.localStorage.getItem('blueprint_template_logs')).not.toBeNull();
    clearLocalBlueprintLogs();
    expect(window.localStorage.getItem('blueprint_template_logs')).toBeNull();
  });
});