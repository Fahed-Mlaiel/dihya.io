/**
 * @file test_ecommerce.js
 * @description Tests unitaires et d’intégration pour les modules e-commerce Dihya Coding (catalogue, panier, paiement, utilisateur).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Tous les tests respectent les bonnes pratiques de validation, anonymisation, logs locaux et consentement utilisateur.
 */

import { ecommerceTemplate, clearLocalEcommerceTemplateLogs } from '../ecommerce/template';

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
window.localStorage.setItem('ecommerce_feature_consent', 'true');

describe('ecommerceTemplate', () => {
  afterEach(() => {
    clearLocalEcommerceTemplateLogs();
  });

  it('génère un module catalogue valide', () => {
    const data = { products: [{ name: 'Produit A', price: 10 }] };
    const module = ecommerceTemplate({ type: 'catalog', data });
    expect(module.catalog).toBeDefined();
    expect(Array.isArray(module.catalog)).toBe(true);
    expect(module.catalog[0].name).toBe('Produit A');
  });

  it('génère un module panier valide', () => {
    const data = { items: [{ productId: 1, qty: 2 }], total: 20 };
    const module = ecommerceTemplate({ type: 'cart', data });
    expect(module.cart).toBeDefined();
    expect(module.total).toBe(20);
  });

  it('génère un module checkout valide', () => {
    const data = { order: { id: 1 }, payment: { method: 'CB' } };
    const module = ecommerceTemplate({ type: 'checkout', data });
    expect(module.order).toBeDefined();
    expect(module.payment).toBeDefined();
  });

  it('génère un module utilisateur avec anonymisation', () => {
    const data = { user: { email: 'user@dihya.app', password: 'secret', name: 'Alice' } };
    const module = ecommerceTemplate({ type: 'user', data });
    expect(module.user.email).toBe('[email]');
    expect(module.user.password).toBe('[protected]');
    expect(module.user.name).toBe('Alice');
  });

  it('refuse un type de module non supporté', () => {
    expect(() => ecommerceTemplate({ type: 'unknown', data: {} })).toThrow();
  });

  it('refuse des données invalides', () => {
    expect(() => ecommerceTemplate({ type: 'catalog', data: {} })).toThrow();
    expect(() => ecommerceTemplate({ type: 'cart', data: {} })).toThrow();
    expect(() => ecommerceTemplate({ type: 'checkout', data: {} })).toThrow();
    expect(() => ecommerceTemplate({ type: 'user', data: {} })).toThrow();
  });

  it('respecte le consentement utilisateur', () => {
    window.localStorage.removeItem('ecommerce_feature_consent');
    expect(() => ecommerceTemplate({ type: 'catalog', data: { products: [] } })).toThrow(/Consentement requis/);
    window.localStorage.setItem('ecommerce_feature_consent', 'true');
  });

  it('purge les logs de génération (droit à l’oubli RGPD)', () => {
    const data = { products: [{ name: 'Produit B', price: 15 }] };
    ecommerceTemplate({ type: 'catalog', data });
    expect(window.localStorage.getItem('ecommerce_template_logs')).not.toBeNull();
    clearLocalEcommerceTemplateLogs();
    expect(window.localStorage.getItem('ecommerce_template_logs')).toBeNull();
  });
});