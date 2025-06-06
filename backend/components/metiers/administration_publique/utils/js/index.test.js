// index.test.js – Tests d'intégration JS pour tous les utilitaires Threed
const utils = require('./index');
describe('Utils Threed (index)', () => {
  it('doit exposer auditThreed', () => {
    expect(typeof utils.auditThreed).toBe('function');
  });
  it('doit exposer i18n', () => {
    expect(typeof utils.i18n).toBe('function');
  });
  it('doit exposer pluginManager', () => {
    expect(typeof utils.pluginManager).toBe('object');
  });
  it('doit exposer logInfo', () => {
    expect(typeof utils.logInfo === 'function' || typeof utils.logger?.logInfo === 'function').toBe(true);
  });
  it('doit exposer recordMetric', () => {
    expect(typeof utils.recordMetric === 'function' || typeof utils.metrics?.recordMetric === 'function').toBe(true);
  });
});
const helpers = require('./index');
describe('Entrée JS helpers globaux threed', () => {
  it('doit exposer les helpers JS globaux (si présents)', () => {
    expect(typeof helpers).toBe('object');
  });
});
// index.test.js – Test d'intégration du point d'entrée JS globaux
const js = require('./index');
describe('Entrée JS helpers globaux', () => {
  it('doit exposer le module JS', () => {
    expect(js).toBeDefined();
  });
});
