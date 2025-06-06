// __init__.test.js
// Test d'import du point d'entrée JS fallback validators
const entry = require('./__init__.js');
describe('Import fallback validators (__init__.js)', () => {
  it('should import fallback without error', () => {
    expect(entry).toBeDefined();
  });
});
