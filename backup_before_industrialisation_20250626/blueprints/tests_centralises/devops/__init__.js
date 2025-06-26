// Initialisation des tests DevOps (Node.js)
const fs = require('fs');
const path = require('path');

const tests = {};
fs.readdirSync(__dirname).forEach(file => {
  if (file.endsWith('.js') && file !== '__init__.js') {
    const name = file.replace('.js', '');
    tests[name] = require('./' + file);
  }
});

module.exports = tests;


describe('dummy', () => { it('should pass', () => { expect(true).toBe(true); }); });
