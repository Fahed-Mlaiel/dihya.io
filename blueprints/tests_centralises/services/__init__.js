// Initialisation des tests Services (Node.js)
const fs = require('fs');
const path = require('path');

const tests = {};
fs.readdirSync(__dirname).forEach(file => {
  if (file.endsWith('.js') && file !== '__init__.js') {
    const name = file.replace('.js', '');
    tests[name] = require('./' + file);
  }
});

const { AssetService } = require('../../services/asset_service.js');
describe('AssetService', () => {
  it('existe', () => {
    expect(typeof AssetService).toBe('function');
  });
});

module.exports = tests;

