// __init__.test.js – Tests unitaires JS pour __init__.js (import dynamique)
const fs = require('fs');
const path = require('path');
const entry = require('./__init__');

describe('__init__.js Threed utils', () => {
  it('importe dynamiquement tous les modules .js', () => {
    const files = fs.readdirSync(__dirname).filter(f => f.endsWith('.js') && f !== '__init__.js' && f.endsWith('.js'));
    files.forEach(f => {
      expect(() => require(path.join(__dirname, f))).not.toThrow();
    });
  });
});

describe('Initialisation JS helpers globaux threed', () => {
  it('doit charger l’index sans erreur', () => {
    expect(entry).toBeDefined();
  });
});

// __init__.test.js – Test d'initialisation helpers JS globaux
const js = require('./__init__');
describe('Init JS helpers globaux', () => {
  it('expose le module JS', () => {
    expect(js).toBeDefined();
  });
});
