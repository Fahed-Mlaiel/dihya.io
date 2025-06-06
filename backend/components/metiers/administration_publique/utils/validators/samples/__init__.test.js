// __init__.test.js
// Test d'import du point d'entrée JS samples validators
const entry = require('./__init__.js');
describe('Import samples validators (__init__.js)', () => {
  it('should import usage and data without error', () => {
    expect(entry.usage).toBeDefined();
    expect(entry.data).toBeDefined();
  });
});
