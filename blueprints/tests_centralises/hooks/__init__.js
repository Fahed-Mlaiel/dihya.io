// Initialisation des tests Hooks (Node.js)
const fs = require('fs');
const path = require('path');
const { beforeCreate } = require('../../hooks/asset_hooks.js');

const tests = {};
fs.readdirSync(__dirname).forEach(file => {
  if (file.endsWith('.js') && file !== '__init__.js') {
    const name = file.replace('.js', '');
    tests[name] = require('./' + file);
  }
});

describe('beforeCreate', () => {
  it('existe', () => {
    expect(typeof beforeCreate).toBe('function');
  });
});

module.exports = tests;

