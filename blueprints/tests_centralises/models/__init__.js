// Initialisation des tests Models (Node.js)
const fs = require('fs');
const path = require('path');

const tests = {};
fs.readdirSync(__dirname).forEach(file => {
  if (file.endsWith('.js') && file !== '__init__.js') {
    const name = file.replace('.js', '');
    tests[name] = require('./' + file);
  }
});

const { AssetModel } = require('../../models/asset_model.js');
describe('AssetModel', () => {
  it('existe', () => {
    expect(typeof AssetModel).toBe('function');
  });
});

module.exports = tests;

