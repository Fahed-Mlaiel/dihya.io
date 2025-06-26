// Initialisation des tests Validations (Node.js)
const fs = require('fs');
const path = require('path');
const { validateAsset } = require('../../validations/asset_validation.js');

const tests = {};
fs.readdirSync(__dirname).forEach(file => {
  if (file.endsWith('.js') && file !== '__init__.js') {
    const name = file.replace('.js', '');
    tests[name] = require('./' + file);
  }
});

describe('validateAsset', () => {
  it('existe', () => {
    expect(typeof validateAsset).toBe('function');
  });
});

module.exports = tests;

