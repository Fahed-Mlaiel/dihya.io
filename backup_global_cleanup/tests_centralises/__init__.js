// Initialisation avancée des tests Node.js pour tests_centralises
const fs = require('fs');
const path = require('path');

function runAllTests() {
  const testFiles = fs.readdirSync(__dirname).filter(f => f.endsWith('.test.js'));
  let results = [];
  testFiles.forEach(file => {
    const test = require(path.join(__dirname, file));
    results.push(test.run());
  });
  return results;
}

describe('Base tests centralisés', () => {
  it('existe', () => {
    expect(true).toBe(true);
  });
});

module.exports = { runAllTests };

