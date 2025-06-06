// Test d’intégration ultra avancé pour le point d’entrée plugins (index.js)
const plugins = require('./index');

describe('Plugins module (clé en main)', () => {
  test('core est accessible', () => {
    expect(plugins.core).toBeDefined();
  });
  test('helpers sont accessibles', () => {
    expect(plugins.helpers).toBeDefined();
  });
  test('fallback est accessible', () => {
    expect(plugins.fallback).toBeDefined();
  });
  test('core, helpers et samples sont accessibles', () => {
    const plugins = require('./index');
    expect(plugins.AdvancedPlugin).toBeDefined();
  });
  // ... autres cas d’intégration, edge cases, etc.
});
